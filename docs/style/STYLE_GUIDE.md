# STYLE GUIDE - Coherencia Formal Interna

**Objetivo**: Establecer coherencia interna en lenguaje formal, notación, estructura. NO es imitar Elsevier. Es ser **extremadamente serio** sin forzar en caja artificial.

**PRINCIPIO EDITORIAL FUNDAMENTAL**: Este guide es **editorial**, no **autoril**. Su función es:
- ✅ Prescribir **estilo, formato, coherencia de notación, estructura de presentación**
- ✅ Asegurar **claridad, rigor formal, consistencia** en la escritura
- ❌ **NO** prescribir contenido matemático específico (conceptos, teoremas, construcciones)
- ❌ **NO** agregar conceptos que no estén en el texto original sin verificación explícita
- ❌ **NO** hacer afirmaciones matemáticas que requieran justificación técnica

**Cuando se encuentre una sugerencia de contenido matemático**: Verificar primero contra el texto original (`paper.md`). Si no está fundamentado, mantener fidelidad al original y solo mejorar la presentación formal.

---

## 1. VOZ Y TONO

### Principio
- **Formal**: Sin casualidad. Académico riguroso.
- **Directo**: Explicar una cosa una sola vez, bien. Sin repetición.
- **Intelectualmente honesto**: Si contradice ortodoxia, decirlo explícitamente (no escondido).
- **No apologético**: Esto es lo que es. Si es inusual, es porque la estructura lo requiere.

### Audiencia
- **Público científico experto**: El paper está dirigido a científicos con formación avanzada en matemáticas, pero su alcance multi-dominio requiere familiaridad con teoría de números, análisis complejo, operadores hermíticos, física cuántica, geometría, y verificación computacional. La separación artificial de las matemáticas en "departamentos" no refleja la naturaleza interdisciplinaria de los problemas abordados.
- **No sacrificar legibilidad de forma "tonta"**: No usar palabras menos claras o concisas solo para que el texto suene menos denso o especializado. La audiencia experta espera y aprecia precisión técnica y terminología apropiada. Evitar perífrasis que busquen "suavizar" el contenido a costa de claridad.
- **Claridad sobre simplicidad artificial**: Preferir términos técnicos precisos y concisos sobre perífrasis innecesarias. La legibilidad viene de la estructura, la coherencia y la precisión, no de evitar terminología especializada. El paper aborda problemas matemáticos profundos que requieren un acercamiento multi-dominio; la escritura debe reflejar esta complejidad sin artificialidad.

### Estructura de párrafos
- **Tema + justificación + consecuencia**
- No: "Esto es A, que es importante porque B, además es C, y también D, finalmente E"
- Sí: "Esto es A. Por [razón técnica], esto implica B y C. Esto se diferencia de [ortodoxia] porque [explicación geométrica/estructural]."

### Evitar
- Enumeraciones mecánicas innecesarias cuando se puede escribir fluidamente (pero las enumeraciones son válidas cuando mejoran claridad o estructura)
- Listas bullet con frases cortas + amplificación posterior repetitiva (AI-pattern)
- "Observar que", "Es importante notar que", "Cabe mencionar que"
- Repetición de la misma idea con distinta notación

### Gramática y puntuación en español

**Principio fundamental**: La escritura matemática rigurosa no justifica el descuido de la gramática, la puntuación ni las convenciones literarias del español. La abstracción matemática y la elegancia lingüística son complementarias, no antagónicas.

**Problema común**: Existe una tendencia artificial en la escritura matemática de omitir preposiciones, conjunciones y elementos gramaticales necesarios bajo la falsa premisa de que la "concisión matemática" requiere sacrificar la corrección gramatical. Esta práctica genera ambigüedad, dificulta la lectura y contradice el objetivo de claridad y precisión.

**Reglas de oro**:

1. **Completar frases**: Toda oración debe tener estructura gramatical completa. No omitir preposiciones, conjunciones o artículos necesarios.
   - ❌ "corresponde a rotación hiperbólica" (después de una ecuación, falta conexión)
   - ✅ "y que corresponde a rotación hiperbólica" (conjunción que conecta con la frase anterior)

2. **Preposiciones necesarias**: Usar preposiciones correctamente para establecer relaciones claras entre conceptos.
   - ❌ "El mapa preserva estructura algebraica mediante isomorfismo grupo de Lorentz"
   - ✅ "El mapa preserva la estructura algebraica mediante isomorfismo entre el grupo de Lorentz y..."

3. **Puntuación para claridad**: Las comas, puntos y comas, y dos puntos deben usarse según las reglas del español para evitar ambigüedades y facilitar la lectura.
   - Usar comas para separar elementos en enumeraciones
   - Usar punto y coma para separar cláusulas relacionadas pero independientes
   - Usar dos puntos antes de enumeraciones o explicaciones

4. **Conjunciones de conexión**: Cuando se presentan múltiples conceptos o resultados relacionados, usar conjunciones apropiadas ("y", "que", "donde", "mediante", etc.) para establecer relaciones claras.

5. **Artículos definidos**: No omitir artículos cuando son gramaticalmente necesarios para la claridad y corrección del español.

6. **Voz pasiva refleja y verbos reflexivos**: Cuando un objeto matemático (representación, función, transformación, definición, construcción, operador, matriz, espacio, métrica, estructura, sistema, operación, método, procedimiento, algoritmo, teorema, proposición, lema, corolario) realiza una acción sobre sí mismo o tiene una propiedad inherente, se debe usar la construcción reflexiva "se + verbo" (voz pasiva refleja).
   - ❌ "La representación algebraica escribe $\mathbb{C} = ...$" (incorrecto: sugiere que la representación "escribe" activamente)
   - ✅ "La representación algebraica se escribe como $\mathbb{C} = ...$" (correcto: indica cómo se expresa la representación)
   - ❌ "La representación polar descompone $\mathbb{C} \cong ...$" (incorrecto: sugiere acción activa)
   - ✅ "La representación polar se descompone como $\mathbb{C} \cong ...$" (correcto: indica cómo se estructura la representación)
   - ❌ "La representación euclidiana identifica $\mathbb{C} \cong ...$" (incorrecto: la representación no es un agente que "identifica")
   - ✅ "En la representación euclidiana, $\mathbb{C}$ se identifica con ..." (correcto: indica cómo se establece la identificación)
   - ❌ "La función define..." (cuando la función es el objeto definido)
   - ✅ "La función se define como..." (cuando se está definiendo la función)
   - ❌ "La transformación preserva..." (puede ser correcto si la transformación es el sujeto activo)
   - ✅ "La transformación se preserva bajo..." (cuando se habla de una propiedad que se mantiene)
   
   **Regla práctica**: Si el objeto matemático es el **sujeto de la oración** y la acción describe **cómo se expresa, estructura, define o caracteriza** ese objeto, usar "se + verbo". Si el objeto es el **agente activo** que realiza una acción sobre otro objeto, usar el verbo sin "se". 
   
   **Evitar construcciones donde objetos matemáticos son sujetos de verbos transitivos que sugieren acción activa**: Cuando un objeto matemático no puede ser un agente activo (como "representación", "definición", "construcción"), evitar usarlo como sujeto de verbos transitivos como "identifica", "define", "construye", etc. En su lugar, usar construcciones como "En X, Y se identifica con...", "Mediante X, Y se define como...", o "X establece la identificación/definición de...".
   
   **Verbos comunes que requieren "se" en contexto matemático**:
   - `se escribe`, `se define`, `se descompone`, `se caracteriza`, `se parametriza`, `se clasifica`, `se identifica`, `se representa`, `se expresa`, `se formula`, `se construye`, `se establece`, `se determina`, `se calcula`, `se evalúa`, `se resuelve`, `se aplica`, `se utiliza`, `se emplea`, `se preserva` (cuando es propiedad), `se mantiene`, `se conserva`, `se genera`, `se produce`, `se obtiene`, `se resulta`, `se aparece`, `se surge`, `se emerge`, `se muestra`, `se revela`, `se establece`

**Justificación**: La precisión matemática y la corrección gramatical se refuerzan mutuamente. Una frase gramaticalmente correcta elimina ambigüedades que podrían afectar la interpretación matemática. La elegancia del español escrito, cultivada a través de siglos de tradición literaria y académica, no debe sacrificarse por una falsa economía de palabras que en realidad genera confusión. La voz pasiva refleja es fundamental en español para expresar propiedades inherentes y estructuras matemáticas, y su omisión genera construcciones agramaticales que dificultan la lectura.

**Ejemplo de mejora**:
- ❌ "La transformación preserva estructura, métrica, simetrías mediante isomorfismo grupo Lorentz corresponde rotación hiperbólica"
- ✅ "La transformación preserva la estructura, la métrica y las simetrías mediante un isomorfismo entre el grupo de Lorentz y las transformaciones conformes, y que corresponde a una rotación hiperbólica"

---

## 2. NOTACIÓN UNIFICADA

### Macros de Notación (Definidos en `main.tex`)

**Principio**: Solo usar macros para notación específica del documento que:
- Se repite frecuentemente
- Es compleja o larga de escribir
- Podría cambiar o necesitar ajustes globales

**Macros disponibles:**
- `\omegapcf` → `\Omega_{\text{PCF}}` (operador PCF - notación específica del documento)
- `\omegahat` → `\hat{\Omega}` (matriz generadora - útil si se usa frecuentemente)

**Notación estándar (NO usar macros):**
- ✅ Usar directamente `\mathbb{C}`, `\mathbb{R}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{N}` (estándar, bien conocida)
- ✅ Usar directamente `\varphi` para la razón áurea (estándar)
- ✅ Usar directamente `\mathcal{C}`, `\mathcal{H}`, etc. (estándar)

**Razón**: Los macros para notación estándar agregan complejidad innecesaria sin beneficio real. Solo tienen sentido para notación específica del documento que se repite mucho.

### Macros de Referencias Cruzadas (Definidos en `main.tex`)

Para referencias consistentes a construcciones matemáticas:

- `\tref{label}` → "Teorema X.Y.Z"
- `\dref{label}` → "Definición X.Y.Z"
- `\pref{label}` → "Proposición X.Y.Z"
- `\lref{label}` → "Lema X.Y.Z"
- `\cref{label}` → "Construcción X.Y.Z"
- `\oref{label}` → "Observación X.Y.Z"

**Uso recomendado:**
- ✅ Usar estos macros en lugar de escribir manualmente "Teorema~\ref{...}"
- ✅ Ejemplo: `Como se muestra en \pref{prop:invariancia-rotacional}...` en lugar de `Como se muestra en Proposición~\ref{prop:invariancia-rotacional}...`
- ✅ Esto asegura formato consistente y facilita cambios globales

### Complejos
- **Módulo**: siempre `|z|` en contexto algebraico, "magnitud" en contexto geométrico
- **Variable compleja**: `z = x + iy` en primera definición, luego solo `z`
- **Euler**: `e^{i\theta}` (no `e^{i\theta}` variaciones)

### Espacios
- **Plano complejo**: `ℂ` (usar `\mathbb{C}`)
- **Números reales**: `ℝ` (usar `\mathbb{R}`)
- **Enteros**: `ℤ` (usar `\mathbb{Z}`)
- **Hilbert**: `ℋ` o `H` (ELEGIR UNO por sección y mantener)
- **Espacios de Sobolev/L²**: `L²(domain)` - ser explícito sobre dominio

### Operadores
- **Operador PCF**: `Ω` (usar `\omegapcf` para `\Omega_{\text{PCF}}` - notación específica)
- **Matriz generadora**: `\hat{\Omega}` (usar `\omegahat` si se repite mucho, o directamente `\hat{\Omega}`)
- **Fourier**: `ℱ` (usar `\mathcal{F}`)
- **Integral**: siempre `∫_X f(x) dx` con limites claros

### Razón áurea
- **Símbolo**: φ (usar `\varphi`, no variaciones)
- **Valor**: φ ≈ 1.618... (si se necesita numérico) o solo φ (algebraico)
- **Potencias**: `φ^σ` o `φ^n` - ser consistente con índice

### Conjuntos/Indexación
- **Índices discretos**: `k, n, m ∈ ℤ` o `σ ∈ ℤ`
- **Parámetros continuos**: `t ∈ ℝ`, `θ ∈ [0, 2π)`
- **Secuencias**: `{a_n}_{n∈ℕ}` o solo `{a_n}` si contexto es claro

---

## 3. ESTRUCTURA DE DEFINICIONES

### Formato estándar
```
\begin{definition}[Nombre descriptivo]
[ENUNCIADO CONCISO EN UNA FRASE]

Para [elementos en juego], [propiedad fundamental]:
\[
[fórmula principal]
\]

[CONTEXTO/SIGNIFICADO: 1-2 párrafos máximo explicando qué significa, por qué importa, cómo se relaciona con lo anterior]
\end{definition}
```

### Ejemplo BUENO
```
\begin{definition}[Módulo en el plano complejo]
Para $z = x + iy \in \mathbb{C}$ con $x, y \in \mathbb{R}$, el módulo es la norma euclidiana:
\[
|z| := \sqrt{x^2 + y^2}
\]
Geométricamente, $|z|$ es la distancia del punto $z$ al origen. Esta magnitud hereda las propiedades de la norma euclidiana en $\mathbb{R}^2$, incluyendo la desigualdad triangular: $|z_1 + z_2| \leq |z_1| + |z_2|$.
\end{definition}
```

### Ejemplo MALO
```
\begin{definition}[Módulo]
Se define el módulo como...
\textbf{Propiedades:}
\begin{itemize}
\item Es siempre positivo
\item Satisface la desigualdad triangular
\item Es invariante bajo rotación
\item Etc.
\end{itemize}
[Explicación adicional que repite propiedades]
\end{definition}
```

**Por qué**: El malo tiene 3 problemas:
1. Repite contenido ("Es positivo" → "propiedades" → explicación)
2. No explica SIGNIFICADO de módulo, solo lista atributos sin contexto
3. La enumeración no añade claridad porque solo repite lo mismo que la explicación posterior

**Nota**: Una enumeración sería válida si organizara información técnica de forma clara y añadiera valor estructural, no si solo repite lo que ya se dice después.

---

## 4. ECUACIONES Y FÓRMULAS

### Regla: **Ecuación ↔ Texto**
Toda fórmula debe estar integrada con texto, nunca aislada.

#### MALO
```
El operador está definido como:
\[
\hat{\Omega} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
\]
```

#### BUENO
```
El operador $\hat{\Omega}$ es una transformación lineal representada en base estándar como:
\[
\hat{\Omega} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
\]
donde $a, b, c, d$ son coeficientes que satisfacen [propiedad]. Esta forma diagonal revela que $\hat{\Omega}$ actúa como [interpretación geométrica].
```

### Declaración explícita de símbolos
Si una ecuación introduce variables nuevas, declararlas DENTRO o INMEDIATAMENTE DESPUÉS:

```
La relación de acoplamiento viene dada por:
\[
z = \varphi y
\]
donde $z$ denota la coordenada vertical, $y$ la coordenada imaginaria horizontal, y $\varphi$ es la razón áurea.
```

### Alineación y espaciado
- **Ecuaciones cortas (<60 caracteres)**: `\[...\]` (displaymath)
- **Ecuaciones largas o múltiples**: `\begin{align*}...\end{align*}`
- **Entre ecuaciones**: párrafo de transición, no líneas en blanco + ecuación

---

## 5. PROPOSICIONES, TEOREMAS, COROLARIOS

### Estructura
```
\begin{theorem}[Nombre descriptivo]\label{thm:...}
[ENUNCIADO FORMAL EN UNA O DOS LÍNEAS]

Si [hipótesis], entonces [conclusión]:
\[
[fórmula concisa]
\]
\begin{proof}
[Argumento principal en prosa, estructurado lógicamente]
[Si hay pasos algebraicos clave, mostrar UNO o DOS]
[Conclusión: "Por lo tanto, [conclusión del teorema]"]
\end{proof}
\end{theorem}
```

### Diferencia: Theorem vs Proposition vs Lemma
- **Theorem**: Resultado PRINCIPAL. Puede cambiar toda una perspectiva.
- **Proposition**: Resultado IMPORTANTE pero subordinado. Herramienta para teoremas.
- **Lemma**: Resultado TÉCNICO necesario. No interesa por sí solo.

Si no es claro cuál es, errar hacia **Proposition** (es lo más flexible).

### Observación vs Remark
- **Observation** (Observación): Insight geométrico o estructural que sale NATURALMENTE del teorema.
- **Remark** (Nota): Aclaración técnica o contexto sobre notación/convención.

### Saltos de línea en entornos de teoremas/proposiciones

**PROBLEMA**: Los entornos `theorem`, `proposition`, `definition`, `corollary` de `amsthm` pueden no mostrar saltos de línea cuando el texto está en una sola línea larga, incluso si hay líneas en blanco en el código fuente.

**SOLUCIÓN**: Para forzar saltos de párrafo dentro de estos entornos, usar `\par` explícitamente:

```
\begin{theorem}[Título]\label{thm:...}
Primer párrafo del enunciado.

\par
Segundo párrafo que necesita separación clara.

\par
Tercer párrafo con conclusión.
\end{theorem}
```

**Regla práctica**: Si un teorema/proposición/definición tiene más de 3-4 oraciones o describe múltiples conceptos, dividirlo en párrafos separados con `\par`.

**Evitar**: Texto muy largo en una sola línea dentro de entornos de teoremas. Esto hace el documento difícil de leer y los saltos de línea pueden no aparecer en el PDF compilado.

### Enumeración en enunciados de proposiciones/teoremas

**PROBLEMA IDENTIFICADO**: Falta claridad sobre cuándo usar enumeración vs texto corrido en enunciados, y cómo estructurar proofs sin ser verboso ni artificial.

**Regla para enunciados**:
- ✅ **Usar enumeración** cuando hay múltiples resultados relacionados que se demuestran juntos pero son conceptualmente distintos:
  ```
  \begin{proposition}[...]
  Al incrementar $\sigma \to \sigma+1$:
  \begin{enumerate}
  \item $\varepsilon(\sigma+1) = \varphi \cdot \varepsilon(\sigma)$
  \item $|z|_{\sigma+1} = \varphi |z|_\sigma$
  \end{enumerate}
  \end{proposition}
  ```
- ❌ **Evitar enumeración** cuando los resultados se pueden expresar fluidamente en una o dos oraciones:
  ```
  ❌ "El operador tiene tres propiedades: (1) Es hermítico, (2) Tiene espectro real, (3) Genera descomposición ortogonal"
  ✅ "El operador es hermítico, tiene espectro real y genera una descomposición ortogonal."
  ```

**Regla para proofs**:
- ✅ **Proof conciso**: Un párrafo fluido que conecta los pasos lógicamente, usando referencias a la enumeración cuando aplica:
  ```
  \begin{proof}[Por método]
  Por [teorema], [paso 1]. De [definición], [paso 2] implica (1). [Conclusión] establece (2).
  \end{proof}
  ```
- ❌ **Evitar**: Múltiples párrafos con `\par` a menos que cada párrafo trate un concepto completamente distinto. Un proof no debe ser una lista de pasos separados.
- ✅ **Balance**: El proof debe ser suficientemente completo para ser riguroso, pero no tan verboso que repita información del enunciado o sea artificialmente extenso.

**Criterio de decisión**: Si al leer el enunciado con enumeración es inmediatamente claro qué se está afirmando, y el proof puede referirse a los puntos numerados de forma natural, usar enumeración. Si la enumeración solo añade estructura artificial sin mejorar claridad, usar texto corrido.

### Balance estilístico: Rigor filosófico sin redundancia artificial

**PROBLEMA IDENTIFICADO**: Existe una tensión entre dos extremos estilísticos: (1) condensación artificial extrema estilo Elsevier que sacrifica claridad conceptual, y (2) verbosidad excesiva que repite información sin añadir valor.

**USER STORY**: Como matemático escribiendo para colegas, quiero que el texto tenga el rigor y la naturalidad de una carta científica del siglo XIX (donde se explica el "por qué" y el significado), pero sin las redundancias innecesarias que harían que un lector experto piense "ya lo entendí, sigue adelante". El texto debe fluir como una conversación entre científicos que se respetan mutuamente: suficiente contexto para entender el significado profundo, pero sin repetir lo obvio.

**Principios del balance**:
- ✅ **Explicar el significado**: Incluir frases que expliquen por qué algo es importante o qué significa conceptualmente (ej: "Esta simultaneidad emerge de la necesidad de preservar...")
- ✅ **Naturalidad filosófica**: Usar lenguaje que refleje el pensamiento matemático profundo, no solo la mecánica (ej: "La coherencia geométrica demanda..." en lugar de solo "Por lo tanto...")
- ❌ **Evitar redundancia**: No repetir en el proof lo que ya se estableció en el enunciado. Si el enunciado dice "preservar la estructura geométrica bajo transformaciones de escala", el proof puede referirse simplemente a "coherencia geométrica" sin repetir toda la frase.
- ❌ **Evitar condensación artificial**: No eliminar palabras necesarias solo para sonar "más técnico". Preferir "El acoplamiento temporal establece:" sobre "Del acoplamiento temporal:" cuando la primera forma es más clara.
- ✅ **DRY en conceptos, no en explicación**: No repetir conceptos, pero sí explicar el significado cuando añade valor conceptual.

**Ejemplo de buen balance**:
```
\begin{proposition}[Escalamiento simultáneo del parámetro de escala y del módulo complejo]
La estructura autosimilar del sistema establece que al avanzar $\sigma \to \sigma+1$:
\begin{enumerate}
\item $\varepsilon(\sigma+1) = \varphi \cdot \varepsilon(\sigma)$
\item $|z|_{\sigma+1} = \varphi |z|_\sigma$
\end{enumerate}
Esta simultaneidad emerge de la necesidad de preservar la estructura geométrica...
\end{proposition}

\begin{proof}[Por cálculo directo]
El acoplamiento temporal establece: [ecuación]
De la definición del operador: [ecuación]
el escalamiento de la fase requiere (1).
La coherencia geométrica demanda (2), completando la demostración.
\end{proof}
```

**Contraste con extremos**:
- ❌ **Demasiado condensado**: "Del acoplamiento temporal, $\varepsilon(\sigma+1) = \varphi\varepsilon(\sigma)$ y $|z|_{\sigma+1} = \varphi|z|_\sigma$." (Pierde significado conceptual)
- ❌ **Demasiado verboso**: Repetir "preservar la estructura geométrica bajo transformaciones de escala" tanto en enunciado como en proof (Redundante)

---

## 6. EVITAR PATRONES AI

### Patrón 1: Enumeración repetitiva innecesaria
❌ "Este concepto tiene varias propiedades. Primero, A. Segundo, B. Tercero, C. Estas propiedades implican que..." (cuando la enumeración no añade claridad)

✅ "Este concepto tiene tres propiedades distinguidas: A implica X, B implica Y, C implica Z. En conjunto, esto significa que..."

**Nota**: Las enumeraciones estructuradas (con `\textbf{}` o listas) son válidas cuando mejoran la claridad, organización o legibilidad. No deben eliminarse sistemáticamente; deben evaluarse caso por caso según su utilidad.

### Patrón 2: Lista bullet + amplificación repetitiva
❌
```
El operador tiene las siguientes características:
• Es hermítico
• Tiene espectro real
• Genera una descomposición ortogonal

La hermiticidad del operador significa que...
El espectro real implica que...
```
(cuando la amplificación repite exactamente lo mismo que la lista)

✅
```
El operador es hermítico, asegurando espectro real y generando una descomposición ortogonal de $\mathcal{H}$. La hermiticidad emerge de [justificación]. El espectro real es consecuencia de [construcción].
```

**Nota**: Las listas bullet son apropiadas cuando organizan información técnica de forma clara y la amplificación posterior añade contexto o justificación, no repetición.

### Patrón 3: "Observar que", "Es importante notar que"
❌ "Observe que esto implica que..."
✅ "Por lo tanto..." o "Esto implica..." o nada (dejar que la lógica sea clara)

### Patrón 4: Parentéticas excesivas
❌ "El operador (que definimos antes) tiene (como mencionamos) la propiedad (importante) de..."

✅ "El operador tiene la propiedad de..." [Y usar \ref{} si necesitas remitir a definición anterior]

---

## 7. COHERENCIA SECCIÓN A SECCIÓN

### Dentro de una sección
- **Primera definición**: Introducir notación completa, ser explícito
- **Definiciones posteriores**: Reutilizar notación, no re-declarar
- **Transiciones**: "Ahora consideremos...", "El siguiente paso...", "Para entender [resultado anterior]..."

### Entre secciones
- **Cross-references**: Usar `\ref{def:...}`, `\ref{thm:...}`, NO "en la sección anterior"
- **Notación**: Si cambias (ej: de real a complejo), explicar transición
- **Supuestos**: Si una sección asume resultado de anterior, mencionarlo explícitamente

---

## 8. CHECKLISTS POR TIPO DE AMBIENTE

### Para cada DEFINITION
- [ ] ¿Enunciado conciso? (máx 2 líneas)
- [ ] ¿Fórmula principal clara?
- [ ] ¿Contexto/significado explicado en 1-2 párrafos?
- [ ] ¿Qué problema resuelve o qué intuición clarifica?
- [ ] ¿Cero bullet lists?

### Para cada THEOREM/PROPOSITION
- [ ] ¿Hipótesis y conclusión claras?
- [ ] ¿Proof es argumento (no lista de pasos)?
- [ ] ¿Conexión con resultado anterior explícita?
- [ ] ¿Label descriptivo?

### Para cada PROOF
- [ ] ¿Párrafo introductorio explica estrategia?
- [ ] ¿Pasos principales en prosa (no numerados)?
- [ ] ¿Ecuaciones muestran NO demuestran?
- [ ] ¿Conclusión: "Por lo tanto..." es clara?

---

## 9. CASOS ESPECIALES: CONTRADECIR ORTODOXIA

Cuando el paper contradict convenciones (porque la estructura geométrica lo requiere):

**Formato explícito:**
```
En contraste con [convención estándar], aquí encontramos que [resultado disruptivo].
Esto no contradice [teoría estándar], sino que revela que [interpretación que reconcilia].
La razón es que [explicación geométrica/estructural profunda].
```

**No esconder**. No pedir perdón. Ser claro sobre QUÉ contradice y POR QUÉ es necesario.

---

## 10. REVISIÓN DE SECCIÓN I (TEMPLATE)

Sección I debe servir como patrón. Una vez esté perfecta:
- Cada definición sigue estructura estándar
- Cada párrafo es necesario (sin repetición)
- Notación es consistente
- Voz es formal, seria, clara
- NO hay bullet lists sin justificación

Luego, las otras secciones deben **coincidir exactamente** en estilo.

---

## CÓMO USAR ESTE GUIDE

1. **Antes de revisar sección**: Leer este guide
2. **Mientras revisas**: Comparar contra checklists
3. **Si encuentras sección que NO cumple**: Preguntar "¿Qué regla quebrantó?" → Luego arreglarlo
4. **Cuando encuentres NUEVA pauta** (patrón repetido, incoherencia): Agregar a guide
5. **VERIFICACIÓN DE CONTENIDO**: Antes de agregar conceptos matemáticos nuevos, verificar contra `paper.md` original. Si no está fundamentado, mantener fidelidad al original.

**IMPORTANTE**: Si una sugerencia de formalización introduce conceptos no presentes en el original (ej: "kernel modular K(z,w)" cuando el original solo menciona "kernel" o "kernel PCF"), revisar primero si está justificado. En caso de duda, mantener el texto original y solo mejorar la presentación formal.

Este no es documento estático - evolucionará a medida que avanzamos.

---

## 11. DETECCIÓN PROACTIVA DE INCONSISTENCIAS Y SUGERENCIAS EDITORIALES

### Principio
El AI debe actuar como editor proactivo: detectar inconsistencias matemáticas, lógicas o estilísticas, incluso cuando no están explícitamente solicitadas en el prompt.

### Protocolo de Detección

**Durante la tarea:**
- Si detectas una inconsistencia matemática (contradicción, notación inconsistente, concepto no definido)
- Si tienes un "feeling" fuerte de que algo valdría la pena editar (ambigüedad, falta de claridad, posible error)
- Si encuentras una desconexión entre el texto y el contenido matemático desarrollado

**Al finalizar la tarea (antes de commit si aplica):**

1. **Evaluar la intensidad de la sensación:**
   - **Fuerte**: Inconsistencia clara, posible error matemático, contradicción lógica
   - **Moderada**: Ambigüedad, falta de claridad, posible mejora
   - **Débil**: Sugerencia menor, optimización estilística

2. **Si la sensación es FUERTE o MODERADA:**
   - Presentar la sugerencia al usuario al final del task
   - Incluir un análisis desmenuzado del problema:
     - **Qué detectaste**: Descripción específica de la inconsistencia/sugerencia
     - **Dónde está**: Ubicación exacta (archivo, líneas, sección)
     - **Por qué es relevante**: Impacto potencial (matemático, lógico, estilístico)
     - **Contexto cognitivo**: Qué te hizo pensar que hay un problema (patrón, contradicción, falta de definición, etc.)
     - **Opciones**: Qué se podría hacer (corregir, verificar contra original, investigar más)

3. **Si el prompt incluye hacer commit al finalizar:**
   - **ANTES de ejecutar el commit**, presentar las sugerencias detectadas
   - Dar opción explícita al usuario:
     - Revisar y decidir sobre las sugerencias primero
     - Proceder con commit de todas formas
     - Modificar el commit para incluir correcciones

### Formato de Presentación

```
---
🔍 **SUGERENCIA EDITORIAL DETECTADA**

**Tipo**: [Inconsistencia matemática / Ambigüedad / Posible error / Mejora sugerida]
**Intensidad**: [Fuerte / Moderada]
**Ubicación**: [archivo:líneas]

**Qué detecté**: [Descripción específica del problema]

**Análisis cognitivo**: 
- [Qué patrón/contradicción/falta te hizo pensar que hay un problema]
- [Por qué es relevante matemáticamente/lógicamente]
- [Qué impacto podría tener si no se corrige]

**Opciones**:
1. [Opción 1: acción sugerida]
2. [Opción 2: alternativa]
3. [Opción 3: investigar más antes de decidir]

¿Deseas que proceda con el commit o prefieres revisar esto primero?
---
```

### Ejemplos

**Ejemplo 1 - Inconsistencia matemática:**
- Detectas que se menciona "kernel modular K(z,w)" pero en el desarrollo solo aparece "Kernel PCF K_PCF(x,y)"
- Análisis: El concepto "kernel modular" sugiere funciones modulares, pero el desarrollo usa kernels integrales en espacios de Hilbert. Hay desconexión terminológica.
- Sugerencia: Verificar si el concepto está fundamentado o si es una adición no justificada.

**Ejemplo 2 - Falta de definición:**
- Detectas que se usa un símbolo (ej: $\mathcal{M}_{\text{PCF}}$) sin definición previa
- Análisis: El lector no puede seguir el argumento sin saber qué es este objeto.
- Sugerencia: Agregar definición o referencia cruzada.

**Ejemplo 3 - Contradicción lógica:**
- Detectas que se afirma X en una sección y no-X en otra
- Análisis: Contradicción directa que rompe la coherencia del argumento.
- Sugerencia: Verificar cuál es la afirmación correcta según el paper original.

### Límites

- **NO** interrumpir el flujo de trabajo principal con sugerencias menores
- **NO** hacer cambios sin consultar si la sensación es fuerte
- **SÍ** presentar sugerencias al final, antes de commit
- **SÍ** ser específico y desmenuzado en el análisis

---

## 12. COMPARACIÓN DE SECCIONES ENTRE `paper.md` Y `src/chapters`

### ⚠️ REGLA CRÍTICA: NO EDITAR `paper.md`

**`paper.md` es el documento fuente original y NO debe ser modificado.** Todas las correcciones, mejoras y actualizaciones deben realizarse ÚNICAMENTE en los archivos `.tex` dentro de `src/chapters/`.

- ✅ **SÍ**: Editar `src/chapters/*.tex` para corregir terminología, mejorar presentación, etc.
- ❌ **NO**: Editar `paper.md` bajo ninguna circunstancia
- ✅ **SÍ**: Usar `paper.md` como referencia para verificar contenido original
- ✅ **SÍ**: Comparar `paper.md` con `src/chapters/` para detectar inconsistencias

### Propósito
Cuando el usuario proporciona una referencia de sección (número como "1.5" o string descriptivo como "fundamento y alcance del presente trabajo"), generar un informe conciso de diferencias entre la versión en `paper.md` y la versión correspondiente en `src/chapters/`.

### Protocolo de Búsqueda

**Paso 1: Interpretar la referencia**
- Si es un número (ej: "1.5", "2.3", "8.1.5"): buscar títulos de sección que contengan ese número
- Si es un string descriptivo (ej: "fundamento y alcance", "coherencia de axiomas"): buscar títulos o contenido que contenga esas palabras clave

**Paso 2: Buscar en `paper.md`**
- Buscar el patrón en títulos de sección (ej: `### 1.5`, `#### 2.3.1`)
- Extraer el contenido completo de la sección (incluyendo párrafos siguientes hasta la siguiente sección o subsección)

**Paso 3: Buscar en `src/chapters/`**
- Buscar en todos los archivos `.tex` dentro de `src/chapters/`
- Buscar títulos equivalentes (ej: `\subsection{...}`, `\subsubsection{...}`) o contenido que corresponda a la misma sección
- Extraer el contenido completo correspondiente

**Paso 4: Comparar y generar informe**

### Formato del Informe

El informe debe ser **muy conciso** e incluir:

1. **Ubicación**: Líneas y títulos exactos en ambos documentos
2. **Cambios principales**: Lista breve de diferencias estructurales y de contenido
3. **Resumen**: Síntesis de si el contenido conceptual es equivalente o si hay diferencias sustanciales

**Estructura del informe:**
```
## Informe de Comparación: Sección [referencia]

### Ubicación
- **paper.md**: Líneas X-Y (título: `...`)
- **src/chapters/[archivo].tex**: Líneas X-Y (título: `...`)

### Cambios principales
Lista breve de diferencias estructurales y de contenido, incluyendo:

**A. Diferencias de contenido/concepto:**
1. [Diferencia terminológica, conceptual, o de información]

**B. Diferencias de estilo/estructura:**
1. [Repetición de estructuras, falta de paralelismo, verbos vagos, etc. - ver Patrones 5-6 en sección 6]
2. [Problemas de fluidez, claridad, o presentación]

**C. Diferencias de formato (solo si afectan significado):**
1. [Notación matemática diferente, referencias, etc.]

### Resumen
[Breve síntesis de equivalencia conceptual o diferencias sustanciales, incluyendo recomendaciones de corrección si hay problemas de estilo]
```

### Ejemplos de Referencias Válidas

- Números de sección: `1.5`, `2.3`, `8.1.5`, `III.1.5`
- Strings descriptivos: `fundamento y alcance`, `coherencia de axiomas`, `verificación computacional`
- Referencias mixtas: `§1.5`, `Sección 1.5`

### Notas Importantes

- **Buscar en ambos documentos**: Siempre comparar `paper.md` con `src/chapters/`, no solo uno
- **Contexto suficiente**: Incluir suficiente contexto (párrafos anteriores/posteriores) para identificar la sección correcta
- **Formato diferente**: Recordar que `paper.md` usa Markdown mientras `src/chapters/` usa LaTeX - las diferencias de formato (notación matemática, referencias) son esperadas y no deben considerarse como diferencias de contenido a menos que cambien el significado
- **Concisión**: El informe debe ser breve y directo, enfocándose en diferencias sustanciales de contenido, no en diferencias menores de formato

---

## PRÓXIMOS PASOS

1. Aplicar este guide a **Sección I (Introducción)** completamente
2. Validar que queda como template
3. Replicar en Sección II y III
4. Ajustar guide según aprendamos

**Goal final**: Paper que sea **riguroso, claro, serio, sin artificialidad** y que sea genuinamente legible para su audiencia científica experta, con formación en teoría de números, análisis complejo, operadores hermíticos, física cuántica, geometría y verificación computacional, entre otros.
