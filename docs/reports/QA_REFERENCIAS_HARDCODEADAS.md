# Reporte QA: Corrección de Referencias Hardcodeadas

**Fecha**: 2025-01-XX  
**Problema**: Referencias hardcodeadas a numeración `n.x.y` en lugar de usar `\ref{}` formales

## Problema Detectado

Se encontraron múltiples referencias hardcodeadas a numeración de secciones y construcciones matemáticas que no coincidían con la estructura real del documento o que se volverían incorrectas si la estructura cambiaba.

### Referencias Hardcodeadas Encontradas

#### En `src/chapters/methods.tex`:

1. **Línea 623**: 
   - Antes: `Teoremas 3.2.11, 3.2.12`
   - Después: `\tref{thm:acoplamiento-temporal} y \tref{thm:acoplamiento-optimo}`

2. **Línea 1552**: 
   - Antes: `Proposición 3.2.10`
   - Después: `\pref{prop:formula-fase-explicita}`

#### En `src/chapters/results.tex`:

3. **Línea 317**: 
   - Antes: `\S 3.8.2`
   - Después: `\ref{subsubsec:emergencia-hermiticidad}`

4. **Línea 327**: 
   - Antes: `(\S 3.8.2)`
   - Después: `(\ref{subsubsec:emergencia-hermiticidad})`

5. **Línea 362**: 
   - Antes: `(\S 3.5.2)`
   - Después: `(\ref{def:lattice-PCF})`

6. **Línea 544**: 
   - Antes: `(\S 3.2.1)`
   - Después: `(\ref{def:magnitudes-tripartitas})`

7. **Línea 588**: 
   - Antes: `(\S 3.3)`
   - Después: `(\ref{subsec:geometria-3d})`

## Causa del Problema

Las referencias hardcodeadas usaban numeración antigua o incorrecta que:
1. No reflejaba la estructura jerárquica real del documento
2. Se volverían incorrectas si la estructura cambiaba
3. No permitían verificación automática de referencias

### Ejemplo del Problema

La referencia `\S 3.8.2` sugiere una sección 3.8.2 que no existe. La estructura real es:
- Sección 2: El Operador PCF
  - Subsección 2.7: Funcionalización: Espacio de Hilbert
    - Subsubsección 2.7.2: Kernel PCF
    - Subsubsección 2.7.3: Construcción del Kernel
    - Subsubsección 2.7.4: Emergencia de Hermiticidad (label: `subsubsec:emergencia-hermiticidad`)

## Solución Aplicada

Todas las referencias hardcodeadas fueron reemplazadas por referencias formales usando `\ref{}` o macros de referencia (`\tref{}`, `\pref{}`, etc.) que:

1. **Se actualizan automáticamente** si la estructura cambia
2. **Permiten verificación** mediante compilación de LaTeX
3. **Son más mantenibles** y consistentes

## Verificación Post-Corrección

### Búsqueda Exhaustiva

Se realizó una búsqueda exhaustiva en todos los archivos de `src/chapters/` para detectar:
- Referencias con `\S` seguido de numeración
- Referencias con `§` seguido de numeración
- Referencias tipo "Teorema n.x.y", "Proposición n.x.y", etc.
- Numeración hardcodeada en títulos de secciones

### Resultados

✓ **No se encontraron más referencias hardcodeadas**  
✓ **Todas las referencias usan `\ref{}` formales**  
✓ **Compilación exitosa sin errores de referencias**  
✓ **No hay títulos con numeración hardcodeada**

## Mapeo de Referencias Corregidas

| Referencia Antigua | Referencia Nueva | Label |
|-------------------|-----------------|-------|
| `Teoremas 3.2.11, 3.2.12` | `\tref{thm:acoplamiento-temporal} y \tref{thm:acoplamiento-optimo}` | Teoremas de acoplamiento |
| `Proposición 3.2.10` | `\pref{prop:formula-fase-explicita}` | Fórmula de Fase Explícita |
| `\S 3.8.2` (2 ocurrencias) | `\ref{subsubsec:emergencia-hermiticidad}` | Emergencia de Hermiticidad |
| `\S 3.5.2` | `\ref{def:lattice-PCF}` | Lattice PCF |
| `\S 3.2.1` | `\ref{def:magnitudes-tripartitas}` | Magnitudes tripartitas |
| `\S 3.3` | `\ref{subsec:geometria-3d}` | Geometría del Círculo en Espacio 3D |

## Recomendaciones

1. **Usar siempre `\ref{}`**: Nunca hardcodear numeración de secciones o construcciones matemáticas
2. **Usar macros de referencia**: Los macros `\tref{}`, `\pref{}`, `\dref{}`, etc. facilitan referencias consistentes
3. **Verificación periódica**: Ejecutar búsquedas periódicas para detectar referencias hardcodeadas
4. **Compilación con verificación**: LaTeX reportará errores si una referencia `\ref{}` apunta a un label inexistente

## Referencias

- Archivos modificados: `src/chapters/methods.tex`, `src/chapters/results.tex`
- Total de referencias corregidas: 7
- Compilación verificada: ✓ Sin errores

