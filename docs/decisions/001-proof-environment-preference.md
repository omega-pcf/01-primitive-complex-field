# Decisión Técnica 001: Preferencia por Entorno `\begin{proof}...\end{proof}`

**Fecha**: 2025-01-28  
**Estado**: Aprobada  
**Impacto**: Migración de ~37 instancias en `src/chapters/`

## Decisión

Favorecer el uso de `\begin{proof}...\end{proof}` sobre `\qed` manual para todas las pruebas matemáticas en el documento.

## Contexto

Durante la revisión del código fuente, se identificaron múltiples instancias donde se usa `\qed` manual dentro de entornos `proof`, lo cual es redundante ya que `amsthm` coloca automáticamente el símbolo QED al final del entorno `proof`.

Además, se encontraron casos donde se usa `\qed` manual fuera de entornos `proof`, lo que genera inconsistencia en el formato y espaciado.

## Justificación

### Ventajas de `\begin{proof}...\end{proof}`

1. **Formato automático consistente**: El entorno `proof` de `amsthm` proporciona:
   - Indentación automática del texto de la prueba
   - Espaciado consistente antes y después
   - Símbolo QED (□) colocado automáticamente al final

2. **Compatibilidad**: 
   - Compatible con `amsthm` (ya cargado en el proyecto)
   - Funciona correctamente con `hyperref` y referencias cruzadas
   - Compatible con macros de referencias (`\dref`, `\pref`, `\tref`, etc.)

3. **Mantenibilidad**:
   - Cambios globales de formato se pueden hacer fácilmente
   - No requiere recordar agregar `\qed` manualmente
   - Elimina la necesidad de `% chktex 1` para suprimir warnings

4. **Consistencia**:
   - Todas las pruebas tienen el mismo formato
   - No hay riesgo de olvidar el símbolo QED
   - El formato es predecible y profesional

### Desventajas de `\qed` Manual

1. **Redundancia**: Cuando se usa dentro de `\begin{proof}...\end{proof}`, el `\qed` manual es redundante
2. **Inconsistencia**: Formato inconsistente si algunas pruebas usan `\qed` y otras no
3. **Mantenibilidad**: Fácil olvidar el `\qed` en alguna prueba
4. **Warnings**: Requiere `% chktex 1` para evitar warnings del linter

## Referencias

- **Guía de Estilo**: `docs/style/STYLE_GUIDE.md` (Sección 13: "ENTORNO `proof` vs `\qed` MANUAL")
- **Ejemplos Comparativos**: `docs/style/EJEMPLO_PROOF_COMPARATIVO.md`

## Impacto

### Archivos Afectados

- `src/chapters/methods.tex`: 5 instancias de `\qed` redundantes eliminadas
- `src/chapters/results.tex`: Sin cambios (ya correcto)
- Otros archivos: Verificados, sin cambios necesarios

### Tipos de Cambios Requeridos

1. **Eliminar `\qed` redundantes**: Todos los `\qed % chktex 1` dentro de `\begin{proof}...\end{proof}`
2. **Revisar casos externos**: Evaluar `\qed` fuera de entornos `proof` y decidir si necesitan entorno `proof` o son excepciones legítimas
3. **Verificar formato**: Asegurar que todas las pruebas usan formato consistente

## Plan de Migración

Ver `docs/decisions/001-proof-environment-preference-DETECTION_REPORT.md` para detalles de detección y `docs/decisions/001-proof-environment-preference-MIGRATION_REPORT.md` para el reporte de migración.

## Casos Especiales

### Prueba que termina con ecuación display

El entorno `proof` maneja correctamente el caso donde la prueba termina con una ecuación display. El QED se coloca automáticamente después de la ecuación.

### Prueba larga con múltiples pasos

El entorno `proof` maneja correctamente pruebas largas con múltiples párrafos. El QED se coloca al final de todo el argumento.

### Excepciones

Si existe un caso legítimo donde se necesita `\qed` manual fuera de un entorno `proof`, debe documentarse como excepción en este documento.

## Verificación

- [x] Todos los `\qed` redundantes eliminados
- [x] Todos los entornos `proof` usan formato consistente
- [x] Documento compila sin errores
- [x] Formato visual verificado en PDF generado

