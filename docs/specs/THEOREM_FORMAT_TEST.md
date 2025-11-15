# THEOREM ENVIRONMENT FORMAT TEST
## Standard rigorous format for PHASE 1B conversion

---

## SETUP IN PREAMBLE (main.tex o lapreprint.cls)

```latex
\usepackage{amsthm}
\usepackage{amsmath}

% Theorem styles
\theoremstyle{plain}
\newtheorem{theorem}{Teorema}[section]
\newtheorem{proposition}[theorem]{Proposición}
\newtheorem{lemma}[theorem]{Lema}
\newtheorem{corollary}[theorem]{Corolario}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definición}
\newtheorem{construction}[theorem]{Construcción}
\newtheorem{observation}[theorem]{Observación}
\newtheorem{example}[theorem]{Ejemplo}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Nota}
\newtheorem{conjecture}[theorem]{Conjetura}
```

---

## USAGE EXAMPLES IN .tex FILES

### Example 1: Definition with Label
```latex
\begin{definition}[Módulo]\label{def:modulo}
Para $z = x + iy \in \mathbb{C}$ con $x, y \in \mathbb{R}$:
\[
|z| := \sqrt{x^2 + y^2}
\]
\end{definition}
```

### Example 2: Proposition with Proof
```latex
\begin{proposition}[Invariancia rotacional]\label{prop:invariancia-rotacional}
Para todo $z \in \mathbb{C}$ y $\theta \in \mathbb{R}$:
\[
|e^{i\theta} z| = |z|
\]
\end{proposition}

\begin{proof}
Sea $z = x + iy$. Entonces:
\[
|e^{i\theta} z| = |(\cos\theta + i\sin\theta)(x + iy)| = \ldots = |z|
\]
\end{proof}
```

### Example 3: Theorem with Proof and Custom Proof Name
```latex
\begin{theorem}[Caracterización única de $\mathbb{C}$]\label{thm:caracterizacion-C}
El plano complejo $\mathbb{C}$ es el único cuerpo algebraicamente cerrado
que satisface los axiomas C1-C7 simultáneamente, salvo isomorfismo.
\end{theorem}

\begin{proof}[Demostración por unicidad]
Supongamos que existe otro cuerpo $\mathbb{F}$ que satisface C1-C7...
\end{proof}
```

### Example 4: Lemma
```latex
\begin{lemma}[Verificación del módulo]\label{lem:verificacion-modulo}
Para triángulo equilátero de lado unitario, las magnitudes son:
\[
|P| = \frac{1}{\sqrt{3}}, \quad |C| = 1, \quad |F| = \frac{\sqrt{3}}{2}
\]
\end{lemma}
```

### Example 5: Corollary
```latex
\begin{corollary}[Semilla binaria]\label{cor:semilla-binaria}
En representación binaria:
\[
M_2 = 3 = 11_2 = \underbrace{11}_{\text{2 unos consecutivos}}
\]
Este es el primer patrón no trivial de unos consecutivos.
\end{corollary}
```

### Example 6: Construction
```latex
\begin{construction}[Rotación de Wick]\label{const:rotacion-wick}
La transformación $t \to it$ convierte métrica euclidiana en pseudo-Riemanniana:
\[
\eta = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\]
\end{construction}
```

### Example 7: Observation
```latex
\begin{observation}[Ángulo óptimo de observación]\label{obs:angulo-optimo}
Existe ángulo desde el cual la curva espacial proyecta los tres fasores
P, C, F con separación angular de 120°.
\end{observation}
```

### Example 8: Example
```latex
\begin{example}[Transformación de Lorentz]\label{ex:lorentz}
Bajo Wick rotation, el boost de Lorentz se convierte en rotación euclidiana:
\[
\Lambda = \begin{pmatrix} \cosh(\phi) & \sinh(\phi) \\ \sinh(\phi) & \cosh(\phi) \end{pmatrix}
\to R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\]
\end{example}
```

### Example 9: Conjecture
```latex
\begin{conjecture}[Isomorfismo logarítmico]\label{conj:isomorfismo-log}
Existe función biyectiva:
\[
\Phi: \sigma \mapsto p_\sigma
\]
determinada por la ecuación logarítmica:
\[
\log_\varphi(2^{p_\sigma}) = \sigma \cdot \lambda + \log_\varphi(3)
\]
\end{conjecture}
```

---

## CROSS-REFERENCES IN TEXT

```latex
% Reference definition
Como se ve en la Definición~\ref{def:modulo}, el módulo es...

% Reference proposition
Por la Proposición~\ref{prop:invariancia-rotacional}, tenemos...

% Reference theorem
El Teorema~\ref{thm:caracterizacion-C} establece que...

% Reference lemma
Del Lema~\ref{lem:verificacion-modulo} se sigue que...

% Reference corollary
El Corolario~\ref{cor:semilla-binaria} implica...

% Reference construction
Por la Construcción~\ref{const:rotacion-wick}...

% Reference observation
La Observación~\ref{obs:angulo-optimo} muestra que...

% Reference example
Como en el Ejemplo~\ref{ex:lorentz}...

% Reference conjecture
La Conjetura~\ref{conj:isomorfismo-log} propone...
```

---

## NUMBERING BEHAVIOR

With `\newtheorem{theorem}{Teorema}[section]`, numbering is:
- Automatic per section
- Format: `Teorema 3.1`, `Teorema 3.2`, etc. (within Section 3)
- All shared counter with `[theorem]` parameter: definitions, propositions, lemmas share same counter

Example for Section 3 (Operador PCF):
- Proposición 3.1
- Definición 3.2
- Lema 3.3
- Teorema 3.4
- Corolario 3.5
- etc.

---

## MIGRATION PATH: FROM CURRENT TO NEW FORMAT

### CURRENT FORMAT (in .tex files):
```latex
\textbf{Definición 3.2.0} (Matriz generadora PCF). La estructura tripartita...
\textbf{Proposición 3.2.0.1} (Propiedades algebraicas). La matriz Ω̂ satisface...
```

### NEW FORMAT (after PHASE 1B):
```latex
\begin{definition}[Matriz generadora PCF]\label{def:matriz-PCF}
La estructura tripartita del operador se codifica mediante la matriz diagonal...
\end{definition}

\begin{proposition}[Propiedades algebraicas]\label{prop:propiedades-matriz}
La matriz $\hat{\Omega}$ satisface...
\end{proposition}
```

---

## ADVANTAGES OF STANDARD FORMAT

1. **Automatic numbering**: LaTeX handles all numbering automatically
2. **Cross-references work**: Use `\ref{}` instead of hardcoding numbers
3. **Professional appearance**: Consistent spacing, fonts, formatting
4. **Proof environment**: Automatic "Proof" heading and QED symbol
5. **Optional titles**: `\begin{theorem}[title]` makes titles optional but clear
6. **Semantic markup**: Later we can change styles globally without editing content

---

## TESTING BEFORE PHASE 1B

Before converting all theorems in PHASE 1B:
1. ✅ Pick ONE section (e.g., Section III.1 Axiomas)
2. ✅ Convert ALL theorems/definitions in that section to new format
3. ✅ Compile and verify output looks professional
4. ✅ Verify cross-references work
5. ✅ If OK: proceed with PHASE 1B system-wide
6. ✅ If issues: fix format in this test doc, then proceed

---

## CRITICAL NOTES FOR SPANISH SPANISH

- Theorem names in Spanish: Teorema, Proposición, Lema, Corolario, Definición, Construcción, Observación, Ejemplo
- Optional argument `[title]` appears after theorem name in output
- Proof environment automatically says "Demostración:" (if using babel spanish)
- Section numbering format: `[section]` gives automatic numbering within each section

