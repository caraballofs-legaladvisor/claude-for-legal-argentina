#!/usr/bin/env python3
"""Convierte una carpeta de caso a Markdown e informa qué se perdió en el camino.

Uso:
    python scripts/convertir-caso.py "G:\\Mi unidad\\Casos Actuales\\PedidosYa"
    python scripts/convertir-caso.py <carpeta> --salida <carpeta_md> --recursivo

Escribe un .md por archivo en <carpeta>/_markdown (o --salida) y un INFORME.md
con el detalle por archivo. El informe es la parte importante: markitdown extrae
texto, no imágenes, así que un PDF escaneado o una captura de pantalla producen
un .md vacío o casi vacío. Esos archivos quedan marcados como SIN TEXTO o DUDOSO
para que se lean por otra vía en lugar de darlos por convertidos.
"""

from __future__ import annotations

import argparse
import re
import sys
import traceback
from datetime import datetime
from email import policy
from email.parser import BytesParser
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    sys.exit("Falta markitdown. Instalar con: pip install markitdown-mcp")

try:
    from markdownify import markdownify
except ImportError:  # viene con markitdown, pero no se da por sentado
    markdownify = None

# Extensiones que markitdown no convierte a texto útil. Se listan en el informe
# como pendientes en lugar de intentarse, para no ensuciar la salida con .md vacíos.
SIN_SOPORTE = {
    ".mp4": "video — no se extrae texto",
    ".mov": "video — no se extrae texto",
    ".avi": "video — no se extrae texto",
    ".mp3": "audio — requiere ffmpeg, no instalado",
    ".wav": "audio — requiere ffmpeg, no instalado",
    ".m4a": "audio — requiere ffmpeg, no instalado",
}

# Debajo de este umbral de caracteres se asume que la extracción falló aunque no
# haya tirado error: típicamente un PDF escaneado o una imagen sin OCR.
UMBRAL_DUDOSO = 200

# Los correos comerciales traen URLs de rastreo de cientos de caracteres. No tienen
# valor probatorio y multiplican el tamaño, así que se recorta el destino y se
# conserva el texto del enlace. Por debajo de este largo la URL se deja intacta.
LARGO_URL_MAX = 120
RE_ENLACE_MD = re.compile(r"\[([^\]]*)\]\((https?://[^)]{%d,})\)" % LARGO_URL_MAX)
RE_URL_SUELTA = re.compile(r"(?<![(\[])\bhttps?://\S{%d,}" % LARGO_URL_MAX)


def acortar_url(url: str) -> str:
    """Deja el dominio y marca el recorte, para que se note que la URL está truncada."""
    dominio = url.split("/")[2] if url.count("/") >= 2 else url[:40]
    return f"https://{dominio}/…(url de rastreo recortada)"


def convertir_eml(src: Path) -> str:
    """Convierte un .eml a Markdown legible.

    markitdown no tiene lector de .eml: lo trata como texto plano y vuelca el MIME
    crudo (cabeceras de ruteo, sellos ARC, adjuntos en base64), decenas de miles de
    caracteres de ruido por correo. Acá se extrae solo lo que sirve como prueba:
    encabezado, cuerpo y lista de adjuntos.
    """
    msg = BytesParser(policy=policy.default).parse(src.open("rb"))

    L = [f"# {msg.get('Subject', '(sin asunto)')}", ""]
    for etiqueta, campo in (("De", "From"), ("Para", "To"), ("CC", "Cc"), ("Fecha", "Date")):
        valor = msg.get(campo)
        if valor:
            L.append(f"**{etiqueta}:** {valor}  ")
    L.append("")

    cuerpo, adjuntos = "", []
    for parte in msg.walk():
        if parte.get_content_maintype() == "multipart":
            continue
        nombre = parte.get_filename()
        if parte.get_content_disposition() == "attachment" or nombre:
            adjuntos.append(nombre or "(sin nombre)")
            continue
        tipo = parte.get_content_type()
        if tipo == "text/plain" and not cuerpo:
            cuerpo = parte.get_content()
        elif tipo == "text/html" and not cuerpo and markdownify:
            cuerpo = markdownify(parte.get_content(), strip=["img", "style", "script"])

    cuerpo = RE_ENLACE_MD.sub(lambda m: f"[{m.group(1)}]({acortar_url(m.group(2))})", cuerpo or "")
    cuerpo = RE_URL_SUELTA.sub(lambda m: acortar_url(m.group(0)), cuerpo)

    # Los correos HTML dejan cascadas de líneas en blanco al pasar a Markdown.
    lineas, blancos = [], 0
    for linea in cuerpo.splitlines():
        blancos = blancos + 1 if not linea.strip() else 0
        if blancos < 3:
            lineas.append(linea.rstrip())
    L.append("\n".join(lineas).strip() or "*(sin cuerpo de texto)*")

    if adjuntos:
        L += ["", "## Adjuntos", ""] + [f"- `{a}`" for a in adjuntos]

    return "\n".join(L) + "\n"


def convertir_carpeta(origen: Path, salida: Path, recursivo: bool) -> list[dict]:
    md = MarkItDown()
    patron = "**/*" if recursivo else "*"
    archivos = sorted(p for p in origen.glob(patron) if p.is_file())

    filas: list[dict] = []
    for src in archivos:
        if salida in src.parents:
            continue

        ext = src.suffix.lower()
        fila = {
            "archivo": src.relative_to(origen).as_posix(),
            "bytes_origen": src.stat().st_size,
            "bytes_md": 0,
            "chars": 0,
            "estado": "",
            "nota": "",
            "destino": None,
        }

        if ext in SIN_SOPORTE:
            fila["estado"] = "OMITIDO"
            fila["nota"] = SIN_SOPORTE[ext]
            filas.append(fila)
            continue

        try:
            if ext == ".eml":
                texto = convertir_eml(src)
            else:
                texto = md.convert(str(src)).text_content or ""
        except Exception as exc:  # noqa: BLE001 - se reporta, no se corta la corrida
            fila["estado"] = "ERROR"
            fila["nota"] = f"{type(exc).__name__}: {exc}".replace("\n", " ")[:200]
            filas.append(fila)
            continue

        fila["chars"] = len(texto)
        if not texto.strip():
            fila["estado"] = "SIN TEXTO"
            fila["nota"] = "requiere OCR o lectura visual directa"
        elif len(texto.strip()) < UMBRAL_DUDOSO:
            fila["estado"] = "DUDOSO"
            fila["nota"] = f"solo {len(texto.strip())} caracteres — revisar a mano"
        else:
            fila["estado"] = "OK"

        rel = src.relative_to(origen).with_suffix(".md")
        dst = salida / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(texto, encoding="utf-8")
        fila["bytes_md"] = dst.stat().st_size
        fila["destino"] = dst.relative_to(salida).as_posix()
        filas.append(fila)

    return filas


def escribir_informe(filas: list[dict], origen: Path, salida: Path) -> Path:
    orden = {"SIN TEXTO": 0, "ERROR": 1, "DUDOSO": 2, "OMITIDO": 3, "OK": 4}
    filas_ord = sorted(filas, key=lambda f: (orden[f["estado"]], f["archivo"]))

    total_origen = sum(f["bytes_origen"] for f in filas)
    total_md = sum(f["bytes_md"] for f in filas)
    conteo = {e: sum(1 for f in filas if f["estado"] == e) for e in orden}
    revisar = [f for f in filas_ord if f["estado"] in ("SIN TEXTO", "ERROR", "DUDOSO", "OMITIDO")]

    L = [
        f"# Informe de conversión — {origen.name}",
        "",
        f"Origen: `{origen}`  ",
        f"Salida: `{salida}`  ",
        f"Fecha: {datetime.now():%Y-%m-%d %H:%M}",
        "",
        "## Resumen",
        "",
        f"- Archivos procesados: **{len(filas)}**",
        f"- Convertidos con texto útil (OK): **{conteo['OK']}**",
        f"- Requieren otra vía: **{len(revisar)}** "
        f"(sin texto {conteo['SIN TEXTO']}, dudosos {conteo['DUDOSO']}, "
        f"errores {conteo['ERROR']}, omitidos {conteo['OMITIDO']})",
        f"- Tamaño original: **{total_origen / 1024 / 1024:.1f} MB** → "
        f"Markdown: **{total_md / 1024:.0f} KB**",
        "",
    ]

    if revisar:
        L += [
            "## Atención — estos archivos NO quedaron convertidos",
            "",
            "El `.md` correspondiente está vacío o es inservible. Leerlos por otra vía "
            "(lectura visual directa del archivo, u OCR) antes de darlos por incorporados.",
            "",
            "| Archivo | Estado | Motivo |",
            "| --- | --- | --- |",
        ]
        L += [f"| `{f['archivo']}` | {f['estado']} | {f['nota']} |" for f in revisar]
        L.append("")

    L += [
        "## Detalle completo",
        "",
        "| Archivo | Estado | Caracteres | Origen | Markdown |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for f in filas_ord:
        L.append(
            f"| `{f['archivo']}` | {f['estado']} | {f['chars']:,} | "
            f"{f['bytes_origen'] / 1024:,.0f} KB | {f['bytes_md'] / 1024:,.0f} KB |"
        )
    L.append("")

    ruta = salida / "INFORME.md"
    ruta.write_text("\n".join(L), encoding="utf-8")
    return ruta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpeta", type=Path, help="Carpeta del caso a convertir")
    ap.add_argument("--salida", type=Path, default=None, help="Destino (default: <carpeta>/_markdown)")
    ap.add_argument("--recursivo", action="store_true", help="Incluir subcarpetas")
    args = ap.parse_args()

    origen = args.carpeta.resolve()
    if not origen.is_dir():
        sys.exit(f"No es una carpeta: {origen}")
    salida = (args.salida.resolve() if args.salida else origen / "_markdown")
    salida.mkdir(parents=True, exist_ok=True)

    filas = convertir_carpeta(origen, salida, args.recursivo)
    if not filas:
        sys.exit(f"No se encontraron archivos en {origen}")

    informe = escribir_informe(filas, origen, salida)
    revisar = [f for f in filas if f["estado"] != "OK"]

    print(f"{len(filas)} archivos procesados — {len(filas) - len(revisar)} OK, {len(revisar)} a revisar")
    print(f"Informe: {informe}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception:
        traceback.print_exc()
        sys.exit(1)
