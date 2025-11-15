# Spec: Mapeo de Nomenclatura y Estructura del Paper

## Objetivo

Mapear el outline del draft final (`paper.md`) a la estructura actual del paper LaTeX, identificando problemas de nomenclatura y proponiendo mejoras para títulos más descriptivos, densos y concisos.

## Metodología

1. **Mapeo Outline → LaTeX**: Identificar correspondencias entre secciones del draft y estructura LaTeX actual
2. **Análisis de Nomenclatura**: Identificar términos genéricos repetidos (especialmente "módulo") y evaluar si requieren nombres más específicos
3. **Propuestas de Mejora**: Sugerir nombres más descriptivos y densos que capturen la esencia semántica

---

## 1. Mapeo Outline Draft → Estructura LaTeX

### Parte I: Introducción

| Draft (paper.md) | LaTeX Actual | Estado |
|------------------|--------------|--------|
| 1.1 La Conjetura de Hilbert-Pólya... | `\section{Introducción}` → `\subsection{La Conjetura de Hilbert-Pólya...}` | ✅ Mapeado |
| 1.2 Obstáculos Históricos... | `\subsection{Obstáculos Históricos...}\label{sec:obstaculos}` | ✅ Mapeado |
| 1.3 Traducción entre Dominios... | `\subsection{Traducción entre Dominios...}` | ✅ Mapeado |
| 1.4 Simetrías y Dualidades... | `\subsection{Simetrías y Dualidades...}\label{subsec:simetrias-dualidades}` | ✅ Mapeado |
| 1.5 Fundamento y Alcance... | `\subsection{Fundamento y Alcance del Presente Trabajo}` | ✅ Mapeado |
| 1.6 Verificación Computacional | `\subsection{Verificación Computacional}` | ✅ Mapeado |
| 1.7 Estructura del Presente Trabajo | `\subsection{Estructura del Presente Trabajo}` | ✅ Mapeado |

### Parte II: El Plano Complejo como Espacio de Módulos

| Draft (paper.md) | LaTeX Actual | Estado |
|------------------|--------------|--------|
| 2.1 El Módulo: Magnitud Primitiva | `\section{El Plano Complejo como Espacio de Módulos}` → `\subsection{El Módulo: Magnitud Primitiva}` | ✅ Mapeado |
| Def. 2.1.1 (Módulo) | `\begin{definition}[Módulo]\label{def:modulo}` | ⚠️ **PROBLEMA: Nombre genérico** |
| Prop. 2.1.2 (Invariancia rotacional) | `\begin{proposition}[Invariancia rotacional]\label{prop:invariancia-rotacional}` | ✅ Bueno |
| 2.2 Rotación como Generador | `\subsection{Rotación como Generador del Plano}` | ✅ Mapeado |
| Prop. 2.2.1 (Dualidad geométrica-algebraica) | `\begin{proposition}[Dualidad geométrica-algebraica]\label{prop:dualidad-geometrica-algebraica}` | ✅ Bueno |
| 2.3 Módulo Algebraico y Estructura de Cuerpo | `\subsection{Módulo Algebraico y Estructura de Cuerpo}` | ✅ Mapeado |
| Def. 2.3.1 (Módulo algebraico) | `\begin{definition}[Módulo algebraico]\label{def:modulo-algebraico}` | ⚠️ **PROBLEMA: Conflicto con def:modulo** |
| Prop. 2.3.2 (Equivalencia de definiciones) | `\begin{proposition}[Equivalencia y privilegio de perspectiva]\label{prop:equivalencia-definiciones}` | ✅ Mejorado |
| 2.4 Lattices: Estructura Discreta | `\subsection{Lattices: Estructura Discreta}` | ✅ Mapeado |
| Def. 2.4.1 (Lattice) | `\begin{definition}[Lattice: periodicidad bidimensional]\label{def:lattice}` | ✅ Mejorado |
| Def. 2.4.2 (Toro complejo) | `\begin{definition}[Toro complejo]\label{def:toro}` | ✅ Bueno |
| 2.5 Espacio de Módulos | `\subsection{Espacio de Módulos}\label{subsec:espacio-modulos}` | ✅ Mapeado |
| Def. 2.5.1 (Espacio de módulos de lattices) | `\begin{definition}[Espacio de módulos de lattices]\label{def:espacio-modulos-lattices}` | ✅ Específico |
| Prop. 2.5.2 (Herencia estructural) | `\begin{proposition}[Herencia estructural]\label{prop:herencia-estructural}` | ✅ Bueno |
| 2.6 Axiomas del Plano Complejo | `\subsection{Axiomas del Plano Complejo}\label{subsec:axiomas-plano-complejo}` | ✅ Mapeado |
| 2.7 Espacios Adjuntos | `\subsection{Espacios Adjuntos: Re-parametrizaciones de $\mathbb{C}$}\label{subsec:espacios-adjuntos}` | ✅ Mapeado |

### Parte III: El Operador PCF

| Draft (paper.md) | LaTeX Actual | Estado |
|------------------|--------------|--------|
| 3.1 Axiomas | `\section{El Operador $\omegapcf$}` → `\subsection{Construcción Axiomática}\label{subsec:axiomas}` | ✅ Mapeado |
| 3.2 Construcción desde el Módulo | `\subsection{Construcción desde el Módulo}\label{subsec:construccion-modulo}` | ✅ Mapeado |
| Def. 3.2.0 (Matriz generadora PCF) | `\begin{definition}[Matriz generadora PCF]\label{def:matriz-PCF}` | ✅ Bueno |
| Def. 3.2.1 (Magnitudes tripartitas) | `\begin{definition}[Magnitudes tripartitas]\label{def:magnitudes-tripartitas}` | ✅ Bueno |
| Lema 3.2.3 (Verificación del módulo) | `\begin{lemma}[Verificación del módulo]\label{lem:verificacion-modulo}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |
| Cor. 3.2.11 (Módulo constante) | `\begin{corollary}[Módulo constante]\label{cor:modulo-constante}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |
| Prop. 3.2.X (Módulo 3D) | `\begin{proposition}[Módulo 3D]\label{prop:modulo-3D}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |
| Prop. 3.2.X (Escalamiento de módulo) | `\begin{proposition}[Escalamiento de módulo]\label{prop:escalamiento-modulo}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |
| Def. 3.X (Módulo topológico) | `\begin{definition}[Módulo topológico]\label{def:modulo-topologico}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |
| Prop. 3.X (Módulo proyectado) | `\begin{proposition}[Módulo proyectado]\label{prop:modulo-proyectado}` | ⚠️ **PROBLEMA: "módulo" ambiguo** |

---

## 2. Análisis de Problemas de Nomenclatura

### 2.1 Uso Repetido de "Módulo"

El término "módulo" aparece en múltiples contextos con significados diferentes:

#### Contextos Identificados:

1. **Módulo básico** (`def:modulo`): `|z| = \sqrt{x^2 + y^2}` - Magnitud primitiva del número complejo
2. **Módulo algebraico** (`def:modulo-algebraico`): `|z|^2 = z \cdot \bar{z}` - Formulación mediante producto hermítico
3. **Módulo constante** (`cor:modulo-constante`): `|\Omega| = 1/2` - Propiedad del operador PCF
4. **Módulo 3D** (`prop:modulo-3D`): Módulo en espacio tridimensional extendido
5. **Módulo proyectado** (`prop:modulo-proyectado`): Módulo después de proyección al plano
6. **Módulo topológico** (`def:modulo-topologico`): `M_{\text{PCF}} = \pi/\varepsilon_0` - Parámetro modular
7. **Escalamiento de módulo** (`prop:escalamiento-modulo`): Comportamiento del módulo bajo escalamiento
8. **Razón de módulos 3D/2D** (`prop:razon-modulos-3d-2d`): Comparación entre módulos en diferentes dimensiones
9. **Verificación del módulo** (`lem:verificacion-modulo`): Verificación de que `|P| \cdot |C| \cdot |F| = 1/2`
10. **Invariancia del módulo** (`cor:invariancia-modulo`): Propiedad de invariancia

#### Problema Principal:

El término "módulo" es **demasiado genérico** y puede causar confusión. En matemáticas, "módulo" puede referirse a:
- Módulo de un número complejo (magnitud)
- Módulo algebraico (estructura sobre anillo)
- Módulo modular (parámetro en teoría de módulos)
- Módulo de un operador (norma)

### 2.2 Otros Términos Genéricos Identificados

- **"Estructura"**: Aparece en múltiples contextos (estructura distribuida, estructura lattice, estructura discreta, etc.)
- **"Espacio"**: Espacio de módulos, espacio de Hilbert, espacio adjunto, espacio cociente
- **"Propiedades"**: Propiedades algebraicas, propiedades geométricas, etc.

---

## 3. Propuestas de Mejora

### 3.1 Principios de Nomenclatura

1. **Especificidad**: Los nombres deben ser específicos al contexto
2. **Densidad semántica**: Capturar la esencia en pocas palabras
3. **Claridad**: Evitar ambigüedad sin sacrificar concisión
4. **Consistencia**: Usar terminología consistente dentro del mismo dominio conceptual
5. **Creatividad controlada**: Permitir nombres creativos cuando capturen conceptos únicos

### 3.2 Propuestas Específicas para "Módulo"

#### Contexto 1: Módulo Básico del Número Complejo
- **Actual**: `[Módulo]` (`def:modulo`)
- **Propuesta**: `[Magnitud compleja]` o `[Módulo euclidiano]` o mantener `[Módulo]` si es el contexto primario
- **Justificación**: Es el módulo canónico, puede mantener nombre genérico si es claro que es el contexto base

#### Contexto 2: Módulo Algebraico
- **Actual**: `[Módulo algebraico]` (`def:modulo-algebraico`)
- **Propuesta**: `[Módulo hermítico]` o `[Norma hermítica]`
- **Justificación**: Específica que emerge del producto hermítico, más preciso

#### Contexto 3: Módulo del Operador PCF
- **Actual**: `[Módulo constante]` (`cor:modulo-constante`)
- **Propuesta**: `[Magnitud invariante del operador]` o `[Norma constante de $\Omega$]` o `[Punto fijo de magnitud]`
- **Justificación**: Específica que es propiedad del operador, no del número complejo genérico

#### Contexto 4: Módulo 3D
- **Actual**: `[Módulo 3D]` (`prop:modulo-3D`)
- **Propuesta**: `[Magnitud en extensión ortogonal]` o `[Norma en espacio extendido]`
- **Justificación**: Específica que es en el espacio extendido, no en el plano complejo base

#### Contexto 5: Módulo Proyectado
- **Actual**: `[Módulo proyectado]` (`prop:modulo-proyectado`)
- **Propuesta**: `[Magnitud bajo proyección vertical]` o `[Norma proyectada al plano]`
- **Justificación**: Específica la operación de proyección

#### Contexto 6: Módulo Topológico
- **Actual**: `[Módulo topológico]` (`def:modulo-topologico`)
- **Propuesta**: `[Parámetro modular PCF]` o `[Invariante modular $M_{\text{PCF}}$]`
- **Justificación**: Es un parámetro modular, no una magnitud. Debería distinguirse claramente.

#### Contexto 7: Verificación del Módulo
- **Actual**: `[Verificación del módulo]` (`lem:verificacion-modulo`)
- **Propuesta**: `[Producto de magnitudes tripartitas]` o `[Identidad de magnitudes PCF]`
- **Justificación**: Específica que verifica el producto de las tres magnitudes

#### Contexto 8: Escalamiento de Módulo
- **Actual**: `[Escalamiento de módulo]` (`prop:escalamiento-modulo`)
- **Propuesta**: `[Escalamiento de magnitud bajo $\varphi$]` o `[Comportamiento de norma bajo escalamiento áureo]`
- **Justificación**: Específica el tipo de escalamiento

### 3.3 Propuestas para Otros Términos

#### "Estructura"
- **Estructura distribuida** → `[Referencia distribuida]` o `[Coherencia multi-dominio]` (más específico)
- **Estructura lattice** → `[Periodicidad lattice]` o `[Estructura discreta lattice]`
- **Estructura discreta** → `[Discretización lattice]` o `[Periodicidad bidimensional]`

#### "Espacio"
- Los espacios están bien diferenciados por contexto (espacio de módulos, espacio de Hilbert, etc.)

---

## 4. Conceptos Únicos que Merecen Nombres Propios

### 4.1 Conceptos Identificados para Bautizar

1. **El operador $\omegapcf$**: Ya tiene nombre propio ✅
2. **El lattice $\Lambda_{\text{PCF}}$**: Ya tiene nombre específico ✅
3. **El módulo topológico $M_{\text{PCF}}$**: Podría tener nombre más memorable
   - **Propuesta**: `[Invariante modular áureo]` o `[Constante de modularización PCF]`
4. **La estructura tripartita $(P, C, F)$**: Ya tiene nombres específicos ✅
5. **El círculo crítico $|z| = 1/2$**: Ya tiene nombre ✅
6. **Las ecuaciones de acoplamiento**: Ya tienen nombres específicos ✅

### 4.2 Oportunidades de Nomenclatura Creativa

1. **El mecanismo de construcción del kernel**: Podría tener nombre que capture la "emergencia de hermiticidad"
2. **La correspondencia Mersenne-áurea**: Ya está bien descrita
3. **La triple convergencia**: Ya tiene nombre descriptivo

---

## 5. Checklist de Implementación

### Fase 1: Identificación Completa
- [ ] Mapear todas las definiciones, proposiciones, teoremas del draft a LaTeX
- [ ] Identificar todos los usos de términos genéricos
- [ ] Catalogar conflictos de nomenclatura

### Fase 2: Propuestas de Mejora
- [ ] Proponer nombres alternativos para cada conflicto
- [ ] Evaluar impacto de cambios (referencias cruzadas, consistencia)
- [ ] Priorizar cambios por impacto/confusión

### Fase 3: Implementación
- [ ] Actualizar definiciones/proposiciones con nuevos nombres
- [ ] Actualizar referencias cruzadas
- [ ] Verificar consistencia en todo el documento

---

## 6. Ejemplos de Mejora

### Ejemplo 1: Módulo vs. Magnitud

**Antes:**
- `[Módulo]` - ambiguo
- `[Módulo algebraico]` - ambiguo
- `[Módulo constante]` - ambiguo

**Después:**
- `[Magnitud compleja]` o `[Módulo euclidiano]` - específico al contexto base
- `[Norma hermítica]` - específico al método de construcción
- `[Magnitud invariante del operador]` - específico al objeto matemático

### Ejemplo 2: Módulo Topológico

**Antes:**
- `[Módulo topológico]` - confunde con magnitud

**Después:**
- `[Parámetro modular PCF]` o `[Invariante modular $M_{\text{PCF}}$]` - específico que es parámetro, no magnitud

---

## 7. Notas sobre Convenciones Matemáticas

### 7.1 Uso de "Módulo" en Matemáticas

En matemáticas, "módulo" tiene múltiples significados aceptados:
- **Módulo de número complejo**: `|z|` (magnitud)
- **Módulo algebraico**: Estructura sobre anillo
- **Módulo modular**: Parámetro en teoría de módulos (Riemann)

### 7.2 Justificación de Cambios

Aunque es común usar "módulo" en diferentes contextos, en un paper técnico denso es preferible:
1. **Claridad sobre convención**: Si mantenemos "módulo", debe ser claro por contexto
2. **Especificidad cuando hay riesgo de confusión**: Cuando hay múltiples usos cercanos, usar términos más específicos
3. **Consistencia interna**: Una vez elegido un término, usarlo consistentemente

---

## 8. Próximos Pasos

1. **Revisar mapeo completo**: Completar mapeo de todas las secciones del draft
2. **Identificar más conflictos**: Buscar otros términos genéricos problemáticos
3. **Proponer nombres específicos**: Para cada conflicto identificado
4. **Validar con usuario**: Presentar propuestas para aprobación antes de implementar
5. **Implementar cambios**: Actualizar nomenclatura en todo el documento

---

## Referencias

- Draft final: `./paper.md`
- Estructura LaTeX: `src/chapters/methods.tex`, `src/chapters/results.tex`, etc.
- Convenciones matemáticas: RAE, estándares de nomenclatura matemática

