# Análisis de Títulos de Proofs

## Títulos Actuales Encontrados

### methods.tex
1. `[Por construcción]` - línea 554
2. `[Por cálculo directo]` - línea 616
3. `[Cálculo directo]` - línea 625 (sin "Por")
4. `[Por construcción]` - línea 643
5. `[Cálculo directo]` - línea 923 (sin "Por")
6. `[Por negación]` - línea 1016
7. `[Por construcción]` - línea 1065
8. `[Por construcción]` - línea 1101
9. `[Por construcción de aplicaciones inversas]` - línea 1235
10. `[Por construcción]` - línea 1372
11. `[Cálculo directo]` - línea 1633 (sin "Por")
12. `[Por sustitución]` - línea 1679
13. `[Por sustitución]` - línea 1810
14. `[Por verificación directa]` - línea 2010
15. `[Por cálculo directo del producto escalar]` - línea 2124
16. `[Por aplicación directa]` - línea 2166

### results.tex
1. `[Por descomposición espectral y análisis asintótico]` - línea 29
2. `[Por sustitución]` - línea 67
3. `[Por sustitución]` - línea 93
4. `[Por sustitución]` - línea 107
5. `[Por fórmula de autosimilitud]` - línea 134
6. `[Esquema de demostración]` - línea 257 (sin "Por")

## Problemas Identificados

### Inconsistencia en uso de "Por"
- Algunos tienen "Por": `[Por construcción]`, `[Por sustitución]`
- Otros no tienen "Por": `[Cálculo directo]`, `[Esquema de demostración]`
- No hay criterio claro de cuándo usar "Por" y cuándo no

### "Por" no tiene sentido en algunos casos
- `[Por construcción]` - ¿Por qué "Por"? Es simplemente "Construcción"
- `[Por sustitución]` - ¿Por qué "Por"? Es simplemente "Sustitución"
- `[Por cálculo directo]` - ¿Por qué "Por"? Es simplemente "Cálculo directo"

### Cambios innecesarios en el diff
Según el usuario, se están agregando "Por" en lugares donde no tiene sentido, siguiendo un patrón artificial.

## Propuesta de Estandarización CORREGIDA

### Principio: Si "Por" suena estándar, mantenerlo. Pero TODOS deben ser estándar.

**Regla:** Usar "Por" para métodos estándar en matemáticas. Estandarizar TODOS para consistencia:
- ✅ `[Por construcción]` - estándar, mantener
- ✅ `[Por sustitución]` - estándar, mantener
- ✅ `[Por contradicción]` - estándar, mantener
- ✅ `[Por inducción]` - estándar, mantener
- ✅ `[Por cálculo directo]` - estándar, mantener
- ❌ `[Cálculo directo]` → `[Por cálculo directo]` - agregar "Por" para consistencia

### Títulos Estandarizados Propuestos

#### methods.tex
1. `[Por construcción]` → ✅ mantener (estándar)
2. `[Por cálculo directo]` → ✅ mantener (estándar)
3. `[Cálculo directo]` → `[Por cálculo directo]` (línea 625 - agregar "Por" para consistencia)
4. `[Por construcción]` → ✅ mantener (estándar)
5. `[Cálculo directo]` → `[Por cálculo directo]` (línea 923 - agregar "Por" para consistencia)
6. `[Por negación]` → ✅ mantener o cambiar a `[Por contradicción]` si aplica
7. `[Por construcción]` → ✅ mantener (estándar)
8. `[Por construcción]` → ✅ mantener (estándar)
9. `[Por construcción de aplicaciones inversas]` → ✅ mantener (estándar)
10. `[Por construcción]` → ✅ mantener (estándar)
11. `[Cálculo directo]` → `[Por cálculo directo]` (línea 1633 - agregar "Por" para consistencia)
12. `[Por sustitución]` → ✅ mantener (estándar)
13. `[Por sustitución]` → ✅ mantener (estándar)
14. `[Por verificación directa]` → ✅ mantener (estándar)
15. `[Por cálculo directo del producto escalar]` → ✅ mantener (estándar)
16. `[Por aplicación directa]` → ✅ mantener (estándar)

#### results.tex
1. `[Por descomposición espectral y análisis asintótico]` → ✅ mantener (estándar)
2. `[Por sustitución]` → ✅ mantener (estándar)
3. `[Por sustitución]` → ✅ mantener (estándar)
4. `[Por sustitución]` → ✅ mantener (estándar)
5. `[Por fórmula de autosimilitud]` → ✅ mantener (estándar)
6. `[Esquema de demostración]` → ✅ mantener sin "Por" (caso especial, no es método)

## Criterio de Decisión CORREGIDO

**Usar "Por" para métodos estándar en matemáticas (MANTENER consistencia):**
- ✅ Métodos estándar: `[Por construcción]`, `[Por sustitución]`, `[Por contradicción]`, `[Por inducción]`
- ✅ Razones estándar: `[Por definición]`, `[Por hipótesis]`
- ✅ Técnicas estándar: `[Por cálculo directo]`, `[Por verificación directa]`, `[Por aplicación directa]`

**AGREGAR "Por" para consistencia:**
- ❌ `[Cálculo directo]` → `[Por cálculo directo]` (3 casos en methods.tex: líneas 625, 923, 1633)

**Excepciones (mantener sin "Por"):**
- ✅ `[Esquema de demostración]` - no es un método, es un esquema/estructura

