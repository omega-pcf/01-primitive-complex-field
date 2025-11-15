# Documentación del Proyecto

Este directorio contiene toda la documentación técnica, guías de estilo, decisiones de diseño, análisis y reportes del proyecto.

## Estructura

```
docs/
├── decisions/          # Decisiones técnicas documentadas
├── style/              # Guías de estilo y formato
├── analysis/           # Análisis y auditorías
├── perplexity/         # Interacciones con Perplexity
├── solutions/          # Soluciones a problemas específicos
├── reports/            # Reportes de verificación y completitud
├── specs/              # Especificaciones formales
└── misc/               # Archivos misceláneos
```

## Decisiones Técnicas

Documentación de decisiones técnicas importantes del proyecto:

- **001-proof-environment-preference.md**: Decisión de favorecer `\begin{proof}...\end{proof}` sobre `\qed` manual
  - Reporte de detección: `001-proof-environment-preference-DETECTION_REPORT.md`
  - Reporte de migración: `001-proof-environment-preference-MIGRATION_REPORT.md`

## Guías de Estilo

- **STYLE_GUIDE.md**: Guía completa de estilo, formato y coherencia para el documento LaTeX
- **EJEMPLO_PROOF_COMPARATIVO.md**: Ejemplos comparativos de uso de entornos `proof`
- **ejemplo_proof.tex**: Archivo LaTeX de ejemplo para pruebas

## Análisis y Auditorías

- **INTRODUCTION_AUDIT.md**: Auditoría de la sección de introducción
- **SECTION_III_ANALYSIS.md**: Análisis de la sección III
- **SECTION_III_AUDIT.md**: Auditoría de la sección III
- **QA_NUMERACION_NXX.md**: QA sobre numeración de secciones n.x.x

## Interacciones con Perplexity

Documentación de consultas y respuestas con Perplexity sobre problemas técnicos:

- **PERPLEXITY_PROMPT_SUBSECTION_NUMBERING.md**: Consulta sobre numeración de subsecciones
- **PERPLEXITY_PROMPT_THEOREM_NUMBERING.md**: Consulta sobre numeración de teoremas
- **PERPLEXITY_REBUTTAL_SUBSECTION_NUMBERING.md**: Primera réplica sobre numeración
- **PERPLEXITY_REBUTTAL_FINAL_SUBSECTION_NUMBERING.md**: Réplica final sobre numeración
- **PERPLEXITY_REBUTTAL_V3_SUBSECTION_NUMBERING.md**: Réplica v3 sobre numeración

## Soluciones a Problemas Específicos

- **SOLUCION_CHKTEX_44_USER_REGEX.md**: Solución a problema de chktex 44 con regex de usuario
- **SOLUCION_CHKTEX_LLAVES_DESBALANCEADAS.md**: Solución a problema de llaves desbalanceadas
- **SOLUCION_TABLAS_LATEX.md**: Solución a problemas con tablas LaTeX

## Reportes

- **PHASE_1A_COMPLETENESS_REPORT.txt**: Reporte de completitud de fase 1A
- **PHASE_1A_VERIFICATION_REPORT.txt**: Reporte de verificación de fase 1A
- **VERIFICATION_REPORT_2025-11-03.txt**: Reporte de verificación del 2025-11-03

## Especificaciones Formales

- **FORMALIZATION_SPEC.md**: Especificación de formalización
- **THEOREM_FORMAT_TEST.md**: Pruebas de formato de teoremas

## Misceláneos

- **paper_md_numeracion_structure.txt**: Estructura de numeración del paper.md
- **SECTION_III_ACTION_CHECKLIST.md**: Checklist de acciones para sección III
- **SECTION_III_QUICK_REFERENCE.txt**: Referencia rápida de sección III
- **ANALISIS_ERRORES_CHKTEX_METHODS.md**: Análisis de errores de chktex en methods.tex

## Uso

Para encontrar documentación específica:

1. **Decisiones técnicas**: Ver `decisions/`
2. **Guías de estilo**: Ver `style/STYLE_GUIDE.md`
3. **Análisis de código**: Ver `analysis/`
4. **Soluciones a problemas**: Ver `solutions/`
5. **Reportes**: Ver `reports/`

## Mantenimiento

Al agregar nueva documentación:

1. Colocar en el directorio apropiado según su tipo
2. Actualizar este README si es necesario
3. Seguir las convenciones de nomenclatura existentes

