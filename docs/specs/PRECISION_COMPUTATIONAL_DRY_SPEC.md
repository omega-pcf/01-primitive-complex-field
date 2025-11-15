# Especificación: Manejo DRY de Precisión Computacional

## Objetivo

Eliminar repetición de menciones de precisión computacional (IEEE 754, $\varepsilon_{\text{mach}}$, errores $< 10^{-14}$, etc.) mediante definición formal centralizada y referencias cruzadas.

## Problema Identificado

Las menciones de precisión computacional aparecen repetidamente en múltiples ubicaciones con formulaciones inconsistentes:

### Ubicaciones Actuales

1. **`src/chapters/abstract.tex` (línea 7)**:
   - "discrepancias observadas ($\sim 10^{-14}$) reflejan límites de precisión numérica IEEE 754"

2. **`src/chapters/introduction.tex` (línea 70)**:
   - Sidenote: "Error acotado por límite de doble precisión IEEE 754 (64 bits)"
   - Texto: "alcanza error $< 10^{-14}$ para $n \sim 10^{10}$"

3. **`src/chapters/results.tex` (línea 86)**:
   - "El error observado numéricamente ($< 10^{-15}$) proviene únicamente de precisión finita de aritmética de punto flotante"

4. **`src/chapters/results.tex` (línea 205)**:
   - "El error es $< 10^{-15}$ para todo $\sigma \in [1,50]$, limitado únicamente por precisión de máquina"

5. **`src/chapters/results.tex` (línea 453)**:
   - "permaneciendo en el nivel de ruido numérico IEEE 754 ($\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$) para todos los ceros verificados"
   - **Esta es la formulación más rigurosa y completa**

6. **`src/chapters/methods.tex` (línea 1805)**:
   - "Ambas ecuaciones de acoplamiento se verifican con precisión de máquina ($<10^{-14}$)"

### Problemas

- **Repetición**: Misma información expresada de múltiples formas
- **Inconsistencia**: Diferentes valores ($10^{-14}$, $10^{-15}$, $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$)
- **Falta de rigor**: Algunas menciones no especifican el estándar IEEE 754 ni $\varepsilon_{\text{mach}}$
- **Violación DRY**: Información técnica repetida en lugar de referenciada

## Solución Propuesta

### 1. Definición Formal Centralizada

**Ubicación**: `src/chapters/results.tex`, justo antes de la línea 453 (antes de "El error no crece monótonamente...")

**Formato**: Definición formal con label para referencia cruzada

```latex
\begin{definition}[Precisión computacional]\label{def:precision-computacional}
Todas las verificaciones numéricas de este trabajo utilizan aritmética de punto flotante de doble precisión según el estándar IEEE 754 (64 bits), con épsilon de máquina:
\[
\varepsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}
\]
Los errores observados en verificaciones computacionales están acotados por este límite fundamental de precisión numérica. Cuando se reporta error $< 10^{-14}$ o $< 10^{-15}$, esto refleja el nivel de ruido numérico inherente a la representación finita, no deficiencia matemática del operador.
\end{definition}
```

**Justificación de ubicación**:
- `results.tex` es donde se presenta la verificación computacional más detallada
- La línea 453 ya contiene la mención más rigurosa
- Es el lugar natural donde un lector buscaría información técnica sobre precisión

### 2. Referencias desde Otros Archivos

#### Abstract (`src/chapters/abstract.tex`)

**Línea 7 actual**:
```latex
La verificación numérica confirma robustez estructural del operador: discrepancias observadas ($\sim 10^{-14}$) reflejan límites de precisión numérica IEEE 754, no deficiencia matemática.
```

**Cambio propuesto**:
```latex
La verificación numérica confirma robustez estructural del operador: discrepancias observadas reflejan límites de precisión computacional (véase \ref{def:precision-computacional}), no deficiencia matemática.
```

**Razón**: Elimina repetición de detalles técnicos, mantiene el mensaje conceptual.

#### Introduction (`src/chapters/introduction.tex`)

**Línea 70 actual**:
```latex
La verificación\sidenote{Error acotado por límite de  doble precisión IEEE 754 (64 bits).} alcanza error $< 10^{-14}$ para $n \sim 10^{10}$ (altura $t \sim 10^{23}$).
```

**Cambio propuesto**:
```latex
La verificación alcanza precisión de máquina (véase \ref{def:precision-computacional}) para $n \sim 10^{10}$ (altura $t \sim 10^{23}$).
```

**Razón**: Elimina sidenote redundante y repetición de valores numéricos.

#### Methods (`src/chapters/methods.tex`)

**Línea 1805 actual**:
```latex
Ambas ecuaciones de acoplamiento se verifican con precisión de máquina ($<10^{-14}$):
```

**Cambio propuesto**:
```latex
Ambas ecuaciones de acoplamiento se verifican con precisión de máquina (véase \ref{def:precision-computacional}):
```

**Razón**: Elimina repetición del valor numérico.

#### Results (`src/chapters/results.tex`)

**Línea 86 actual**:
```latex
Esta NO es convergencia asintótica ($\lim_{\sigma \to \infty}$) sino igualdad algebraica exacta para todo $\sigma \in \mathbb{N}$. El error observado numéricamente ($< 10^{-15}$) proviene únicamente de precisión finita de aritmética de punto flotante.
```

**Cambio propuesto**:
```latex
Esta NO es convergencia asintótica ($\lim_{\sigma \to \infty}$) sino igualdad algebraica exacta para todo $\sigma \in \mathbb{N}$. El error observado numéricamente proviene únicamente de precisión finita de aritmética de punto flotante (véase \ref{def:precision-computacional}).
```

**Línea 205 actual**:
```latex
\item \textbf{Tasa}: Algebraica exacta. El error es $< 10^{-15}$ para todo $\sigma \in [1,50]$, limitado únicamente por precisión de máquina.
```

**Cambio propuesto**:
```latex
\item \textbf{Tasa}: Algebraica exacta. El error para todo $\sigma \in [1,50]$ está limitado únicamente por precisión de máquina (véase \ref{def:precision-computacional}).
```

**Línea 453 actual**:
```latex
El error no crece monótonamente con $n$, permaneciendo en el nivel de ruido numérico IEEE 754 ($\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$) para todos los ceros verificados.
```

**Cambio propuesto**:
```latex
El error no crece monótonamente con $n$, permaneciendo en el nivel de ruido numérico (véase \ref{def:precision-computacional}) para todos los ceros verificados.
```

**Razón**: La definición formal ya contiene esta información, solo necesitamos referenciarla.

### 3. Tablas y Datos Numéricos

**Principio**: Las tablas con valores numéricos específicos (ej: Tabla 8.1 en `results.tex`) mantienen sus valores de error individuales, ya que son datos empíricos. Solo las menciones textuales generales se simplifican.

**Ejemplo**: La Tabla 8.1 con errores individuales ($1.30 \times 10^{-14}$, etc.) se mantiene tal cual. Solo las afirmaciones generales como "error $< 10^{-14}$" se reemplazan con referencias.

## Estructura de la Definición

### Contenido Requerido

1. **Estándar técnico**: IEEE 754, doble precisión, 64 bits
2. **Épsilon de máquina**: $\varepsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$
3. **Interpretación**: Errores observados reflejan límites de representación, no deficiencia matemática
4. **Rango típico**: Errores $< 10^{-14}$ o $< 10^{-15}$ están en el nivel de ruido numérico

### Formato LaTeX

```latex
\begin{definition}[Precisión computacional]\label{def:precision-computacional}
Todas las verificaciones numéricas de este trabajo utilizan aritmética de punto flotante de doble precisión según el estándar IEEE 754 (64 bits), con épsilon de máquina:
\[
\varepsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}
\]
Los errores observados en verificaciones computacionales están acotados por este límite fundamental de precisión numérica. Cuando se reporta error $< 10^{-14}$ o $< 10^{-15}$, esto refleja el nivel de ruido numérico inherente a la representación finita, no deficiencia matemática del operador.
\end{definition}
```

## Checklist de Implementación

### Paso 1: Crear Definición Formal
- [ ] Agregar definición en `src/chapters/results.tex` antes de línea 453
- [ ] Verificar que el label `def:precision-computacional` sea único
- [ ] Asegurar que la definición esté en contexto apropiado (sección de verificación computacional)

### Paso 2: Actualizar Abstract
- [ ] Reemplazar mención explícita con referencia a `\ref{def:precision-computacional}`
- [ ] Mantener mensaje conceptual sobre robustez
- [ ] Verificar que el flujo narrativo se mantenga

### Paso 3: Actualizar Introduction
- [ ] Eliminar sidenote redundante en línea 70
- [ ] Reemplazar "error $< 10^{-14}$" con referencia
- [ ] Simplificar texto manteniendo información esencial

### Paso 4: Actualizar Methods
- [ ] Reemplazar "precisión de máquina ($<10^{-14}$)" con referencia
- [ ] Mantener contexto de verificación de ecuaciones

### Paso 5: Actualizar Results
- [ ] Línea 86: Reemplazar mención explícita con referencia
- [ ] Línea 205: Reemplazar mención explícita con referencia
- [ ] Línea 453: Reemplazar mención explícita con referencia (después de crear definición)
- [ ] Mantener tablas con valores numéricos específicos sin cambios

### Paso 6: Verificación
- [ ] Compilar documento y verificar que referencias funcionen
- [ ] Verificar que no haya referencias rotas
- [ ] Revisar que el flujo narrativo se mantenga en todos los archivos
- [ ] Confirmar que la definición sea accesible desde todos los puntos de referencia

## Consideraciones Adicionales

### Contexto de Uso

- **Abstract**: Mención breve y conceptual
- **Introduction**: Contexto de verificación computacional
- **Methods**: Verificación de ecuaciones técnicas
- **Results**: Verificación detallada con datos numéricos

### Mantenimiento de Información Específica

- **Valores numéricos en tablas**: Se mantienen (son datos empíricos)
- **Rangos específicos**: Se mantienen si son relevantes para el contexto (ej: "para $n \sim 10^{10}$")
- **Comparaciones**: Se mantienen si son parte del argumento (ej: comparación con otros métodos)

### Estilo y Tono

- **Rigor técnico**: La definición formal debe ser precisa y completa
- **Claridad**: Las referencias deben ser claras sin interrumpir el flujo
- **Consistencia**: Todas las referencias deben usar el mismo formato

## Ejemplo de Resultado Final

### Antes (con repetición):
```latex
% Abstract
discrepancias observadas ($\sim 10^{-14}$) reflejan límites de precisión numérica IEEE 754

% Introduction
La verificación\sidenote{Error acotado por límite de doble precisión IEEE 754 (64 bits).} alcanza error $< 10^{-14}$

% Methods
se verifican con precisión de máquina ($<10^{-14}$)

% Results (múltiples lugares)
El error observado numéricamente ($< 10^{-15}$) proviene únicamente de precisión finita...
El error es $< 10^{-15}$ para todo $\sigma \in [1,50]$, limitado únicamente por precisión de máquina...
permaneciendo en el nivel de ruido numérico IEEE 754 ($\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$)
```

### Después (DRY con referencia):
```latex
% Results (definición única)
\begin{definition}[Precisión computacional]\label{def:precision-computacional}
[... definición completa ...]
\end{definition}

% Abstract
discrepancias observadas reflejan límites de precisión computacional (véase \ref{def:precision-computacional})

% Introduction
La verificación alcanza precisión de máquina (véase \ref{def:precision-computacional}) para $n \sim 10^{10}$

% Methods
se verifican con precisión de máquina (véase \ref{def:precision-computacional})

% Results (referencias)
El error observado numéricamente proviene únicamente de precisión finita (véase \ref{def:precision-computacional})
El error está limitado únicamente por precisión de máquina (véase \ref{def:precision-computacional})
permaneciendo en el nivel de ruido numérico (véase \ref{def:precision-computacional})
```

## Notas de Implementación

1. **Orden de cambios**: Crear la definición primero, luego actualizar referencias
2. **Compilación**: Verificar después de cada cambio que el documento compile correctamente
3. **Referencias cruzadas**: Asegurar que `\ref{def:precision-computacional}` funcione desde todos los archivos
4. **Contexto**: La definición debe estar en una ubicación lógica dentro de `results.tex` (sección de verificación computacional)

## Referencias Internas

- STYLE_GUIDE.md: Principio DRY y evitar repetición
- Abstract actual: Línea 7
- Introduction actual: Línea 70
- Methods actual: Línea 1805
- Results actual: Líneas 86, 205, 453

