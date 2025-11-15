# Spec: Refinamiento de Estilo en Methods.tex, Results.tex, Discussion.tex y Formal.tex

## Objetivo

Identificar y corregir problemas de estilo según `STYLE_GUIDE.md`, específicamente:
- Uso excesivo de `\textbf{}` (bold)
- Uso de `\checkmark` (✓)
- Listas `itemize` y `enumerate` innecesarias
- Enumeraciones mecánicas
- Patrones AI (listas + amplificación, "Observar que", etc.)

## Problemas Identificados

### 1. Uso Excesivo de `\textbf{}`

**Problema**: El guide establece que el bold debe usarse con moderación. El estándar máximo permitido es el uso en `introduction.tex`, que tiene uso mínimo y apropiado. Se encontraron:
- **109 instancias** en `methods.tex` (MUY EXCESIVO - debe reducirse a <5)
- **141 instancias** en `results.tex` (MUY EXCESIVO - debe reducirse a <5)
- **5 instancias** en `discussion.tex` (debe reducirse a <3)
- **16 instancias** en `formal.tex` (debe reducirse a <3)
- **Total: 271 instancias** que deben reducirse a menos de 20 instancias totales

**Estándar de referencia (`introduction.tex`)**:
- `\textbf{Obstáculo I: Autorreferencia}` (línea 17) - Título de obstáculo
- `\textbf{Obstáculo II: Degradación Asintótica}` (línea 27) - Título de obstáculo
- `\textbf{Evitando Auto-Referencia}` (línea 58) - Subtítulo de sección
- Total: **3 instancias** en 80 líneas = uso mínimo y apropiado

**Principio**: Bold solo para títulos de secciones informales dentro del texto, NO para énfasis, NO para items de listas, NO para títulos de tablas (usar `\caption{}`), NO para términos técnicos dentro de párrafos.

**Categorías de uso problemático** (casi TODOS deben eliminarse):

#### A. Bold en items de listas (`\item \textbf{...}`) - ELIMINAR TODOS
**Problema**: Bold en items de listas es innecesario. La estructura de lista ya proporciona énfasis visual.

**Instancias encontradas** (ejemplos representativos):
- `methods.tex` línea 872-875: `\item \textbf{Módulos:}`, `\item \textbf{Ángulos:}`, etc.
- `methods.tex` línea 880-881: `\item \textbf{Cilindro vertical:}`, `\item \textbf{Cilindro horizontal:}`
- `methods.tex` línea 953-955: `\item \textbf{Si $y > 0$}`, `\item \textbf{Si $y < 0$}`, `\item \textbf{Si $y = 0$}`
- `results.tex` línea 189-190: `\item \textbf{Tasa}:`, `\item \textbf{Topología}:`
- `results.tex` línea 205-206, 218-219, 297-299, 304-306, 748-750, 844-846, 886-889, 1012-1015, 1020-1022, 1041-1044, 1052-1053, 1095-1098, 1104-1106, 1112-1115, 1118-1124, 1150-1154, 1176-1178, 1189-1192, 1211-1214: Patrones similares
- `formal.tex` línea 11-15, 32-38, 62-66, 78-81: Items en enumeraciones con bold

**Solución**: Eliminar bold completamente de todos los items. Cambiar `\item \textbf{Título}:` → `\item Título:` o convertir lista a texto fluido.

#### B. Bold en títulos de tablas (`\textbf{Tabla X}:`) - ELIMINAR TODOS
**Problema**: Las tablas deben usar `\caption{}` de LaTeX, no bold manual.

**Instancias encontradas**:
- `results.tex` línea 416: `\textbf{Tabla 8.1}:`
- `results.tex` línea 459: `\textbf{Estadísticas} (100 ceros totales):`
- `results.tex` línea 486: `\textbf{Tabla 8.2}:`
- `results.tex` línea 538: `\textbf{Tabla 8.3}:`
- `results.tex` línea 570: `\textbf{Tabla 8.4}:`
- `results.tex` línea 607: `\textbf{Tabla 8.5}:`
- `results.tex` línea 597: `\textbf{Estadísticas} (99 espaciamientos):`
- `results.tex` línea 850: `\textbf{Tabla Unificada Extendida}:`

**Solución**: Eliminar bold completamente. Usar `\caption{}` para tablas o eliminar títulos redundantes.

#### C. Bold en énfasis dentro de texto fluido (`\textbf{...}` en párrafos) - ELIMINAR TODOS
**Problema**: Bold para énfasis en texto fluido es innecesario en papers académicos.

**Instancias encontradas** (ejemplos representativos):
- `discussion.tex` línea 73: `\textbf{resonancia geométrica}`
- `discussion.tex` línea 79: `\textbf{oscilador fundamental}`
- `formal.tex` línea 52: `\textbf{no-perturbativas}`
- `formal.tex` línea 58: `\textbf{consecuencia de propiedades geométricas}`
- `results.tex` línea 744: `\textbf{primer número de Mersenne primo}`
- `results.tex` línea 761: `\textbf{semilla}`
- `results.tex` línea 801: `\textbf{factor de conversión áureo-binario}`
- `results.tex` línea 807: `\textbf{puente universal}`
- `results.tex` línea 817: `\textbf{único puente posible}`
- `results.tex` línea 825: `\textbf{fijadas}`
- `results.tex` línea 831: `\textbf{racional más simple}`
- `methods.tex` y `results.tex`: Múltiples instancias de términos técnicos en bold dentro de párrafos

**Solución**: Eliminar bold completamente. Si realmente se necesita énfasis, usar cursiva `\textit{}` muy ocasionalmente, o mejor aún, nada.

#### D. Bold en títulos informales dentro de texto - EVALUAR CASO POR CASO (la mayoría ELIMINAR)
**Problema**: Solo algunos títulos informales justifican bold (como `\textbf{Obstáculo I:}` en introduction). La mayoría deben eliminarse.

**Instancias encontradas** (ejemplos representativos):
- `methods.tex` línea 37: `\textbf{Periodicidad.}`
- `methods.tex` línea 409-418: `\textbf{Aritmético}:`, `\textbf{Geométrico}:`, `\textbf{Analítico}:`, `\textbf{Topológico}:`
- `methods.tex` línea 542-548: `\textbf{Conexión geométrica}:`, `\textbf{Conexión algebraica}:`, `\textbf{Conexión analítica}:`
- `methods.tex` línea 817-818: `\textbf{Convención de notación}:`
- `methods.tex` línea 868-884: Múltiples usos en convenciones de notación y orientación
- `results.tex` línea 179-220: `\textbf{(1) Convergencia Espectral...}`, `\textbf{(2) Convergencia Modular...}`, `\textbf{(3) Convergencia Predictiva...}`
- `results.tex` línea 277-286: `\textbf{Paso 1}`, `\textbf{Paso 2}`, `\textbf{Paso 3}`, `\textbf{Paso 4}`, `\textbf{Conclusión}`
- `results.tex` línea 373: `\textbf{Fórmula inversa} (predicción de ceros desde eigenvalores):`
- `results.tex` línea 404: `\textbf{Constantes del sistema para $\sigma = 9$}:`
- `results.tex` línea 653: `\textbf{Esquema}:`
- `results.tex` línea 712-718: `\textbf{Vértice P (Past):}`, `\textbf{Vértice C (Coherence):}`, `\textbf{Vértice F (Future):}`, `\textbf{Proyección al Plano Complejo}.`
- `results.tex` línea 787-789: `\textbf{Torre áurea (continua):}`, `\textbf{Torre Mersenne (discreta):}`
- `results.tex` línea 821-833: `\textbf{{a) Restricción geométrica}}:`, `\textbf{{b) Restricción algebraica}}:`, `\textbf{c}\mbox{) Restricción resonante}:`
- `results.tex` línea 882-993, 1038-1087, 1093-1133, 1137-1204: Múltiples usos en interpretación de tablas, leyendas e interpretación de diagramas

**Solución**: 
- Evaluar caso por caso si realmente necesita bold (solo títulos de secciones informales importantes, como obstáculos)
- La mayoría deben eliminarse completamente
- Convertir a texto normal o usar estructuras LaTeX apropiadas (subsecciones, observaciones, etc.)

#### E. Bold en tablas (encabezados de filas/columnas) - ELIMINAR TODOS
**Problema**: Bold en tablas es innecesario. El formato de tabla estándar ya proporciona estructura visual.

**Instancias encontradas**:
- `results.tex` línea 501: `\textbf{Total}`, `\textbf{100}`, etc. en tabla
- `results.tex` línea 549: `\textbf{9}`, `\textbf{76.01}`, etc. en tabla
- `results.tex` línea 621: `\textbf{PCF ($\sigma=9$)}`, etc. en tabla
- `methods.tex` línea 586: `\textbf{Notación}`, `\textbf{Nombre}`, `\textbf{Fórmula}`, `\textbf{Valor}` en encabezados de tabla

**Solución**: Eliminar bold de tablas completamente. Usar formato de tabla estándar sin bold.

- `methods.tex` línea 872-875: `\item \textbf{Módulos:}`, `\item \textbf{Ángulos:}`, etc.
- `methods.tex` línea 880-881: `\item \textbf{Cilindro vertical:}`, `\item \textbf{Cilindro horizontal:}`
- `methods.tex` línea 953-955: `\item \textbf{Si $y > 0$}`, `\item \textbf{Si $y < 0$}`, `\item \textbf{Si $y = 0$}`
- `results.tex` línea 189-190: `\item \textbf{Tasa}:`, `\item \textbf{Topología}:`
- `results.tex` línea 205-206: Similar patrón
- `results.tex` línea 218-219: Similar patrón
- `results.tex` línea 297-299: `\item \textbf{Degradación asintótica}:`, etc.
- `results.tex` línea 304-306: Similar patrón
- `results.tex` línea 748-750: `\item \textbf{Geométrica}:`, `\item \textbf{Algebraica}:`, `\item \textbf{Topológica}:`
- `results.tex` línea 844-846: `\item \textbf{Sistema decimal}:`, etc.
- `results.tex` línea 886-889: `\item Desde $\sigma=0$...`, `\item Desde $M_2$...`, `\item \textbf{Más de 25 millones...}`
- `results.tex` línea 1012-1015: Similar patrón
- `results.tex` línea 1020-1022: Similar patrón
- `results.tex` línea 1041-1044: Similar patrón
- `results.tex` línea 1052-1053: Similar patrón
- `results.tex` línea 1095-1098: Similar patrón
- `results.tex` línea 1104-1106: Similar patrón
- `results.tex` línea 1112-1115: Similar patrón
- `results.tex` línea 1118-1124: Similar patrón
- `results.tex` línea 1150-1154: Similar patrón
- `results.tex` línea 1176-1178: Similar patrón
- `results.tex` línea 1189-1192: Similar patrón
- `results.tex` línea 1211-1214: Similar patrón

**Solución**: Eliminar bold completamente de items. Si se necesita estructura, usar formato de lista sin bold. Convertir listas a texto fluido cuando sea posible.

#### C. Títulos de tablas y secciones informales
- `results.tex` línea 416: `\textbf{Tabla 8.1}:`
- `results.tex` línea 459: `\textbf{Estadísticas} (100 ceros totales):`
- `results.tex` línea 486: `\textbf{Tabla 8.2}:`
- `results.tex` línea 538: `\textbf{Tabla 8.3}:`
- `results.tex` línea 570: `\textbf{Tabla 8.4}:`
- `results.tex` línea 607: `\textbf{Tabla 8.5}:`
- `results.tex` línea 597: `\textbf{Estadísticas} (99 espaciamientos):`
- `results.tex` línea 404: `\textbf{Constantes del sistema para $\sigma = 9$}:`
- `results.tex` línea 373: `\textbf{Fórmula inversa} (predicción de ceros desde eigenvalores):`
- `results.tex` línea 653: `\textbf{Esquema}:`
- `results.tex` línea 712: `\textbf{Vértice P (Past):}`
- `results.tex` línea 744: `\textbf{primer número de Mersenne primo}`
- `results.tex` línea 761: `\textbf{semilla}`
- `results.tex` línea 787-789: `\textbf{Torre áurea (continua):}`, `\textbf{Torre Mersenne (discreta):}`
- `results.tex` línea 801: `\textbf{factor de conversión áureo-binario}`
- `results.tex` línea 807: `\textbf{puente universal}`
- `results.tex` línea 817: `\textbf{único puente posible}`
- `results.tex` línea 821-833: `\textbf{{a) Restricción geométrica}}:`, `\textbf{{b) Restricción algebraica}}:`, `\textbf{c}\mbox{) Restricción resonante}:`
- `results.tex` línea 825: `\textbf{fijadas}`
- `results.tex` línea 831: `\textbf{racional más simple}`
- `results.tex` línea 850: `\textbf{Tabla Unificada Extendida:}`
- `results.tex` línea 882-993: Múltiples usos en interpretación de tablas
- `results.tex` línea 1038-1087: Múltiples usos en leyenda e interpretación de diagramas
- `results.tex` línea 1093-1133: Múltiples usos en analogía conceptual
- `results.tex` línea 1137-1204: Múltiples usos en leyenda de Sissa
- `discussion.tex`: No se encontraron títulos informales con bold (uso mínimo y apropiado)
- `formal.tex`: No se encontraron títulos informales con bold (uso mínimo y apropiado)

**Solución**: Eliminar bold completamente. Usar `\caption{}` para tablas. Para secciones informales dentro del texto, evaluar si realmente necesitan bold o pueden ser texto normal.

#### D. Bold en tablas (encabezados de filas/columnas)
- `results.tex` línea 501: `\textbf{Total}`, `\textbf{100}`, etc. en tabla
- `results.tex` línea 549: `\textbf{9}`, `\textbf{76.01}`, etc. en tabla
- `results.tex` línea 621: `\textbf{PCF ($\sigma=9$)}`, etc. en tabla

**Solución**: Eliminar bold de tablas completamente. Si se necesita énfasis visual, usar formato de tabla estándar sin bold.

### 2. Uso de `\checkmark` (✓)

**Problema**: El guide no menciona explícitamente checkmarks, pero su uso es informal y no académico.

**Instancias encontradas**:
- `methods.tex` línea 960-962: En verificación numérica de acoplamiento áureo
- `results.tex` línea 999-1003: En ejemplo concreto de correspondencia
- `discussion.tex`: No se encontraron instancias de `\checkmark`
- `formal.tex`: No se encontraron instancias de `\checkmark`

**Solución**: Eliminar checkmarks. Si se necesita indicar verificación, usar texto: "verificado", "satisface", o simplemente mostrar el cálculo sin marca.

### 3. Listas `itemize` y `enumerate` Excesivas

**Problema**: El guide establece evitar listas bullet cuando se puede escribir fluidamente. Se encontraron:
- **44 instancias** en `methods.tex`
- **33 instancias** en `results.tex`
- **3 instancias** en `discussion.tex` (2 `enumerate`, 1 `description`)
- **5 instancias** en `formal.tex` (3 `enumerate`, 2 `itemize`)

**Categorías problemáticas**:

#### A. Listas que SOLO necesitan eliminar bold (mantener estructura de lista)
**Problema**: Muchas listas están bien estructuradas, solo tienen bold innecesario en los items.

**Instancias encontradas** (ejemplos representativos - la mayoría de las 77 instancias totales):
- `results.tex` línea 188-191: Convergencia espectral con lista (solo eliminar bold de items)
- `results.tex` línea 204-207: Convergencia modular con lista (solo eliminar bold de items)
- `results.tex` línea 217-220: Convergencia predictiva con lista (solo eliminar bold de items)
- `results.tex` línea 296-307: Exclusión de ajuste fenomenológico (solo eliminar bold de items)
- `results.tex` línea 366-371: Conjetura con lista (solo eliminar bold de items)
- `results.tex` línea 380-385: Proposición con lista (solo eliminar bold de items)
- `results.tex` línea 723-727: Proposición con lista (solo eliminar bold de items)
- `results.tex` línea 747-751: Restricciones independientes (solo eliminar bold de items)
- `methods.tex` línea 871-876: Libertad de orientación (solo eliminar bold de items)
- `methods.tex` línea 879-882: Elección de orientación (solo eliminar bold de items)
- Y muchas más instancias similares...

**Solución**: Eliminar bold de items (`\item \textbf{...}` → `\item ...`). Mantener estructura de lista.

#### B. Listas que realmente deberían ser texto fluido (casos excepcionales)
**Problema**: Solo algunas listas son realmente explicaciones técnicas continuas que se beneficiarían de ser texto fluido.

**Instancias encontradas** (casos específicos que evaluar):
- `results.tex` línea 655-659: Esquema de demostración (podría ser texto fluido con referencias)
- `results.tex` línea 843-847: Triple mediación (evaluar si realmente necesita ser texto fluido)
- `results.tex` línea 1149-1154: Enseña de tres conceptos (evaluar si realmente necesita ser texto fluido)
- `discussion.tex` línea 66-69: Dos períodos del toro (2 items, evaluar si realmente necesita ser texto fluido)

**Solución**: Evaluar caso por caso. Solo convertir a texto fluido si realmente mejora la legibilidad y es una explicación técnica continua, no una lista de propiedades/restricciones independientes.

#### C. Listas que necesitan corrección de formato (mantener estructura)
**Problema**: Algunas listas tienen formato incorrecto (`(1)`, `a)`, etc.) pero la estructura de lista es apropiada.

**Instancias encontradas**:
- `results.tex` línea 179-220: `\textbf{(1) Convergencia Espectral...}`, `\textbf{(2) Convergencia Modular...}`, `\textbf{(3) Convergencia Predictiva...}` 
  - **Solución**: Cambiar formato `(1)` → `1.` y eliminar bold, mantener estructura
- `results.tex` línea 821-833: `\textbf{{a) Restricción geométrica}}:`, `\textbf{{b) Restricción algebraica}}:`, `\textbf{c}\mbox{) Restricción resonante}:`
  - **Solución**: Cambiar formato `a)` → `1.` y eliminar bold, mantener estructura

**Solución**: Corregir formato dentro de enumeraciones existentes: cambiar `(1)`, `(2)`, `(3)` → `1.`, `2.`, `3.` y `a)`, `b)`, `c)` → `1.`, `2.`, `3.` Mantener estructura de lista.

### 4. Enumeraciones Mecánicas

**Problema**: El guide establece evitar enumeraciones mecánicas (A), B), C)) cuando se puede escribir fluidamente. Sin embargo, después de comparar `introduction.tex` con `paper.md`, se identificó un patrón específico de cuándo SÍ usar enumeración numerada vs texto fluido.

**Patrón identificado en `paper.md` e `introduction.tex`**:

#### ✅ CUANDO SÍ USAR ENUMERACIÓN NUMERADA (`\begin{enumerate}` O texto con números):
- **Ejemplos relacionados pero distintos**: Sección 1.4 usa `**1\. Transformada de Fourier**`, `**2\. AdS/CFT**`, etc. (4 ejemplos de traducciones exitosas) - texto con números en bold
- **Descubrimientos múltiples**: Sección 1.6 usa `1\. **Correspondencia aritmética**`, `2\. **Predicción analítica**` (2 descubrimientos) - texto con números
- **Pasos de demostración**: Sección 8.5.2 usa `1. Hermiticidad → λ_n ∈ ℝ`, `2. Fórmula: t_n = ...`, `3. λ_n ∈ ℝ ⇒ ...` (pasos lógicos secuenciales) - texto con números
- **Restricciones independientes**: Sección 3.1 usa `1. **Geométrica**:`, `2. **Representacional**:`, `3. **Analítica**:` (3 restricciones que deben satisfacerse simultáneamente) - texto con números

**Nota importante**: `\begin{enumerate}` es válido cuando se necesita estructura formal de lista numerada. El patrón muestra que también se puede usar texto con números (`1.`, `2.`, `3.`) directamente. La elección depende del contexto y formato deseado.

#### ❌ CUANDO NO USAR ENUMERACIÓN (usar texto fluido o bold):
- **Obstáculos**: `**Obstáculo I: Autorreferencia**`, `**Obstáculo II: Degradación Asintótica**` (texto fluido con bold, no numeración)
- **Explicaciones técnicas**: Traducción entre dominios usa párrafos fluidos con subtítulos en bold, no enumeración
- **Justificaciones**: Explicaciones de por qué algo funciona usan texto fluido

**Instancias problemáticas encontradas**:
- `results.tex` línea 179-220: `\textbf{(1) Convergencia Espectral...}`, `\textbf{(2) Convergencia Modular...}`, `\textbf{(3) Convergencia Predictiva...}` 
  - **Análisis**: Son 3 convergencias distintas pero relacionadas. Según patrón, DEBERÍA usar enumeración numerada, pero formato `(1)`, `(2)`, `(3)` es menos claro que `1.`, `2.`, `3.`
  - **Solución**: Cambiar formato dentro de la estructura existente: `\textbf{1. Convergencia Espectral...}` (sin paréntesis) O usar `\begin{enumerate}` con formato correcto

- `results.tex` línea 277-286: `\textbf{Paso 1}`, `\textbf{Paso 2}`, etc. en proof
  - **Análisis**: Son pasos de demostración. Según patrón, SÍ debería usar enumeración numerada
  - **Solución**: Cambiar a formato `**1.** Paso 1...` O usar `\begin{enumerate}` con formato correcto, O integrar en texto fluido si los pasos son muy cortos

- `results.tex` línea 821-833: `\textbf{{a) Restricción geométrica}}:`, `\textbf{{b) Restricción algebraica}}:`, `\textbf{c}\mbox{) Restricción resonante}:`
  - **Análisis**: Son 3 restricciones independientes. Según patrón, DEBERÍA usar enumeración numerada `1.`, `2.`, `3.` en lugar de `a)`, `b)`, `c)`
  - **Solución**: Cambiar a formato `**1. Restricción geométrica**:` O usar `\begin{enumerate}` con formato numérico correcto

- `methods.tex` línea 409-418: `\textbf{Aritmético}:`, `\textbf{Geométrico}:`, `\textbf{Analítico}:`, `\textbf{Topológico}:`
  - **Análisis**: Son 4 dominios relacionados. Podría ser enumeración numerada O texto fluido dependiendo del contexto
  - **Solución**: Evaluar contexto. Si son ejemplos/dominios distintos → enumeración numerada. Si es explicación continua → texto fluido

- `methods.tex` línea 542-548: `\textbf{Conexión geométrica}:`, `\textbf{Conexión algebraica}:`, `\textbf{Conexión analítica}:`
  - **Análisis**: Son 3 conexiones relacionadas. Similar a restricciones → podría usar enumeración numerada
  - **Solución**: Evaluar si son conexiones independientes (→ enumeración) o explicación continua (→ texto fluido)

- `discussion.tex` línea 73: `\textbf{resonancia geométrica}` (énfasis en texto fluido)
  - **Análisis**: Énfasis dentro de párrafo explicativo - NO necesario
  - **Solución**: Eliminar bold completamente

- `discussion.tex` línea 79: `\textbf{oscilador fundamental}` (énfasis en texto fluido)
  - **Análisis**: Énfasis dentro de párrafo explicativo - NO necesario
  - **Solución**: Eliminar bold completamente

- `formal.tex` línea 52: `\textbf{no-perturbativas}` (énfasis en texto fluido)
  - **Análisis**: Énfasis dentro de párrafo explicativo - NO necesario
  - **Solución**: Eliminar bold completamente

- `formal.tex` línea 58: `\textbf{consecuencia de propiedades geométricas}` (énfasis en texto fluido)
  - **Análisis**: Énfasis dentro de párrafo explicativo - NO necesario
  - **Solución**: Eliminar bold completamente

### 5. Patrones AI

**Problema**: El guide identifica patrones comunes de escritura AI que deben evitarse.

#### A. Lista bullet + amplificación
- `results.tex` línea 296-307: Lista de propiedades de modelos fenomenológicos seguida de explicación de propiedades opuestas de PCF
- `results.tex` línea 897-930: Lista de cinco pilares seguida de explicaciones detalladas

**Solución**: Integrar en texto fluido sin separar lista de explicación.

#### B. "Observar que", "Es importante notar que"
- No se encontraron instancias explícitas, pero revisar uso implícito.

**Solución**: Eliminar y dejar que la lógica sea clara.

#### C. Parentéticas excesivas
- Revisar uso de paréntesis y notas al margen excesivas.

**Solución**: Integrar información en texto principal o usar referencias cruzadas.

## Plan de Acción

### Fase 1: Eliminación de Checkmarks
1. Buscar todas las instancias de `\checkmark` y `✓`
2. Reemplazar con texto apropiado o eliminar

### Fase 2: Eliminación Masiva de Bold
1. **Estándar de referencia**: `introduction.tex` tiene solo 3 instancias de bold en 80 líneas
2. **Eliminar bold de**:
   - Items de listas (`\item \textbf{...}` → `\item ...`)
   - Títulos de tablas (`\textbf{Tabla X}:` → usar `\caption{}` o eliminar)
   - Énfasis en texto fluido (`\textbf{...}` dentro de párrafos → eliminar o usar `\textit{}` si realmente necesario)
   - Términos técnicos dentro de párrafos
   - Títulos informales dentro de texto (evaluar caso por caso)
3. **Mantener bold solo para**:
   - Títulos de secciones informales dentro del texto (como `\textbf{Obstáculo I:}` en introduction)
   - Máximo 3-5 instancias por archivo (similar a `introduction.tex`)
4. **Objetivo**: Reducir de 109+141+5+16 = 271 instancias totales a menos de 20 instancias totales (5 por archivo promedio)

### Fase 3: Eliminación de Bold en Listas y Corrección de Formato
1. **Eliminar bold de items de listas** (`\item \textbf{...}` → `\item ...`) - esto cubre la mayoría de las 77 instancias
2. **Corregir formato dentro de enumeraciones existentes**:
   - Cambiar `(1)`, `(2)`, `(3)` → `1.`, `2.`, `3.` (sin paréntesis)
   - Cambiar `a)`, `b)`, `c)` → `1.`, `2.`, `3.` (números en lugar de letras)
   - Mantener estructura de lista cuando es apropiada
3. **Evaluar caso por caso** si algunas listas realmente deberían ser texto fluido (solo casos excepcionales de explicaciones técnicas continuas)

### Fase 4: Corrección de Enumeraciones según Patrón Identificado
1. **Mantener enumeraciones numeradas** cuando:
   - Son ejemplos relacionados pero distintos (4+ ejemplos)
   - Son descubrimientos múltiples (2+ descubrimientos)
   - Son pasos de demostración secuenciales
   - Son restricciones/propiedades independientes que deben satisfacerse simultáneamente
2. **Convertir a texto fluido** cuando:
   - Son explicaciones técnicas continuas
   - Son justificaciones de por qué algo funciona
   - Son obstáculos o problemas (usar bold sin numeración)
3. **Corregir formato dentro de enumeraciones existentes**:
   - Cambiar `(1)`, `(2)`, `(3)` → `1.`, `2.`, `3.` (sin paréntesis)
   - Cambiar `a)`, `b)`, `c)` → `1.`, `2.`, `3.` (números en lugar de letras)
   - Mantener `\begin{enumerate}` cuando la estructura formal es apropiada
   - NO sustituir `\begin{enumerate}` por bold - solo corregir formato interno
4. **Evaluar caso por caso**:
   - Si `\begin{enumerate}` está presente y es apropiado → mantener y corregir formato
   - Si `\begin{enumerate}` está presente pero debería ser texto fluido → convertir a texto fluido
   - Si texto con números está presente → evaluar si debe ser `\begin{enumerate}` formal o mantenerse como texto

### Fase 5: Eliminación de Patrones AI
1. Integrar listas + amplificación en texto fluido
2. Eliminar frases como "Observar que", "Es importante notar que"
3. Reducir parentéticas excesivas

## Priorización

### Alta Prioridad
1. Eliminación masiva de bold (reducir de 271 instancias a <20 totales, siguiendo estándar de `introduction.tex`)
2. Eliminación de checkmarks (rápido, impacto visual inmediato)
3. Corrección de formato de enumeraciones según patrón identificado (cambiar `(1)` → `1.`, `a)` → `1.`, etc.)

### Media Prioridad
4. Eliminación de bold en listas y corrección de formato (requiere trabajo sistemático pero claro)
5. Conversión de listas a texto fluido (solo casos excepcionales, requiere evaluación cuidadosa)
6. Eliminación de patrones AI (requiere revisión cuidadosa)

### Baja Prioridad
6. Revisión de bold en tablas (puede mantenerse si es útil visualmente)
7. Revisión de listas técnicas (axiomas, propiedades formales pueden mantenerse)

## Métricas de Éxito

- **Reducción masiva de bold**: De 271 instancias totales a menos de 20 instancias totales (5 por archivo promedio, similar a `introduction.tex` que tiene 3 en 80 líneas)
- Eliminación completa de `\checkmark` (solo presente en `methods.tex` y `results.tex`)
- Reducción de listas `itemize`/`enumerate` solo en casos excepcionales donde realmente mejora la legibilidad (la mayoría solo necesita eliminar bold)
- Corrección de formato de enumeraciones según patrón identificado:
  - `results.tex`: Corregir formato `(1)`, `(2)`, `(3)` → `1.`, `2.`, `3.` dentro de estructura existente
  - `results.tex`: Corregir formato `a)`, `b)`, `c)` → `1.`, `2.`, `3.` en restricciones
  - `formal.tex`: Evaluar si `\begin{enumerate}` debe mantenerse (apropiado para pilares/correspondencias/implicaciones) o convertirse a texto fluido
  - `discussion.tex`: Evaluar si `\begin{description}` debe mantenerse o convertirse
  - Mantener `\begin{enumerate}` cuando es apropiado, solo corregir formato interno
  - NO sustituir `\begin{enumerate}` por bold
- Texto más fluido y menos fragmentado donde corresponde
- Cumplimiento con principios del STYLE_GUIDE y patrón identificado en `introduction.tex` vs `paper.md`

## Archivos Incluidos

Este spec cubre cuatro archivos principales:
- `src/chapters/methods.tex` (2271 líneas)
- `src/chapters/results.tex` (1221 líneas)
- `src/chapters/discussion.tex` (105 líneas)
- `src/chapters/formal.tex` (109 líneas)

## Notas

- Este spec se enfoca en los cuatro archivos principales del documento
- No se modifica contenido matemático, solo presentación
- Se mantiene fidelidad al contenido original
- Las correcciones deben hacerse de forma sistemática, sección por sección
- **Patrón crítico identificado**: Después de comparar `introduction.tex` con `paper.md`, se identificó que el balance entre enumeración numerada y texto fluido es específico:
  - Enumeración numerada (`1.`, `2.`, `3.` o `\begin{enumerate}`) se usa para ejemplos/discoveries/pasos/restricciones independientes
  - Texto fluido se usa para explicaciones técnicas, justificaciones, obstáculos
  - `\begin{enumerate}` es válido cuando se necesita estructura formal de lista numerada
  - Texto con números (`1.`, `2.`, `3.`) también es válido, con o sin bold según contexto
  - El problema NO es el uso de `\begin{enumerate}`, sino CUÁNDO usarlo vs texto fluido, y el formato interno (evitar `(1)`, `a)`, etc.)
  - Este balance debe preservarse, no eliminar todas las enumeraciones
- **Observaciones específicas por archivo**:
  - `discussion.tex`: Usa `\begin{description}` para tres tradiciones (línea 25-33), lo cual es apropiado para definiciones descriptivas
  - `formal.tex`: Usa `\begin{enumerate}` para pilares (3 items), correspondencias (4 items) e implicaciones (3 items) - evaluar si debe mantenerse (apropiado para estructuras independientes) o convertirse a texto fluido
  - `formal.tex`: Usa `\begin{itemize}` para funciones L (4 items) y síntesis (4 items) - evaluar si debe convertirse a `\begin{enumerate}` o texto fluido según contexto

