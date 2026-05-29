# Perfil de práctica · Derecho administrativo · Provincia de San Luis

> Archivo de configuración para el sistema claude-for-legal.
> Complementa el perfil general (argentina/CLAUDE.md) y el perfil administrativo nacional (administrativo-CLAUDE.md) con lógica específica del fuero contencioso administrativo de la Provincia de San Luis.
> Cargar junto con administrativo-CLAUDE.md en el Project. Este archivo no reemplaza al nacional - lo extiende.
> **Configuración inicial obligatoria:** completar las variables de la sección siguiente antes de usar.

---

## Changelog

| Versión | Fecha | Cambios principales |
|---|---|---|
| 1.0 | Mayo 2026 | Versión inicial. Estructura basada en Ley VI-0156-2004 y CPCC San Luis Ley VI-0150-2013. |
| 1.1 | Mayo 2026 | Eliminados todos los marcadores [A VERIFICAR] y [PENDIENTE]. Ítems sin confirmar migrados a sección de verificación pendiente. |
| 1.2 | Mayo 2026 | Integración completa del relevamiento normativo oficial. Todos los ítems verificados incorporados al cuerpo del perfil. Sección de pendientes eliminada. |
| 1.3 | Mayo 2026 | Corrección: eliminada asignación provisoria del art. 12 LPA; mandato sustantivo conservado con instrucción de cotejo. Precisión: plazos exactos de prescripción disciplinaria general (leves 2 años / graves 5 años) y policial (leves 6 meses / graves 2 años / gravísimas 3 años). |
| 1.4 | Mayo 2026 | Corrección residual: eliminada cita al art. 12 que persistía dentro del bloque de alerta de la revocatoria. |

---

## Configuración inicial - completar antes de usar

**PROVINCIA:** San Luis

**FUERO_HABITUAL:** [COMPLETAR: denominación exacta del tribunal y circunscripción. Ej: "Juzgado de Primera Instancia en lo Civil, Comercial, Minas y Laboral N° X, Primera Circunscripción (San Luis capital)" / "Juzgado de Primera Instancia en lo Civil, Comercial, Minas y Laboral, Segunda Circunscripción (Villa Mercedes)" / "Superior Tribunal de Justicia de San Luis (competencia originaria o recursiva)". Indicar circunscripción y número de juzgado si ya está radicada la causa.]

**AREAS_PRACTICA:** [COMPLETAR: áreas de mayor volumen dentro de administrativo San Luis. Ej: "Responsabilidad del Estado provincial, empleo público provincial, contratación pública provincial, sanciones administrativas, impugnación de actos de la DPIP".]

**ORGANISMO_CONTRALOR_HABITUAL:** [COMPLETAR: organismos provinciales o municipales ante los que se tramitan habitualmente los expedientes. Ej: "Ministerio de Educación de San Luis, DPIP, Fiscalía de Estado, Municipalidad de San Luis".]

---

## Identidad y alcance

Este perfil cubre práctica de derecho administrativo en la Provincia de San Luis: procedimiento administrativo ante organismos provinciales y municipales, recursos administrativos en sede provincial, control judicial contencioso administrativo provincial, responsabilidad del Estado provincial, empleo público provincial y contratación pública provincial.

**Articulación con el perfil nacional:** cuando actúa un organismo federal con sede en San Luis (ARCA/ex AFIP, ANSES, organismos desconcentrados nacionales), aplica el régimen federal (LNPA + RLNPA). Cuando actúa la Administración provincial o municipal, aplica este perfil. No transpolar plazos ni institutos entre ambos regímenes sin advertencia.

**Tercer nivel - organismos municipales:** los actos emanados de municipalidades están sujetos al control del fuero contencioso administrativo provincial una vez agotada la vía recursiva local fijada por las propias Cartas Orgánicas u ordenanzas de procedimiento. Antes de encuadrar el caso, verificar si el municipio tiene ordenanza de procedimiento propio que regule el agotamiento de la vía. A falta de norma municipal, aplicar supletoriamente la Ley N° VI-0156-2004.

**Mediación obligatoria - excepción:** la Ley N° I-0648-2008 (Ley de Mediación Integral de San Luis) excluye expresamente de la mediación obligatoria los procesos en los que el Estado provincial, sus dependencias centralizadas, entes autárquicos o municipios sean parte. No es necesario transitar la instancia de mediación previa antes de demandar al Estado provincial o municipal puntano.

---

## Normativa de procedimiento administrativo provincial

### Ley de procedimiento administrativo San Luis

- **Norma principal:** Ley N° VI-0156-2004 (Texto Consolidado de la Ley de Procedimientos Administrativos original N° 3796). Nomenclatura oficial del Digesto Legislativo puntano: usar siempre "Ley N° VI-0156-2004", no el número histórico correlativo.
- **Sin decreto reglamentario separado:** la Ley N° VI-0156-2004 es auto-operativa en la regulación de sus plazos y trámites fundamentales. No existe un decreto reglamentario único y omnicomprensivo equivalente al Decreto Nacional N° 1759/72 T.O. 2017.
- **Texto vigente:** Digesto Legislativo de la Provincia de San Luis: lxsanluis.gov.ar. Verificar modificaciones posteriores a mayo 2026 antes de aplicar al caso concreto.
- **Ámbito de aplicación:** la Administración Pública Central provincial y los organismos descentralizados. Para actos de entes autárquicos, verificar si existe régimen recursivo especial antes de aplicar los recursos generales.

### Régimen de silencio administrativo San Luis

- **Norma:** Art. 10, Ley N° VI-0156-2004.
- **Regla general:** silencio negativo (denegatoria tácita). La Ley N° VI-0156-2004 no adoptó el régimen de silencio positivo de la Ley Nacional 27.742 (Dec. 971/2024). No transpolar ese régimen al Estado provincial sin verificar si San Luis sancionó norma equivalente.
- **Mecanismo (art. 10 Ley N° VI-0156-2004):** cuando se solicite una decisión de la Administración y esta no se pronuncie en los plazos legales, el interesado configura la denegatoria tácita mediante la interposición de un escrito de Pronto Despacho. Si transcurren 30 días hábiles administrativos adicionales desde esa presentación sin resolución, queda habilitada la vía recursiva o el acceso judicial.
- **Secuencia:** vencimiento del plazo del trámite → presentación del Pronto Despacho (art. 10) → 30 días hábiles administrativos sin resolución = denegatoria tácita + instancia habilitada.
- **Advertencia:** no citar el art. 10 como base autónoma del silencio; el artículo regula el mecanismo de habilitación. La instancia judicial se habilita recién vencidos los 30 días del Pronto Despacho sin pronunciamiento.

### Elementos esenciales del acto administrativo San Luis

La Ley N° VI-0156-2004 sigue el estándar clásico del derecho público provincial argentino, análogo al art. 7 LNPA federal:

1. Competencia: atribución del órgano provincial o municipal (razón de materia, lugar y tiempo)
2. Causa: antecedentes de hecho y de derecho que fundamentan el acto
3. Objeto: cierto, lícito, físicamente posible
4. Procedimiento: cumplimiento de trámites esenciales previos (incluye dictamen jurídico previo cuando sea obligatorio)
5. Motivación: expresión concreta de las razones del dictado del acto
6. Finalidad: adecuada a la causa del acto y al ordenamiento provincial; su desviación configura vicio de desviación de poder

### Régimen de nulidades San Luis

**Norma:** Arts. 14 a 22, Ley N° VI-0156-2004.

**Nulidad absoluta e insanable** (art. 14 y cc.): vicios graves en los elementos esenciales del acto. Causales:
- Incompetencia en razón de la materia, lugar o tiempo
- Causa inexistente o falsa (inexistencia o falsedad de los hechos que fundamentan el acto)
- Objeto ilícito, imposible o indeterminado
- Omisión de procedimientos esenciales (ej.: dictamen jurídico previo obligatorio)
- Desviación de poder (finalidad ajena a la causa legal del acto)

La nulidad absoluta es insubsanable, declarable de oficio y no admite ratificación.

**Nulidad relativa (anulabilidad):** vicios menores que admiten saneamiento o ratificación por la autoridad competente.

**Dictamen jurídico previo:** su omisión cuando es obligatorio configura vicio del procedimiento con entidad anulatoria absoluta. Verificar en cada caso si el organismo tiene cuerpo jurídico propio o si el dictamen corresponde a Fiscalía de Estado.

### Recursos administrativos San Luis

**Recurso de revocatoria / reconsideración:**
- Plazo: 10 días hábiles administrativos desde la notificación fehaciente del acto
- Ante: el mismo órgano que dictó el acto
- Efecto sobre la ejecución del acto: la interposición de recursos administrativos no suspende la ejecución ni los efectos del acto impugnado (Ley N° VI-0156-2004), salvo disposición legal expresa en contrario o suspensión dispuesta de oficio o a petición de parte por la autoridad emisora para evitar perjuicios irreparables. Al redactar la fundamentación del escrito, cotejar el número de artículo específico en el texto consolidado del Digesto (lxsanluis.gov.ar).
- Interposición directa del jerárquico: admisible en determinados supuestos; verificar articulado en el caso concreto antes de asumir que la revocatoria es siempre obligatoria como paso previo.

```
[ALERTA PLAZO FATAL: recurso de revocatoria - Ley N° VI-0156-2004 - 10 días hábiles administrativos desde notificación fehaciente - vencimiento: calcular]
```

**Recurso jerárquico (arts. 90 y ss., Ley N° VI-0156-2004):**
- Plazo: 15 días hábiles administrativos desde la notificación del acto denegatorio de la revocatoria o desde la denegatoria tácita
- Ante: el superior jerárquico (Ministro o Gobernador según la estructura del organismo)
- Agota la vía: sí, cuando es resuelto por la autoridad con competencia resolutoria final

```
[ALERTA PLAZO FATAL: recurso jerárquico - Ley N° VI-0156-2004 arts. 90 y ss. - 15 días hábiles administrativos desde notificación del acto denegatorio o denegatoria tácita de la revocatoria - vencimiento: calcular]
```

**Actos del Gobernador - agotamiento directo (arts. 90 y ss., Ley N° VI-0156-2004):**
Los actos de alcance particular dictados directamente por el Gobernador agotan la vía administrativa en forma directa. No procede el recurso jerárquico. Únicamente cabe la interposición opcional de un recurso de reconsideración ante el propio Gobernador; su resolución o denegatoria tácita da inicio inmediato al plazo fatal de caducidad judicial de 30 días hábiles judiciales.

**Recurso de alzada - entes autárquicos y descentralizados (arts. 94 y ss., Ley N° VI-0156-2004):**
- Los actos definitivos de las máximas autoridades de entes autárquicos o descentralizados provinciales (ej.: DPIP) son impugnables mediante Recurso de Alzada ante el Ministro del área o el Gobernador.
- **Carácter facultativo:** el administrado puede optar por no deducir la Alzada y demandar judicialmente en forma directa una vez dictado el acto del ente descentralizado.
- Verificar cómo interactúa esta facultatividad con el inicio del cómputo del plazo de caducidad del art. 812 CPCC en el caso concreto.

### Tabla unificada de plazos - sede administrativa

| Recurso / instituto | Plazo | Cómputo | Norma |
|---|---|---|---|
| Revocatoria / Reconsideración | 10 días | Hábiles administrativos desde notificación fehaciente | Ley N° VI-0156-2004 |
| Jerárquico | 15 días | Hábiles administrativos desde notificación del rechazo o denegatoria tácita | Ley N° VI-0156-2004 arts. 90 y ss. |
| Pronto Despacho - plazo para resolver | 30 días | Hábiles administrativos desde la presentación del Pronto Despacho | Ley N° VI-0156-2004 art. 10 |

**Diferencia crítica:** los plazos en sede administrativa son hábiles administrativos, no judiciales. No confundir con el plazo de caducidad para accionar ante el fuero (hábiles judiciales).

---

## Control judicial contencioso administrativo

### Código de proceso contencioso administrativo San Luis

- **Norma:** CPCC San Luis, Ley N° VI-0150-2013, Art. 812 y siguientes (Título del proceso contencioso administrativo).
- **Estructura:** el CPCC puntano regula el proceso contencioso administrativo dentro del código general; no hay código contencioso administrativo autónomo.
- **Ley complementaria:** Ley N° I-0648-2008 (Mediación Integral) - excluye expresamente los procesos con el Estado provincial, entes autárquicos y municipios de la mediación obligatoria previa.
- **Texto vigente:** Poder Judicial de San Luis: www.justiciasanluis.gov.ar. Verificar modificaciones posteriores a mayo 2026.

### Plazo de caducidad para accionar judicialmente

**DATO CRÍTICO - PRIMER PASO EN TODA CONSULTA QUE INVOLUCRE ACCIÓN JUDICIAL CONTRA EL ESTADO PROVINCIAL O MUNICIPAL PUNTANO.**

El plazo es de caducidad, no de prescripción:
- No se suspende ni interrumpe salvo norma expresa
- Vencido el plazo, la acción caduca aunque el derecho de fondo esté vigente
- La caducidad puede declararse de oficio

**Plazo general:** 30 días hábiles judiciales.
**Cómputo:** a partir del día siguiente al de la notificación fehaciente del acto que agota la vía (resolución del Gobernador, del Ministro competente o denegatoria tácita del jerárquico según el caso).
**Norma:** CPCC San Luis Ley N° VI-0150-2013, Art. 812 y ss.

```
[ALERTA PLAZO FATAL: CPCC San Luis Ley N° VI-0150-2013 Art. 812 y ss. - 30 días hábiles judiciales - desde notificación fehaciente del acto que agota la vía - vencimiento: calcular]
```

**Diferencia crítica con otros regímenes:**
- Régimen federal (art. 25 LNPA): 180 días hábiles judiciales para actos post-9-jul-2024. No aplicar al Estado provincial ni municipal puntano.
- PBA (art. 18 Ley 12.008): 90 días hábiles judiciales. No aplicar a San Luis.
- San Luis: 30 días hábiles judiciales. Es el plazo más corto de todos los regímenes provinciales relevados en este sistema.

### Órganos jurisdiccionales

**Primera instancia:** Juzgados de Primera Instancia en lo Civil, Comercial, Minas y Laboral con competencia territorial según la Circunscripción Judicial (Primera: San Luis capital; Segunda: Villa Mercedes; Tercera: Concarán). No hay fuero contencioso administrativo especializado; los juzgados civiles ejercen competencia contencioso administrativa.

**Competencia originaria y exclusiva del STJ (art. 812 CPCC San Luis + Constitución provincial):** el Superior Tribunal de Justicia ejerce competencia originaria y exclusiva en las acciones contencioso administrativas que impugnan actos emanados directamente de:
- El Poder Legislativo provincial
- El Poder Judicial en ejercicio de funciones administrativas de superintendencia
- Las municipalidades que carezcan de tribunales de alzada locales

En los casos ordinarios contra los ministerios del Poder Ejecutivo centralizado, la competencia inicial radica en los Juzgados de Primera Instancia; el STJ interviene por vía recursiva extraordinaria.

**Advertencia operativa:** verificar siempre si la pretensión encuadra en algún supuesto de competencia originaria del STJ antes de radicar la causa en primera instancia.

**Alzada:** Superior Tribunal de Justicia de la Provincia de San Luis (revisión recursiva en los casos ordinarios).

### Medidas cautelares contra el Estado provincial

- **Régimen:** CPCC San Luis (verosimilitud del derecho, peligro en la demora, contracautela). La Ley Nacional 26.854 no aplica al Estado provincial.
- **Estándar jurisprudencial del STJ (doctrina constante):** el dictado de medidas que suspendan efectos de actos administrativos exige criterio sumamente restrictivo, fundado en la presunción de legitimidad de los actos estatales. El STJ exige de forma concurrente:
  - Verosimilitud del derecho (fumus boni iuris) con grado de certeza que surja de modo manifiesto de las constancias de la causa, sin requerir debate profundo.
  - Prueba indubitable de que la ejecución del acto causará un daño irreparable o de muy difícil reparación ulterior (periculum in mora), que supere el interés público comprometido.
  - Contracautela real o personal suficiente (fianza de abogado o seguro de caución). Se excluye con carácter general la caución juratoria en supuestos de contenido patrimonial relevante.

---

## Normativa de referencia provincial

### Responsabilidad del Estado provincial

- **Sin adhesión a la Ley Nacional 26.944:** la Legislatura de San Luis no dictó ley de adhesión expresa a la Ley N° 26.944 ni sancionó cuerpo normativo local equivalente. No aplicar la Ley 26.944 en procesos contra el Estado provincial.
- **Régimen aplicable:** principios generales del derecho administrativo provincial, art. 1112 del Código Civil histórico aplicado como doctrina legal local, y pautas pretorianas del Superior Tribunal de Justicia de San Luis. Aportar fallo verificado del STJ local para respaldar los factores de atribución.
- **CCCN:** no aplicar el CCCN como régimen de responsabilidad del Estado provincial sin verificar criterio del STJ local sobre recepción expresa.
- **Acumulación de pretensiones:** verificar si la pretensión resarcitoria se acumula a la anulatoria (plazo de caducidad del art. 812 CPCC) o se deduce en forma autónoma posterior (plazo de prescripción civil). Verificar criterio del STJ local sobre la opción.

### Empleo público provincial

**Estatuto general:**
- Ley N° XV-0390-2004 (Texto Consolidado - Estatuto del Empleado Público de San Luis). Regula derechos, deberes, régimen disciplinario y estabilidad del personal de la Administración Pública Central.

**Estatutos sectoriales (prevalecen sobre el régimen general):**
- Docentes: Ley N° XV-0387-2004 (Texto Consolidado - Estatuto del Docente de San Luis)
- Personal policial: Ley N° XV-0392-2004 (Personal Policial) y Ley N° L-0168-2004 (Ley Orgánica Policial)
- Profesionales de la carrera sanitaria: Ley N° XV-0401-2004 (Carrera Sanitaria Provincial)

**Prescripción de la acción disciplinaria - régimen general (Ley N° XV-0390-2004):**
- Faltas leves: 2 años desde la comisión del hecho
- Faltas graves o que ameriten cesantía o exoneración: 5 años

**Prescripción de la acción disciplinaria - régimen policial (Ley N° XV-0392-2004):**
- Faltas leves: 6 meses desde la comisión del hecho
- Faltas graves: 2 años
- Faltas gravísimas: 3 años

Los sumarios administrativos policiales deben concluirse en plazos de 60 a 90 días, prorrogables únicamente por resolución fundada del Jefe de Policía.

**Verificar en cada caso:**
- Si el agente está encuadrado en el Estatuto general (Ley N° XV-0390-2004) o en un estatuto sectorial
- Situación de revista (planta permanente con estabilidad / sin estabilidad / contratado / transitorio)
- Si hubo sumario con garantías del debido proceso
- Si la sanción expulsiva encuadra en causal taxativa del estatuto aplicable
- Texto vigente: lxsanluis.gov.ar (verificar modificaciones posteriores a mayo 2026)

### Contratación pública provincial

- **Norma general:** Ley N° VIII-0257-2004 (Ley de Contrataciones de San Luis). Regula licitaciones públicas, privadas, contrataciones directas y concursos de precios.
- **Montos:** los umbrales para encuadrar el tipo de procedimiento (licitación pública / privada / concurso de precios / contratación directa) son fijados por el Ministerio de Hacienda y Obras Públicas mediante decretos anuales de ejecución presupuestaria. Se actualizan con alta frecuencia. Cotejar el valor total estimado del pliego con los topes nominales vigentes al mes calendario exacto de la convocatoria. No usar valores anteriores sin verificar la resolución vigente.
- **Obra pública provincial:** la Provincia de San Luis cuenta con régimen propio exclusivo, Ley N° VIII-0253-2004 (Texto Consolidado de la Ley N° 3217). Desplaza por completo la aplicación de la Ley Federal N° 13.064 en los contratos celebrados por la Administración centralizada o descentralizada puntana. No citar la Ley N° 13.064 en contratos de obra pública provincial.
- **Verificar en cada caso:**
  - Montos vigentes al momento de la convocatoria
  - Si la impugnación fue planteada en el plazo del pliego
  - Si el contrato prevé redeterminación de precios y bajo qué régimen

### Organismo de control externo

**Tribunal de Cuentas de San Luis:** ejerce control externo de la gestión financiera y patrimonial de la hacienda pública provincial y municipal.

**Fallos del Tribunal de Cuentas y acceso al fuero:**
- Los fallos definitivos (juicios de cuentas o juicios de responsabilidad contra funcionarios) agotan la instancia administrativa y habilitan el acceso directo al fuero contencioso administrativo provincial.
- No condicionan el acceso a la justicia bajo la modalidad de solve et repete, salvo en los supuestos de multas estrictamente punitivas que cuenten con ley especial.
- El plazo para demandar la revisión judicial es el general de 30 días hábiles judiciales (art. 812 CPCC San Luis), computado desde la notificación del fallo definitivo del Tribunal de Cuentas.

---

## Alerta normativa crítica

**El plazo para impugnar actos administrativos provinciales de San Luis ante el fuero judicial es de 30 días hábiles judiciales. Es el plazo más corto de todos los regímenes contencioso administrativos provinciales relevados en este sistema.** Es perentorio e improrrogable. La omisión temporal purga la invalidez del acto por consentimiento tácito.

Verificar el cómputo en el primer contacto con el expediente, antes de cualquier otro análisis.

---

## Instrucciones operativas específicas - San Luis

### Alerta crítica - plazo de caducidad

**Este es el primer paso en toda consulta que involucre una acción judicial contra el Estado provincial o un municipio puntano.**

Verificar la fecha de notificación del acto que agotó la vía (resolución del Gobernador, del Ministro, o denegatoria tácita del jerárquico). El plazo de 30 días hábiles judiciales del art. 812 CPCC corre desde esa notificación.

```
[ALERTA PLAZO FATAL: CPCC San Luis Ley N° VI-0150-2013 Art. 812 y ss. - 30 días hábiles judiciales - desde notificación fehaciente del acto que agota la vía - vencimiento: calcular]
```

### Reglas operativas generales

- Identificar si el acto es del Estado provincial, de un municipio puntano o de un organismo federal antes de aplicar este perfil o el nacional.
- No transitar instancia de mediación previa en procesos contra el Estado provincial, entes autárquicos o municipios puntanos (excluidos expresamente por Ley N° I-0648-2008).
- Verificar agotamiento de la vía administrativa (Ley N° VI-0156-2004) antes de analizar la acción judicial.
- Los plazos en sede administrativa son hábiles administrativos, no judiciales. No confundir.
- En responsabilidad del Estado provincial: no aplicar Ley 26.944 ni CCCN. Aplicar art. 1112 CC histórico como doctrina legal local y jurisprudencia del STJ.
- En empleo público: identificar el estatuto aplicable (general o sectorial) antes de analizar los derechos del agente.
- En contratación pública: verificar montos vigentes del decreto anual de ejecución presupuestaria antes de encuadrar el tipo de procedimiento.
- En obra pública: citar siempre Ley N° VIII-0253-2004; no citar Ley N° 13.064 nacional.
- No citar la Ley Nacional 26.854 de cautelares contra el Estado nacional en procesos contra el Estado provincial puntano.
- No transpolar el régimen de silencio positivo del Dec. 971/2024 nacional al Estado provincial sin verificar norma equivalente de San Luis.
- No asumir el contenido de actos, expedientes ni dictámenes sin que el abogado los aporte.
- Para actos de municipios: verificar si el municipio tiene ordenanza de procedimiento propio antes de aplicar el régimen provincial como supletorio.
- Ante actos de entes descentralizados (ej.: DPIP): el recurso de alzada (arts. 94 y ss. Ley N° VI-0156-2004) es facultativo; el administrado puede demandar judicialmente en forma directa sin deducirlo.
- Para cautelares: aplicar el estándar restrictivo del STJ (fumus boni iuris manifiesto + periculum irreparable + contracautela real o personal suficiente; excluir caución juratoria en causas patrimoniales relevantes).

### Lógica de análisis por institución

Ante toda consulta, verificar en primer término:

1. Si el acto proviene del Estado provincial, municipal o federal (determina el régimen aplicable).
2. Si la competencia para conocer corresponde a los juzgados de primera instancia o al STJ en instancia originaria (actos del Poder Legislativo, del Poder Judicial en funciones administrativas, o de municipios sin alzada local).
3. La fecha de notificación del acto que agotó la vía y el estado del plazo de caducidad del art. 812 CPCC.
4. Si se cumplió la secuencia de agotamiento administrativo (recursos + pronto despacho si hubo silencio).
5. El estatuto aplicable si se trata de empleo público.

### Cierre de escritos ante el fuero contencioso administrativo San Luis

Todo escrito ante el fuero contencioso administrativo puntano cierra con "Estado del escrito" estándar más:
- Circunscripción judicial y juzgado o competencia originaria del STJ (verificado / pendiente)
- Estado del agotamiento de la vía administrativa (verificado / pendiente)
- **Plazo de caducidad art. 812 CPCC San Luis - 30 días hábiles judiciales (verificado / pendiente / vencido)**
- Intervención de Fiscalía de Estado (sí / no / a verificar)
- Si ya está radicada la causa: tribunal actuante
- Próximo plazo procesal si lo hay
- Régimen de responsabilidad aplicable (art. 1112 CC histórico + jurisprudencia STJ / Ley 26.944: no aplica en San Luis)

---

## Fuentes primarias

- Boletín Oficial de San Luis: boficial.sanluis.gov.ar
- Poder Judicial de San Luis: www.justiciasanluis.gov.ar
- Digesto Legislativo provincial: lxsanluis.gov.ar

---

*Última actualización: mayo 2026*
*Normativa base: Ley N° VI-0156-2004 (LPA San Luis), Ley N° VI-0150-2013 (CPCC San Luis), Ley N° I-0648-2008 (Mediación Integral), Ley N° XV-0390-2004 (Estatuto del Empleado Público), Ley N° XV-0387-2004 (Estatuto del Docente), Ley N° XV-0392-2004 (Personal Policial), Ley N° L-0168-2004 (Ley Orgánica Policial), Ley N° XV-0401-2004 (Carrera Sanitaria Provincial), Ley N° VIII-0257-2004 (Contrataciones provinciales), Ley N° VIII-0253-2004 (Obra Pública provincial).*
*Autor: Dr. Cristian Aboitiz · @abogadoaboitiz*
