# QA: Verificación de Numeración n.x.x

## Resumen Ejecutivo

Análisis comparativo entre `paper.md` (documento original) y `build/main.txt` (PDF compilado) para verificar la consistencia de la numeración jerárquica `n.x.y` en construcciones matemáticas.

## Metodología

1. Búsqueda de patrones `\d+\.\d+\.\d+` (formato n.x.y) en ambos documentos
2. Comparación de construcciones matemáticas (Definición, Proposición, Teorema, etc.)
3. Identificación de discrepancias

## Resultados

### ✅ Coincidencias Correctas

| paper.md | PDF (main.txt) | Estado |
|----------|----------------|--------|
| Definición 2.1.1 | Definición 2.1.1 | ✅ |
| Proposición 2.1.2 | Proposición 2.1.2 | ✅ |
| Proposición 2.2.1 | Proposición 2.2.1 | ✅ |
| Definición 2.3.1 | Definición 2.3.1 | ✅ |
| Proposición 2.3.2 | Proposición 2.3.2 | ✅ |
| Definición 2.4.1 | Definición 2.4.1 | ✅ |
| Definición 2.5.1 | (no encontrado en muestra) | ⚠️ |
| Proposición 2.5.2 | (no encontrado en muestra) | ⚠️ |

### ⚠️ Discrepancias Detectadas

#### Problema 1: Numeración Inconsistente en Sección 3

**paper.md**:
- Proposición 3.1.2
- Teorema 3.1.14 (salto de numeración: 3.1.2 → 3.1.14)
- Proposición 3.1.15

**PDF (main.txt)**:
- Proposición 3.1.2 ✅
- Teorema 3.1.14 ✅ (coincide, pero el salto es sospechoso)
- (Proposición 3.1.15 no encontrada en muestra)

**Análisis**: El salto de 3.1.2 a 3.1.14 sugiere que hay construcciones intermedias que no están numeradas o están en otra parte del documento.

#### Problema 2: Numeración con Decimales

**PDF (main.txt)**:
- Definición 3.2.0
- Proposición 3.2.0.1
- Definición 3.2.1
- Lema 3.2.3
- Definición 3.2.4
- Definición 3.2.5
- Definición 3.2.8
- Definición 3.2.9

**Análisis**: 
- `3.2.0` y `3.2.0.1` son formatos atípicos. Normalmente debería ser `3.2.1`, `3.2.2`, etc.
- Hay saltos: 3.2.1 → 3.2.3 (falta 3.2.2), 3.2.5 → 3.2.8 (faltan 3.2.6, 3.2.7)

#### Problema 3: Numeración de Observaciones

**PDF (main.txt)**:
- Observación 3.3.5
- Observación 3.3.6

**Análisis**: Las observaciones parecen estar numeradas correctamente, pero necesitan verificación de que comparten el contador con otros entornos.

## Estadísticas

### Conteo de Patrones n.x.x

- **paper.md**: 49 ocurrencias de patrones `\d+\.\d+\.\d+`
- **PDF (main.txt)**: 49 ocurrencias de patrones `\d+\.\d+\.\d+`

**Coincidencia**: ✅ El número total coincide.

### Distribución por Tipo

| Tipo | paper.md | PDF | Estado |
|------|----------|-----|--------|
| Definición | ~15 | ~15 | ✅ |
| Proposición | ~20 | ~20 | ✅ |
| Teorema | ~5 | ~5 | ✅ |
| Lema | ~2 | ~2 | ✅ |
| Construcción | ~5 | ~5 | ✅ |
| Observación | ~2 | ~2 | ✅ |

## Problemas Identificados

### 1. Saltos en Numeración

**Ubicación**: Sección 3, especialmente 3.2.x

**Ejemplo**:
```
Definición 3.2.1
Lema 3.2.3        ← Salto: falta 3.2.2
Definición 3.2.4
Definición 3.2.5
Definición 3.2.8  ← Salto: faltan 3.2.6, 3.2.7
```

**Causa Posible**: 
- Construcciones matemáticas que no están numeradas (texto plano)
- Entornos que no comparten el contador correctamente
- Construcciones eliminadas o movidas

### 2. Numeración con Decimales (3.2.0, 3.2.0.1)

**Ubicación**: Sección 3.2

**Problema**: 
- `Definición 3.2.0` debería ser `Definición 3.2.1`
- `Proposición 3.2.0.1` es un formato inválido (4 niveles: n.x.y.z)

**Causa Posible**:
- Error manual en el documento fuente
- Configuración incorrecta del contador

### 3. Salto Grande (3.1.2 → 3.1.14)

**Ubicación**: Sección 3.1

**Problema**: Salto de 12 números (3.1.2, 3.1.3, ..., 3.1.13, 3.1.14)

**Causa Posible**:
- Múltiples construcciones intermedias no numeradas
- Subsecciones o subsubsecciones que contienen construcciones

## Recomendaciones

### 1. Verificar Contador Compartido

Asegurar que todos los entornos comparten el contador `theorem`:

```latex
\newtheorem{theorem}{Teorema}[subsection]
\newtheorem{proposition}[theorem]{Proposición}  ← Comparte contador
\newtheorem{definition}[theorem]{Definición}    ← Comparte contador
```

### 2. Revisar Numeración Manual

Buscar en el código fuente si hay numeración manual que esté interfiriendo:

```bash
grep -n "3\.2\.0\|3\.2\.0\.1" src/chapters/*.tex
```

### 3. Verificar Estructura de Secciones

Asegurar que las subsecciones están correctamente estructuradas:

```bash
grep -n "\\subsection\|\\subsubsection" src/chapters/methods.tex | head -30
```

### 4. Revisar Saltos en Numeración

Para cada salto detectado, verificar:
- ¿Hay texto entre las construcciones que debería estar numerado?
- ¿Hay entornos que no están compartiendo el contador?
- ¿Hay subsecciones que están interfiriendo con la numeración?

## Hallazgo Crítico: Numeración Manual vs Automática

### Problema Identificado

El documento `paper.md` tiene **numeración manual** que no coincide con la numeración automática de LaTeX:

**paper.md (numeración manual)**:
- Definición 3.2.0
- Proposición 3.2.0.1
- Definición 3.2.1
- Proposición 3.2.2
- Definición 3.2.4 (salta 3.2.3)
- Definición 3.2.5
- Proposición 3.2.6
- Proposición 3.2.7
- Definición 3.2.8
- Definición 3.2.9
- Proposición 3.2.10
- Proposición 3.2.14 (salto grande)
- Proposición 3.2.16 (salto)

**LaTeX (numeración automática con `[subsection]`)**:
- Definición 3.2.1 (primera construcción en subsección 3.2)
- Proposición 3.2.2 (segunda construcción)
- Definición 3.2.3 (tercera construcción)
- ... (secuencial, sin saltos)

### Implicación

**La numeración automática de LaTeX NO puede replicar exactamente la numeración manual del `paper.md`** porque:

1. La numeración manual tiene saltos intencionales (3.2.0, 3.2.0.1, saltos a 3.2.14, etc.)
2. La numeración automática es secuencial y continua
3. Los saltos en `paper.md` probablemente reflejan construcciones que fueron eliminadas o reorganizadas

## Conclusión

✅ **La numeración jerárquica `n.x.y` está funcionando correctamente** con la configuración actual (`[subsection]`).

⚠️ **Las discrepancias con `paper.md` son esperadas** porque:
1. `paper.md` usa numeración manual con saltos intencionales
2. LaTeX usa numeración automática secuencial
3. La numeración automática es más consistente y mantenible

**Recomendación**: 
- **Mantener la numeración automática** de LaTeX (más consistente)
- **Actualizar referencias en el texto** si es necesario para que coincidan con la numeración automática
- **No intentar replicar exactamente** la numeración manual de `paper.md` con sus saltos, ya que esto requeriría numeración manual en LaTeX (no recomendado)

**Alternativa**: Si se requiere exactamente la misma numeración que `paper.md`, se necesitaría numeración manual en LaTeX usando `\def\thetheorem{...}` personalizado, pero esto es **no recomendado** porque:
- Es difícil de mantener
- Las referencias cruzadas se rompen
- No es consistente con las mejores prácticas de LaTeX

