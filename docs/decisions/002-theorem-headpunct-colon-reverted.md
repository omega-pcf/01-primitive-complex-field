# Decisión Técnica 002: Reversión de Modificación de `\thm@headpunct` para Dos Puntos

**Fecha**: 2025-01-28  
**Estado**: Aprobada  
**Impacto**: Configuración de formato de teoremas en `main.tex`

## Decisión

**NO modificar `\thm@headpunct` para usar dos puntos (`:`) en lugar del punto (`.`) por defecto.** Mantener el formato predeterminado de `amsthm` que usa punto después del número del teorema.

## Contexto

Se intentó modificar el formato de los entornos de teoremas (`theorem`, `definition`, `proposition`, etc.) para que mostraran dos puntos (`:`) después del número en lugar del punto (`.`) por defecto. Por ejemplo:

- **Formato deseado**: "Definición 2.1.1:"
- **Formato actual (por defecto)**: "Definición 2.1.1."

## Intentos Realizados

Se realizaron múltiples intentos durante varios commits para lograr este cambio:

### Intento 1: `\renewcommand{\thm@headpunct}{:}`
```latex
\renewcommand{\thm@headpunct}{:}
```
**Resultado**: Error de compilación: `You can't use 'the character :' after \the.`

### Intento 2: `\renewcommand{\thm@headpunct}{\space:}`
```latex
\renewcommand{\thm@headpunct}{\space:}
```
**Resultado**: Error de compilación: `You can't use 'blank space ' after \the.`

### Intento 3: `\renewcommand{\thm@headpunct}{\@:}`
```latex
\renewcommand{\thm@headpunct}{\@:}
```
**Resultado**: Error de compilación: `You can't use '\spacefactor' in vertical mode.`

### Intento 4: Modificación de `\@thm` con `xpatch`
Se investigó usar `xpatch` o `etoolbox` para modificar la definición interna de `\@thm`, pero esto requeriría cambios más profundos y podría causar incompatibilidades con `hyperref`.

## Causa Técnica del Problema

El error ocurre porque `\thm@headpunct` es un token register (`\newtoks`) que se expande usando `\the\thm@headpunct` dentro de la definición de `\@thm` en `amsthm`. Cuando se inserta directamente después de `\thetheorem`, LaTeX no puede procesar el carácter `:` porque:

1. `\thm@headpunct` se inserta en el contexto: `\thetheorem\the\thm@headpunct`
2. LaTeX interpreta esto como `\thetheorem:` cuando `\thm@headpunct` contiene `:`
3. El carácter `:` no puede aparecer directamente después de `\the` en este contexto
4. Similarmente, `\space` y `\@` causan problemas en modo vertical o en el contexto de expansión de `\the`

## Justificación de la Reversión

### Razones Técnicas

1. **Incompatibilidad fundamental**: La forma en que `amsthm` usa `\thm@headpunct` no permite caracteres especiales como `:` directamente después de `\the`
2. **Solución requeriría cambios profundos**: Modificar esto correctamente requeriría redefinir `\@thm` completamente, lo cual:
   - Es frágil y propenso a romperse con actualizaciones de `amsthm`
   - Puede causar incompatibilidades con `hyperref` y otros paquetes
   - Añade complejidad innecesaria al código

### Razones de Diseño

1. **Convención estándar**: El punto (`.`) después del número del teorema es la convención estándar en matemáticas y LaTeX
2. **Legibilidad**: El punto funciona bien visualmente y es reconocido universalmente
3. **Mantenibilidad**: Usar el formato predeterminado reduce la complejidad y el riesgo de errores futuros

## Solución Aplicada

Se revirtieron todos los cambios relacionados con `\thm@headpunct`. La configuración actual en `main.tex` es:

```latex
\makeatletter
\@addtoreset{theorem}{subsection}
\makeatother
```

Sin ninguna modificación de `\thm@headpunct`, manteniendo el comportamiento predeterminado de `amsthm`.

## Referencias

- **Documentación consultada**: 
  - `docs/perplexity/PROMPT_LATEX_DEFINITION_LINEBREAK.md`
  - `docs/perplexity/PROMPT_LATEX_DEFINITION_LINEBREAK_REBUTTAL.md`
  - `docs/perplexity/PROMPT_LATEX_DEFINITION_LINEBREAK_REBUTTAL_response.md`
  - `docs/style/LINTER_PROBLEMS_ANALYSIS.md`

- **Búsquedas realizadas**: Múltiples consultas sobre `thm@headpunct`, `amsthm`, y soluciones para usar dos puntos en lugar de punto

## Impacto

### Archivos Afectados

- `main.tex`: Eliminada la modificación de `\thm@headpunct` y código relacionado

### Cambios Revertidos

- Eliminado: `\renewcommand{\thm@headpunct}{:}` (y variantes)
- Eliminado: Modificaciones de `\@begintheorem` relacionadas con el cambio de formato
- Mantenido: `\@addtoreset{theorem}{subsection}` (necesario para numeración correcta)

## Alternativas Consideradas

1. **Usar `thmtools`**: Se investigó pero añadiría una dependencia adicional sin garantía de resolver el problema
2. **Redefinir completamente `\@thm`**: Demasiado complejo y frágil
3. **Modificar `\thetheorem`**: No resuelve el problema porque el punto/dos puntos se agregan después

## Verificación

- [x] Documento compila sin errores
- [x] Todos los entornos de teoremas muestran formato correcto (con punto)
- [x] No hay errores de compilación relacionados con `\thm@headpunct`
- [x] La numeración jerárquica funciona correctamente

## Lecciones Aprendidas

1. **No todos los cambios de formato son triviales**: Aunque cambiar un carácter parece simple, la implementación interna de LaTeX puede hacerlo imposible sin cambios profundos
2. **Las convenciones estándar existen por razones**: El formato predeterminado de `amsthm` es robusto y ampliamente compatible
3. **Es importante reconocer cuándo detenerse**: Después de múltiples intentos fallidos, es mejor aceptar la limitación técnica que forzar una solución frágil

## Notas Adicionales

Si en el futuro se requiere absolutamente el formato con dos puntos, se recomienda:
1. Investigar si versiones futuras de `amsthm` o `thmtools` ofrecen esta funcionalidad
2. Considerar si el cambio visual justifica la complejidad técnica requerida
3. Evaluar alternativas de presentación que no requieran modificar comandos internos de LaTeX

