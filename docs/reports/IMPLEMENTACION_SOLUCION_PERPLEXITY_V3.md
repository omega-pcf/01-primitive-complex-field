# Implementación de Solución Perplexity V3: Basada en Análisis del Diff

## Fecha
2025-01-28

## Cambios Implementados

### 1. Removidos `\@addtoreset` Antes de `titlesec` en `lapreprint.cls`

**Ubicación**: Líneas 229-233 (removidas)

**Código removido**:
```latex
% Ensure proper counter hierarchy before titlesec modifies sections
\@addtoreset{subsection}{section}
\@addtoreset{subsubsection}{subsection}
```

**Razón**: Según Perplexity, estos `\@addtoreset` antes de cargar `titlesec` causan problemas de doble evaluación. Cuando `titlesec` evalúa los parámetros de título dos veces (medición + output), la lógica de reset de contadores se evalúa dos veces, causando offsets inconsistentes (+1, +2, +4, +5, +6, +10, +11, +12).

### 2. Removidas Definiciones de `\ttl@...label` en `lapreprint.cls`

**Ubicación**: Líneas 241-245 (removidas)

**Código removido**:
```latex
\def\ttl@sectionlabel{}
\def\ttl@subsectionlabel{}
\def\ttl@subsubsectionlabel{}
\def\ttl@paragraphlabel{}
\def\ttl@subparagraphlabel{}
```

**Razón**: Estas definiciones interfieren con el mecanismo interno de etiquetado de `titlesec`. Solo son necesarias cuando se usa `\titleclass`, que ya fue removido. La versión funcional nunca las tuvo.

### 3. Restaurado `\usepackage{titlesec}` en `main.tex`

**Ubicación**: Línea ~155 (restaurado)

**Código agregado**:
```latex
\usepackage{titlesec}
\titlespacing*{\section}{0pt}{2\baselineskip}{1\baselineskip}
\titlespacing*{\subsection}{0pt}{1.5\baselineskip}{0.75\baselineskip}
\titlespacing*{\subsubsection}{0pt}{1.25\baselineskip}{0.5\baselineskip}
```

**Razón**: La versión funcional tenía `titlesec` cargado en ambos lugares. Aunque LaTeX ignora cargas duplicadas de paquetes (solo la primera se ejecuta), tenerlo en `main.tex` permite usar `\titlespacing` sin problemas. Es seguro y no causa conflictos.

### 4. Mantenido `\@addtoreset{theorem}{subsection}` en `main.tex`

**Ubicación**: Línea 94 (mantenido)

**Código mantenido**:
```latex
\@addtoreset{theorem}{subsection}
```

**Razón**: Este `\@addtoreset` está en el preámbulo DESPUÉS de que todos los paquetes se han cargado, por lo que es seguro. `amsthm` con `[subsection]` debería manejar los resets automáticamente, pero este comando explícito no causa problemas aquí.

## Análisis de Perplexity

### Hallazgos Clave

1. **`secnumdepth` por defecto es 3**: La versión funcional funcionaba porque el valor por defecto de `secnumdepth` en `article`/`extarticle` es 3, no 2. La línea `\if@secnum\else\setcounter{secnumdepth}{0}\fi` no hacía nada cuando `secnum` estaba activo, dejando el valor por defecto.

2. **`\@addtoreset` antes de `titlesec` causa doble evaluación**: Cuando `titlesec` evalúa los parámetros de título dos veces (una para medir, otra para output), cualquier lógica de reset de contadores se evalúa dos veces, causando valores inconsistentes.

3. **Las definiciones `\ttl@...label` son innecesarias**: Solo son necesarias cuando se usa `\titleclass`, que ya fue removido. La versión funcional nunca las tuvo.

4. **Cargar `titlesec` dos veces es seguro**: LaTeX ignora cargas duplicadas de paquetes. La versión funcional lo hacía y funcionaba correctamente.

## Configuración Final

### `lapreprint.cls` (Líneas 222-235)

```latex
% Format title
\if@secnum
  \setcounter{secnumdepth}{3}% Explicitly enable subsubsection numbering (redundant but harmless - default is 3)
\else
  \setcounter{secnumdepth}{0}% Disable all numbering when secnum option is not used
\fi

\RequirePackage[explicit]{titlesec}

% CRITICAL: Do NOT add \@addtoreset, \titleclass, or \ttl@...label definitions here
% These interfere with titlesec's internal counter management and cause double-evaluation issues

\titleformat{\section}
  {\color{MediumGrey}\Large\bfseries}
  {\thesection}{10pt}{#1}[]
\titleformat{\subsection}
  {\large\bfseries}
  {\thesubsection}{10pt}{#1}[]
\titleformat{\subsubsection}
  {\large}
  {\thesubsubsection}{10pt}{#1}[]    
\titleformat{\paragraph}
  {\color{MediumGrey}\large}
  {\theparagraph}{10pt}{#1}[]
```

### `main.tex` (Líneas 70-157)

```latex
% Theorem environments (AMS standard for rigorous mathematics)
% Numeración jerárquica: n.x.y (sección.subsección.teorema)
\usepackage{amsthm}
\theoremstyle{plain}
\newtheorem{theorem}{Teorema}[subsection]
\newtheorem{proposition}[theorem]{Proposición}
\newtheorem{lemma}[theorem]{Lema}
\newtheorem{corollary}[theorem]{Corolario}
\newtheorem{conjecture}[theorem]{Conjetura}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definición}
\newtheorem{construction}[theorem]{Construcción}
\newtheorem{observation}[theorem]{Observación}
\newtheorem{example}[theorem]{Ejemplo}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Nota}

% Asegurar que el contador de teoremas se resetee correctamente al cambiar de subsección
% Esto es seguro aquí porque está en el preámbulo después de que todos los paquetes se han cargado
\makeatletter
\@addtoreset{theorem}{subsection}
\makeatother

% Espacio en títulos de sección
% Note: titlesec is already loaded in lapreprint.cls, but loading it again here is safe
\usepackage{titlesec}
\titlespacing*{\section}{0pt}{2\baselineskip}{1\baselineskip}
\titlespacing*{\subsection}{0pt}{1.5\baselineskip}{0.75\baselineskip}
\titlespacing*{\subsubsection}{0pt}{1.25\baselineskip}{0.5\baselineskip}
```

## Verificación

### Pasos de Verificación

1. ✅ Archivos auxiliares eliminados
2. ✅ Compilación del documento (3 veces)
3. ⏳ Ejecución del script de verificación
4. ⏳ Verificación de numeraciones específicas

### Resultados Esperados

- ✅ Documento compila sin errores
- ✅ Numeraciones correctas en todo el documento
- ✅ Script de verificación reporta 0 inconsistencias (o muy pocas)

## Referencias

- Respuesta de Perplexity: `docs/perplexity/PERPLEXITY_REBUTTAL_V3_ANALISIS_DIFF_response.md`
- Rebuttal original: `docs/perplexity/PERPLEXITY_REBUTTAL_V3_ANALISIS_DIFF.md`
- Documentación oficial de `titlesec`: https://texdoc.org/serve/titlesec/0
- LaTeX default `secnumdepth`: https://latexref.xyz/Sectioning.html

## Notas

- La solución está basada en volver a la configuración funcional con cambios mínimos
- Se removieron todos los elementos problemáticos identificados en el análisis del diff
- La configuración ahora es más simple y cercana a la versión funcional

