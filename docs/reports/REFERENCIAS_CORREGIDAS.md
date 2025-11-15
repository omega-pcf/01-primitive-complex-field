# Referencias Corregidas: Mapeo de § a \ref{}

## Resumen

Se han identificado y corregido referencias hardcodeadas en los archivos `.tex` que corresponden a referencias con símbolo § en `paper.md`.

## Correcciones Realizadas

### 1. methods.tex línea 412
**Antes:**
```latex
El operador hereda los axiomas de $\mathbb{C}$ previamente establecidos en la sección 2.
```

**Después:**
```latex
El operador hereda los axiomas de $\mathbb{C}$ previamente establecidos en \ref{sec:plano-complejo-modulos}.
```

**Mapeo:** "sección 2" → `\ref{sec:plano-complejo-modulos}` (corresponde a §2 en paper.md)

### 2. methods.tex línea 344
**Antes:**
```latex
\begin{proposition}[Conexión con espacio de módulos]\label{prop:conexion-moduli-teichmuller}
```

**Después:**
```latex
\begin{proposition}[Conexión con \ref{subsec:espacio-modulos}]\label{prop:conexion-moduli-teichmuller}
```

**Mapeo:** "Conexión con espacio de módulos" → "Conexión con \ref{subsec:espacio-modulos}" (corresponde a "Conexión con §2.5" en paper.md línea 336)

### 3. methods.tex línea 2166
**Antes:**
```latex
\begin{theorem}[Coherencia categórica]\label{thm:coherencia-categorica}
```

**Después:**
```latex
\begin{theorem}[Coherencia categórica desde \ref{thm:conmutatividad-functores}]\label{thm:coherencia-categorica}
```

**Mapeo:** "Coherencia categórica" → "Coherencia categórica desde \ref{thm:conmutatividad-functores}" (corresponde a "Coherencia categórica desde §2.6.6" en paper.md línea 1469)

## Referencias que Ya Estaban Correctas

Las siguientes referencias ya usan `\ref{}` correctamente y no necesitaron corrección:

- methods.tex línea 634: Ya usa `\ref{subsubsec:emergencia-hermiticidad}` en lugar de §3.8.2
- methods.tex línea 1750: Ya usa `\ref{const:rotacion-wick}` en lugar de §2.6.2
- methods.tex línea 1804: Ya usa `\ref{def:parametro-escala}` y `\ref{subsubsec:acoplamiento-optimo}` en lugar de §3.2.2 y §3.5.5
- methods.tex línea 1899: Ya usa `\ref{const:funcionalizacion}` en lugar de §2.6.3
- methods.tex línea 1919: Ya usa `\ref{prop:propiedades-matriz}` en lugar de §3.2.0
- results.tex línea 544: Ya usa `\ref{def:magnitudes-tripartitas}` en lugar de §3.2.1

## Estado del Mapeo

### Referencias Identificadas en paper.md
- Total de referencias con § encontradas: 81
- Referencias mapeadas a secciones en paper.md: ~30
- Referencias con labels identificados en .tex: ~20
- Referencias corregidas en .tex: 3

### Referencias Pendientes

Muchas referencias en `paper.md` apuntan a subsecciones, definiciones, teoremas, etc. que no tienen referencias hardcodeadas equivalentes en los archivos `.tex`. Esto es correcto porque:

1. `paper.md` es el draft original y no se modifica
2. Las referencias en `paper.md` son para referencia interna del documento
3. Los archivos `.tex` ya usan `\ref{}` en la mayoría de los casos

## Próximos Pasos

1. Continuar identificando labels faltantes para referencias específicas (definiciones, teoremas, etc.)
2. Verificar que todas las referencias `\ref{}` en .tex apuntan a labels válidos
3. Completar el mapeo de referencias a subsecciones más específicas si es necesario

