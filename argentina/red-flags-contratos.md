# Red flags para revisión de contratos · Derecho argentino

Lista de alertas prioritarias para análisis automatizado de contratos bajo derecho argentino continental. Ordenadas por nivel de riesgo.

---

## Nulidad absoluta

Estas situaciones invalidan la cláusula de pleno derecho. Marcar siempre, sin excepción.

### 1. Renuncia anticipada a derechos irrenunciables

**Normas:** Art. 12 LCT (laboral) / Art. 37 LDC (consumo) / Arts. 944-954 CCCN (general)

Cualquier cláusula que intente hacer renunciar al trabajador o al consumidor a derechos de orden público es nula. El contrato subsiste sin la cláusula.

Formas habituales:
- "El trabajador renuncia a cualquier diferencia salarial futura"
- "El consumidor acepta renunciar a cualquier acción por daños derivados del servicio"
- "Las partes acuerdan que el presente contrato satisface íntegramente cualquier crédito laboral"

### 2. Prórroga de jurisdicción al extranjero en contratos de consumo

**Norma:** Art. 2654 CCCN - prohibición expresa

Contexto habitual: contratos de plataformas digitales, servicios SaaS, e-commerce internacional, términos y condiciones de servicios con sede en EE.UU. o Europa.

Forma habitual: "Any dispute arising from this agreement shall be submitted to the exclusive jurisdiction of the courts of [estado extranjero]"

### 3. Limitación de responsabilidad por dolo o culpa grave

**Norma:** Art. 1743 CCCN - nulidad sin excepción

Cualquier cláusula que limite o excluya la responsabilidad del predisponente por su propio dolo o culpa grave es inválida, independientemente de la forma en que esté redactada.

Formas habituales:
- "En ningún caso la parte X será responsable por daños directos o indirectos..."
- "La responsabilidad total de X no excederá el monto pagado por el servicio..."
- "X no será responsable por fallas en la prestación causadas por cualquier motivo..."

### 4. Cláusulas abusivas en contratos de adhesión

**Normas:** Arts. 985-989 CCCN / Arts. 37-38 LDC

Contrastar cada cláusula limitativa o excluyente contra el estándar de desequilibrio significativo entre derechos y obligaciones. La lista del art. 37 LDC es enunciativa, no taxativa.

Tipos más frecuentes:
- Modificación unilateral de precio o condiciones sin causa objetiva
- Exclusión o limitación de responsabilidad por vicios o defectos
- Inversión de la carga probatoria en perjuicio del consumidor
- Renuncia anticipada a derechos procesales (fuero, recurso)

---

## Riesgo alto

Marcar y desarrollar en el informe. Requieren análisis específico o propuesta de redacción alternativa.

### 5. Ausencia de mecanismo de actualización en contratos de largo plazo

**Contexto:** En Argentina, un contrato de tracto sucesivo (locación de servicios, suministro, mantenimiento, licencia de uso) sin cláusula de actualización es un pasivo potencial para la parte acreedora de dinero.

Verificar si el plazo supera seis meses. Si supera: alertar y proponer alguna de estas opciones:
- Cláusula de ajuste por índice (ICL, IPC, RIPTE según el tipo de contrato)
- Precio en moneda extranjera con indicación de tipo de cambio aplicable
- Revisión periódica pactada con mecanismo de negociación

### 6. Pacto comisorio sin notificación previa

**Normas:** Arts. 1083-1089 CCCN

Verificar que el mecanismo de resolución contractual sea compatible con el régimen legal: intimación previa con plazo razonable (art. 1088 CCCN) o resolución de pleno derecho cuando el incumplimiento hace imposible la finalidad del contrato (art. 1089 CCCN).

Formas problemáticas:
- "El incumplimiento de cualquier obligación dará derecho a resolver el contrato de pleno derecho y de manera inmediata"
- Ausencia total de cláusula resolutoria cuando el contrato es de larga duración

### 7. Confidencialidad sin plazo determinado

**Riesgo:** Nulidad parcial por indeterminación del objeto o plazo irrazonable según fuero y circunstancias.

Verificar: si la obligación de confidencialidad no tiene plazo o tiene un plazo irrazonablemente extenso (más de 5 años para información no constitutiva de secreto comercial), alertar.

Proponer: plazo máximo razonable según el tipo de información protegida, con indicación de las excepciones estándar (información pública, obtenida de tercero, requerida judicialmente).

### 8. Arbitraje con sede en el extranjero

Verificar antes de dar el visto bueno:
- Ley aplicable al fondo del asunto
- Ejecutabilidad del laudo en Argentina (Convención de Nueva York, aprobada por Ley 23.619)
- Compatibilidad con orden público argentino
- En contratos de consumo: la prórroga a arbitraje extranjero puede ser inválida (ver red flag 2)

Marcar como pendiente de análisis específico si el contrato no aporta suficiente información sobre el tipo de arbitraje (ad hoc o institucional) y las reglas aplicables.

---

## Riesgo medio

Consignar en el informe. No bloquean el avance pero requieren atención del abogado.

### 9. Ausencia de domicilio especial constituido en Argentina

Relevancia para: notificaciones fehacientes, notificaciones procesales, eventual ejecución judicial.

En contratos con personas jurídicas extranjeras: verificar si tienen sucursal inscripta en Argentina (art. 118 LGS) y si el domicilio contractual coincide con el registral.

### 10. Moneda de pago en divisas sin cláusula de opción de pago en pesos

Verificar compatibilidad con normativa cambiaria vigente al momento de la consulta. Las restricciones cambiarias en Argentina varían con frecuencia: alertar sobre la necesidad de verificación actualizada antes de firmar.

### 11. Garantías sin inscripción registral cuando corresponde

- Prenda con registro (Decreto-Ley 15.348/46): verificar inscripción y vigencia
- Hipoteca (arts. 2205-2211 CCCN): verificar inscripción registral y rango
- Anticresis (arts. 2212-2218 CCCN): verificar instrumentación y entrega de la cosa
- Garantías sobre acciones o cuotas sociales: verificar régimen aplicable según tipo societario

### 12. Plazo de prescripción no contemplado

Verificar que el contrato no intente modificar los plazos de prescripción legales (arts. 2532-2564 CCCN). Las partes pueden acortar o ampliar plazos dentro de los límites legales (art. 2533 CCCN), pero no pueden eliminarlos ni fijar plazos irrazonables.

---

## Notas de uso

Esta lista es un punto de partida para el análisis automatizado, no un checklist exhaustivo. No reemplaza la revisión del abogado sobre el contrato específico, el contexto de la negociación y la relación entre las partes.

Los red flags marcan situaciones que requieren atención. La evaluación final sobre si una cláusula es o no válida, y sobre qué hacer al respecto, es siempre responsabilidad del abogado.

---

*Última actualización: mayo 2026*  
*Normativa base: CCCN (Ley 26.994), LCT (Ley 20.744), LDC (Ley 24.240), Ley 25.326*  
*Autor: Dr. Cristian Aboitiz · [@abogadoaboitiz](https://x.com/abogadoaboitiz)*
