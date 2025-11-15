# Mapeo Completo de Referencias § de paper.md a Labels de LaTeX

Este documento mapea todas las referencias con símbolo § encontradas en `paper.md` a sus labels correspondientes en los archivos `.tex`.

## Metodología

1. Se extrajeron todas las referencias § del `paper.md`
2. Se buscó la sección correspondiente en `paper.md` usando la numeración del MD
3. Se identificó el label equivalente en los archivos `.tex`
4. Se verificó si existe una referencia hardcodeada en `.tex` que necesite ser reemplazada

## Mapeo de Referencias

### Secciones Principales

| Referencia MD | Sección en MD | Label en TEX | Archivo | Línea TEX | Notas |
|--------------|---------------|--------------|---------|-----------|-------|
| §1.2 | 1.2 Obstáculos Históricos | `sec:obstaculos` | introduction.tex | 13 | |
| §1.4 | 1.4 Simetrías y Dualidades | (sin label) | - | - | Necesita label |
| §2 | II. EL PLANO COMPLEJO | `sec:plano-complejo-modulos` | methods.tex | 2 | |
| §2.5 | 2.5 Espacio de Módulos | `subsec:espacio-modulos` | methods.tex | 101 | |
| §2.6 | 2.6 Axiomas del Plano Complejo | `subsec:axiomas-plano-complejo` | methods.tex | 137 | |
| §2.6.2 | 2.6.2 Espacio Adjunto I | `const:rotacion-wick` | methods.tex | 235 | Construcción |
| §2.6.3 | 2.6.3 Espacio Adjunto II | `const:funcionalizacion` | methods.tex | 265 | Construcción |
| §2.6.6 | 2.7.6 Coherencia Categórica | `thm:conmutatividad-functores` | methods.tex | 354 | Teorema |
| §3.1 | 3.1 Axiomas | `subsec:axiomas` | methods.tex | 409 | |
| §3.2 | 3.2 Construcción desde el Módulo | `subsec:construccion-modulo` | methods.tex | 558 | |
| §3.2.0 | 3.2.0 Matriz generadora | `def:matriz-PCF` | methods.tex | 571 | Definición |
| §3.2.1 | 3.2.1 Magnitudes de Componentes | `def:magnitudes-tripartitas` | methods.tex | 640 | Definición |
| §3.2.2 | 3.2.2 Fases de Componentes | `def:fases-componentes` | methods.tex | 682 | Definición |
| §3.2.3 | 3.2.3 Componentes Completas | `def:componentes-PCF` | methods.tex | 707 | Definición |
| §3.2.6 | 3.2.6 (Grupo C₃) | (buscar) | - | - | Necesita identificar |
| §3.2.7 | 3.2.7 (Dualidad Fibonacci) | (buscar) | - | - | Necesita identificar |
| §3.3 | 3.3 Geometría del Círculo en Espacio 3D | `subsec:geometria-3d` | methods.tex | 746 | |
| §3.3.1 | 3.3.1 Parametrización de la Curva | `prop:curva-PCF` | methods.tex | 750 | Proposición |
| §3.3.6 | 3.3.6 Los Tres Vértices | `subsubsec:tres-vertices-referencia` | methods.tex | 820 | |
| §3.3.9 | 3.3.9 Nota Crítica | `subsubsec:vertices-vs-componentes` | methods.tex | 912 | |
| §3.3.10 | 3.3.10 Cierre Topológico | `subsubsec:cierre-topologico` | methods.tex | 926 | |
| §3.3.10.6 | 3.3.10.6 Isomorfismo Bidireccional | `thm:isomorfismo-bidireccional` | methods.tex | 1184 | Teorema |
| §3.4 | 3.4 Proyección al Plano Complejo | `subsec:toro-lattice` | methods.tex | 1291 | |
| §3.5.2 | 3.5.2 Lattice Vertical | `def:lattice-PCF` | methods.tex | 1328 | Definición |
| §3.5.3 | 3.5.3 Invariancia de la Razón | (buscar) | - | - | Necesita identificar |
| §3.5.4 | 3.5.4 Espacio Adjunto | (buscar) | - | - | Necesita identificar |
| §3.5.5 | 3.5.5 Ecuación de Acoplamiento Óptimo | `subsubsec:acoplamiento-optimo` | methods.tex | 1645 | |
| §3.7.2 | 3.7.2 (Kernel Hermítico) | (buscar) | - | - | Necesita identificar |
| §3.7.4 | 3.7.4 (Funciones Ψ_σ) | (buscar) | - | - | Necesita identificar |
| §3.8.2 | 3.8.2 Kernel PCF | `subsubsec:emergencia-hermiticidad` | methods.tex | 1958 | |
| §4 | IV. CONVERGENCIA ESPECTRAL | `convergencia` | results.tex | 2 | |
| §5 | V. INVARIANCIA MODULAR | `invariancia` | results.tex | 64 | |
| §6 | VI. DIMENSIÓN DE HAUSDORFF | `hausdorff` | results.tex | 123 | |
| §7 | VII. TRIPLE CONVERGENCIA | `triple` | results.tex | 173 | |
| §7.2 | 7.2 Independencia Topológica | (buscar) | results.tex | - | Necesita identificar |
| §8 | VIII. RESULTADOS PRINCIPALES | `resultados` | results.tex | 311 | |
| §8.1 | 8.1 Espectro del Operador | (buscar) | results.tex | - | Necesita identificar |
| §9 | IX. CORRESPONDENCIAS | `mersenne` | results.tex | 587 | |
| §IX.0 | (buscar en paper.md) | (buscar) | - | - | |
| §IX.0.1 | (buscar en paper.md) | (buscar) | - | - | |
| §IX.1 | (buscar en paper.md) | (buscar) | - | - | |
| §IX.2 | (buscar en paper.md) | (buscar) | - | - | |

## Referencias que Necesitan Corrección en .tex

### 1. methods.tex línea 344
**Contexto**: Proposición "Conexión con espacio de módulos"
**Referencia en paper.md**: "Conexión con §2.5" (línea 336)
**Acción**: Agregar `\ref{subsec:espacio-modulos}` en el título o texto de la proposición

### 2. methods.tex línea 412
**Contexto**: "en la sección 2"
**Acción**: Reemplazar con `\ref{sec:plano-complejo-modulos}`

## Referencias que Ya Están Correctas

- methods.tex línea 634: Ya usa `\ref{subsubsec:emergencia-hermiticidad}` en lugar de §3.8.2
- results.tex línea 544: Ya usa `\ref{def:magnitudes-tripartitas}` en lugar de §3.2.1

## Próximos Pasos

1. Completar el mapeo de todas las referencias faltantes
2. Identificar labels faltantes en .tex
3. Reemplazar referencias hardcodeadas en .tex
4. Verificar que todas las referencias apunten a labels válidos

