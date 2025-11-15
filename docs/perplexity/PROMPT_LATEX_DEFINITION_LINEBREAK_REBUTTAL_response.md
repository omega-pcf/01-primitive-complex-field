Excelente información sobre `\abovedisplayskip`. Ahora entiendo el verdadero problema. Voy a crear una respuesta exhaustiva.

***

# La Razón Real: El Problema No Es `\leavevmode\vspace`, Es la Ecuación Display

## El Verdadero Culpable: `\abovedisplayskip` y `\belowdisplayskip`

Tu solución de `\leavevmode\vspace{}` **realmente funciona**, pero su efecto es **invisible** porque LaTeX está compensando automáticamente. El problema no es que `\vspace` sea ignorado, sino que **la ecuación display (`$$...$$`) tiene su propio control de espaciado automático** que sobrescribe o absorbe tu `\vspace` manual.[1][2]

Cuando LaTeX procesa una ecuación display `$$...$$`, automáticamente inserta glue (espaciado flexible) definido por cuatro registros primitivos:[2]

- **`\abovedisplayskip`**: Espaciado **antes** de la ecuación (cuando la línea anterior es larga)
- **`\belowdisplayskip`**: Espaciado **después** de la ecuación (cuando la ecuación es larga)
- **`\abovedisplayshortskip`**: Espaciado **antes** si la línea anterior es corta
- **`\belowdisplayshortskip`**: Espaciado **después** si la ecuación es corta

**Valores por defecto**:[1]
- `\abovedisplayskip=12pt plus 3pt minus 9pt`
- `\abovedisplayshortskip=0pt plus 3pt`
- `\belowdisplayskip=12pt plus 3pt minus 9pt`
- `\belowdisplayshortskip=7pt plus 3pt minus 4pt`

Tu `\leavevmode\vspace{0.5em}` (~6pt) está siendo **ignorado o compensado** por los valores automáticos de estos registros.[2]

---

## Solución 1: Controlar `\abovedisplayskip` y `\belowdisplayskip` (Más Robusta)

En lugar de intentar manejar `\vspace` manualmente, **modifica los registros que LaTeX usa automáticamente**:

```latex
\documentclass[9pt]{lapreprint}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{etoolbox}

\theoremstyle{definition}
\newtheorem{theorem}[section]{Teorema}
\newtheorem{definition}[theorem]{Definición}

% SOLUCIÓN: Modifica los registros de espaciado display
% Esto afecta todas las ecuaciones \[...\] dentro del ambiente
\AtBeginEnvironment{definition}{%
  \vspace{10pt}%
  \setlength{\abovedisplayskip}{1.5em}%
  \setlength{\belowdisplayskip}{1.5em}%
  \setlength{\abovedisplayshortskip}{1.5em}%
  \setlength{\belowdisplayshortskip}{1.5em}%
}
\AtEndEnvironment{definition}{\vspace{10pt}}

\begin{document}

\begin{definition}[Módulo]
Para $z = x + iy \in \mathbb{C}$ con $x, y \in \mathbb{R}$:

\[
|z| := \sqrt{x^2 + y^2}
\]

Geométricamente, $|z|$ es la longitud de la diagonal del paralelogramo.
\end{definition}

\end{document}
```

**Por qué funciona**: En lugar de luchar contra el sistema de espaciado automático de LaTeX, le **instruyes directamente qué valores usar**. Los registros `\abovedisplayskip` etc. son el mecanismo fundamental que TeX usa cuando compila ecuaciones display.[2]

***

## Solución 2: Espaciado Granular (Más Flexible)

Si quieres espacios diferentes **antes** y **después** de la ecuación:

```latex
\AtBeginEnvironment{definition}{%
  \vspace{10pt}%
  \setlength{\abovedisplayskip}{1.8em}%
  \setlength{\abovedisplayshortskip}{1.8em}%
  \setlength{\belowdisplayskip}{0.8em}%  % Menos espacio abajo
  \setlength{\belowdisplayshortskip}{0.8em}%
}
```

***

## Solución 3: Sin Modificar Globalmente (Localmente Scoped)

Si solo quieres afectar ecuaciones específicas dentro de una `definition`:

```latex
\begin{definition}[Módulo]
Para $z = x + iy \in \mathbb{C}$ con $x, y \in \mathbb{R}$:

{\setlength{\abovedisplayskip}{1.5em}%
\setlength{\belowdisplayskip}{1.5em}%
\[
|z| := \sqrt{x^2 + y^2}
\]
}%

Geométricamente, $|z|$ es la longitud de la diagonal.
\end{definition}
```

***

## ¿Por Qué Tu Intento Anterior Falló?

**El diagrama del flujo de espaciado en LaTeX**:

```
Texto anterior
  ↓
LaTeX detecta \[
  ↓
LaTeX consulta: ¿es la línea anterior "corta"?
  ↓
Tu \vspace{0.5em} viene AQUÍ ← DEMASIADO TARDE
  ↓
LaTeX inserta \abovedisplayshortskip O \abovedisplayskip
  ↓
[ECUACIÓN]
  ↓
LaTeX inserta \belowdisplayskip O \belowdisplayshortskip
  ↓
Texto siguiente
```

**El problema**: El `\vspace` manual se inserta *dentro* del flujo horizontal, pero la ecuación display tiene su propio mecanismo de espaciado vertical que **se ejecuta después** del procesamiento del párrafo, en la fase de ruptura de líneas TeX. Tu `\vspace` queda "capturado" en ese procesamiento.[2]

***

## Respuestas a Tus Preguntas Específicas

**P1: ¿Es específico de `lapreprint`?**

R: No. Es comportamiento general de TeX/LaTeX. Cualquier ecuación display (`$$...$$` o `\begin{equation}...\end{equation}`) se comporta así. `lapreprint` no lo causa, solo lo hereda de LaTeX.[2]

**P2: ¿Los hooks de `\AtBeginEnvironment` interfieren?**

R: No directamente. Los hooks que agregaban `\vspace{10pt}` al inicio/final son útiles, pero no "saben" de los registros `\abovedisplayskip`. Por eso necesitas configurarlos explícitamente dentro del hook.[2]

**P3: ¿Por qué `\leavevmode` no ayudó?**

R: Porque `\leavevmode` solo fuerza la transición a modo horizontal. No tiene ningún efecto sobre cómo TeX maneja las ecuaciones display, que operan a nivel de ruptura de líneas (después de que LaTeX ha completado el párrafo en modo horizontal).[1]

**P4: ¿Funciona `\vspace*{}`?**

R: En teoría, `\vspace*{}` (no descartable) mantendría el espacio incluso al inicio de páginas. Pero **el verdadero problema es que ambos (`\vspace` y `\vspace*`) compiten con el sistema de espaciado display** automático de TeX. No es un problema de "desechable vs. no descartable", es un problema de **capas diferentes del procesamiento de TeX**.[2]

***

## Documentación Oficial de Referencia

**Overleaf - `\abovedisplayskip` and related commands**:[2]
> "If the equation is preceded by a 'sufficiently short' line the glue stored in `\abovedisplayshortskip` will be inserted above the equation... For longer lines... TeX will instead insert the glue stored in `\abovedisplayskip`."

**The TeXbook (Knuth, p. 188-189)**: Explicación detallada de cómo TeX elige cuál glue insertar basándose en la longitud de la línea anterior.[2]

**amsmath Package Documentation (CTAN)**: Reconoce que `\abovedisplayskip` controla el espaciado alrededor de ecuaciones display.[1]



***

## Resumen: Tu Próximo Paso

**Reemplaza tu código actual**:

```latex
% ❌ Lo que NO funciona visiblemente
\begin{definition}[Módulo]
Para $z = x + iy$...
\leavevmode\vspace{0.5em}  % Esto está siendo sobrescrito
\[
|z| := \sqrt{x^2 + y^2}
\]
\end{definition}
```

**Con**:

```latex
% ✓ Lo que SÍ funciona
\AtBeginEnvironment{definition}{%
  \setlength{\abovedisplayskip}{1.5em}%
  \setlength{\belowdisplayskip}{1.5em}%
  \setlength{\abovedisplayshortskip}{1.5em}%
  \setlength{\belowdisplayshortskip}{1.5em}%
}

\begin{definition}[Módulo]
Para $z = x + iy$...

\[
|z| := \sqrt{x^2 + y^2}
\]

Geométricamente...
\end{definition}
```

Compila este código y verás que el espaciado alrededor de la ecuación **sí cambia ahora**, porque estás modificando los registros que TeX **realmente usa** para espaciar ecuaciones display.

[1](https://groups.google.com/g/latexusersgroup/c/cXwZxCy29zI)
[2](https://www.overleaf.com/learn/latex/%5Cabovedisplayskip_and_related_commands)
[3](https://www.overleaf.com/learn/latex/Theorems_and_proofs)
[4](https://www.pma.caltech.edu/latex-style-file)
[5](https://madritsch.perso.math.cnrs.fr/downloads/LCMA2UFT30/amsthdoc.pdf)
[6](https://tuck.adelaide.edu.au/LaTeX/ltxenviron.html)
[7](https://www.overleaf.com/learn/latex/Spacing_in_math_mode)
[8](https://github.com/LaPreprint/LaPreprint/wiki)
[9](https://mirrors.ctan.org/macros/latex/required/tools/theorem.pdf)
[10](https://www.reddit.com/r/LaTeX/comments/11jk1n1/increasing_space_between_lines_in_math_display/)
[11](https://ctan.org/pkg/amsthm?lang=en)
[12](https://texdoc.org/serve/amsthm/0)
[13](https://github.com/myst-templates/lapreprint)
[14](https://www.overleaf.com/learn/latex/Display_style_in_math_mode)
[15](https://arxiv.org/html/2405.06128v1)
[16](https://github.com/LaPreprint/typst)
[17](https://www.scribd.com/document/193660862/How-to-Suppress-Vertical-Space-Between-Theorem-Heads-and-Enumitem-Environments)
[18](https://arxiv.org/html/2311.07135v2)
[19](https://github.com/LaPreprint)
[20](https://arxiv.org/html/2305.18511v2)
[21](https://www.scribd.com/document/462065406/transportation-research-board-trb-latex-template)
[22](https://github.com/LaPreprint/LaPreprint)
[23](https://arxiv.org/html/2407.03203v1)
[24](https://www.overleaf.com/learn/latex/Articles/How_to_change_paragraph_spacing_in_LaTeX)
[25](https://github.com/qjcg/awesome-typst)
[26](https://cdn.blot.im/folder/v-2ad4a687/blog_c4dd9b9e12594509b9fed826b0f6b5ce/%5BMusings%5D/Misc/blot%20blog%20post%20example%20files/lapreprintexample.pdf)
[27](https://latex.org/forum/viewtopic.php?t=16556)
[28](https://github.com/LaPreprint/LaPreprint/blob/main/main.tex)
[29](https://www.youtube.com/watch?v=ghjZuHrHKzE)
[30](https://github.com/LaPreprint/LaPreprint/blob/main/lapreprint.cls)
[31](https://www.reddit.com/r/LaTeX/comments/vyh3cc/how_to_reduce_the_vertical_spacing_between/)
[32](https://latex.org/forum/viewtopic.php?t=12894)
[33](https://latex.org/forum/viewtopic.php?t=7974)
[34](https://emerson.emory.edu/services/latex/latex_119.html)
[35](https://www.reddit.com/r/LaTeX/comments/u17337/reducting_spacing_above_and_below_equations/)
[36](https://stackoverflow.com/questions/49977918/mathjax-weird-spacing-before-and-after-display-math)
[37](https://www.latex-project.org/help/documentation/amsldoc.pdf)
[38](https://github.com/wspr/unicode-math/issues/453)
[39](https://www.youtube.com/watch?v=Se88eSiMDQY)
[40](https://es.overleaf.com/learn/latex/Typesetting_exams_in_LaTeX)
[41](https://paulwintz.com/mathematical-writing/theorem-like-environments-in-latex/)
[42](https://nhigham.com/2022/07/14/how-to-space-displayed-mathematical-equations/)
[43](https://latex.org/forum/viewtopic.php?t=20866)
[44](https://www.math.uni-bielefeld.de/~rost/amslatex/doc/amsthdoc.pdf)
[45](https://www.overleaf.com/learn/latex/Typesetting_exams_in_LaTeX)