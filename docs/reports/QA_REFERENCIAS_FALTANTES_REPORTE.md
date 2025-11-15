# Reporte Exhaustivo: Referencias Faltantes por Corregir

**Fecha**: 2025-01-XX  
**Estado**: Análisis post-implementación parcial

## Resumen Ejecutivo

De las **23 referencias** identificadas en el plan, se han completado **15 correcciones confirmadas** y quedan **8 referencias pendientes** de verificación o corrección.

### Desglose por Estado
- ✅ **Completadas y verificadas**: 15 referencias
- ❓ **Pendientes de verificación (texto puede no existir)**: 3 referencias
- 📋 **Referencias en tablas (tabla existe)**: 5 referencias
  - ✅ 4 ya corregidas (Triple Convergencia - línea 100, Grupo C₃ - línea 53, Estructura matriz - línea 82, Corresp. Mersenne - línea 71)
  - ❓ 1 requiere verificación (Espiral Áurea - línea 68)

## Referencias Completadas ✅

### methods.tex
1. ✅ **Label creado**: `\label{subsec:espacios-adjuntos}` en línea 204
2. ✅ **§3.2.2**: Agregada referencia `\dref{def:fases-componentes}` en `prop:separacion-angular` (línea 692)
3. ✅ **§3.2.1**: Agregada referencia `\dref{def:magnitudes-tripartitas}` en `prop:preservacion-estructura` (línea 1274)
4. ✅ **§3.2.3**: Cambiada referencia a `\dref{def:componentes-PCF}` en `constr:cilindro-vertices` (línea 806)
5. ✅ **§3.5.2**: Corregida referencia a `\dref{def:modulo-topologico}` en results.tex línea 362

### results.tex
6. ✅ **§IX.0/§IX.1**: Agregada referencia `\ref{mersenne}` en línea 589
7. ✅ **§IX.2**: Agregada referencia `\ref{subsec:prediccion-ceros}` en línea 1092

### discussion.tex
8. ✅ **Label creado**: `\label{subsec:prediccion-ceros}` en línea 61

### appendices.tex (Tabla de Verificaciones)
9. ✅ **§3.2.6**: Agregada referencia `\autoref{prop:separacion-angular}` en línea 53 (Grupo C₃)
10. ✅ **§3.7.4**: Agregada referencia `\autoref{prop:funciones-escala-hilbert}` en línea 82 (Estructura matriz)
11. ✅ **§9.2**: Agregada referencia `\autoref{fig:sintesis_unificada}` en línea 71 (Corresp. Mersenne)

## Referencias Pendientes por Archivo

### methods.tex

#### 1. §2: Plano complejo como espacio de módulos
- **Ocurrencias en paper.md**: Líneas 111, 1015
- **Contexto paper.md línea 1015**: "**Conexión con §2** (Espacio de parámetros de curvas elípticas)"
- **Label existente**: `sec:plano-complejo-modulos`
- **Ubicación en .tex**: methods.tex línea 1421 (`obs:conexion-curvas-elipticas`)
- **Estado**: ✅ **YA CORREGIDO** - La observación ya tiene `\ref{sec:plano-complejo-modulos}` en el título de la observación. El texto del paper.md menciona "Conexión con §2" pero en .tex ya está referenciado correctamente.
- **Acción requerida**: Ninguna - ya está corregido

#### 2. §2.6: Espacios paramétricos adjuntos
- **Ocurrencias en paper.md**: Línea 112
- **Label creado**: `subsec:espacios-adjuntos` ✅
- **Ubicación en .tex**: introduction.tex línea 78
- **Estado**: ✅ **YA CORREGIDO** - Ya corregido en introduction.tex línea 78 con `\autoref{subsec:espacios-adjuntos}`
- **Acción requerida**: Ninguna - ya está corregido

#### 3. §3.1: Axiomas fundamentales
- **Ocurrencias en paper.md**: Línea 115
- **Label existente**: `subsec:axiomas`
- **Ubicación en .tex**: 
  - methods.tex línea 409 (definición de la subsección)
  - introduction.tex línea 78: ✅ Ya referenciado con `\autoref{subsec:axiomas}`
- **Estado**: ✅ **YA CORREGIDO** - Ya referenciado en introduction.tex línea 78
- **Acción requerida**: Ninguna - ya está corregido

#### 4. §3.2: Construcción desde el módulo
- **Ocurrencias en paper.md**: Líneas 116, 485, 1748
- **Contexto paper.md línea 485**: "**Prueba**. La construcción de §3.2 proporciona realización explícita."
- **Contexto paper.md línea 1748**: "Todos los parámetros (M_PCF, φ, ε₀) están determinados por la estructura tripartita del operador establecida en §3.2."
- **Label existente**: `subsec:construccion-modulo`
- **Ubicación en .tex**: 
  - methods.tex línea 543 (proof de `thm:consistencia`): ✅ "La construcción de \ref{subsec:construccion-modulo} proporciona realización explícita."
  - results.tex: Buscar texto sobre "estructura tripartita establecida" o "parámetros determinados"
- **Estado**: 
  - ✅ methods.tex línea 543 ya tiene referencia
  - ❓ **PENDIENTE**: Buscar en results.tex texto equivalente a "estructura tripartita establecida en §3.2"
- **Acción requerida**: Buscar en results.tex texto sobre "estructura tripartita establecida" o "parámetros determinados" y agregar `\ref{subsec:construccion-modulo}` si existe

#### 5. §3.2.6: Separación angular
- **Ocurrencias en paper.md**: Línea 3127 (en tabla de verificaciones)
- **Label existente**: `prop:separacion-angular`
- **Ubicación**: methods.tex línea 691
- **Estado**: La proposición existe pero no se referencia desde tablas
- **Acción requerida**: Si hay tablas en .tex que mencionen "Grupo C₃" o "Separación angular", agregar `\pref{prop:separacion-angular}`

#### 6. §3.7.4: Funciones de escala en Hilbert
- **Ocurrencias en paper.md**: Línea 3137 (en tabla de verificaciones)
- **Label existente**: `prop:funciones-escala-hilbert`
- **Ubicación**: methods.tex línea 2104
- **Estado**: La proposición existe pero no se referencia desde tablas
- **Acción requerida**: Si hay tablas en .tex que mencionen "Funciones de escala" o "Estructura matriz", agregar `\pref{prop:funciones-escala-hilbert}`

### results.tex

#### 7. §4: Necesidad del toro complejo
- **Ocurrencias en paper.md**: Línea 120
- **Contexto**: Necesita verificación del mapeo correcto
- **Labels posibles**: `subsec:toro-lattice`, `convergencia`
- **Estado**: Requiere búsqueda del contexto exacto en paper.md línea 120
- **Acción requerida**: Leer paper.md línea 120, identificar texto equivalente en .tex, determinar label correcto

#### 8. §5: Convergencia espectral
- **Ocurrencias en paper.md**: Línea 123
- **Label existente**: `convergencia`
- **Ubicación**: results.tex línea 2
- **Estado**: La sección existe pero necesita verificar si hay texto que mencione "§5" sin referencia
- **Acción requerida**: Buscar menciones de "Convergencia espectral" o "§5" que deberían referenciar `\ref{convergencia}`

#### 9. §6: Invariancia exacta
- **Ocurrencias en paper.md**: Línea 126
- **Label existente**: `invariancia`
- **Ubicación**: results.tex línea 64
- **Estado**: La sección existe pero necesita verificar si hay texto que mencione "§6" sin referencia
- **Acción requerida**: Buscar menciones de "Invariancia modular" o "§6" que deberían referenciar `\ref{invariancia}`

#### 10. §7: Dimensión de Hausdorff
- **Ocurrencias en paper.md**: Línea 129
- **Label existente**: `hausdorff`
- **Ubicación**: results.tex línea 123
- **Estado**: La sección existe pero necesita verificar si hay texto que mencione "§7" sin referencia
- **Acción requerida**: Buscar menciones de "Dimensión de Hausdorff" o "§7" que deberían referenciar `\ref{hausdorff}`

#### 11. §8: Coherencia en tres espacios
- **Ocurrencias en paper.md**: Línea 132
- **Label existente**: `triple`
- **Ubicación**: results.tex línea 173
- **Estado**: La sección existe pero necesita verificar si hay texto que mencione "§8" sin referencia
- **Acción requerida**: Buscar menciones de "Triple convergencia" o "§8" que deberían referenciar `\ref{triple}`

#### 12. §8.1: Triple convergencia
- **Ocurrencias en paper.md**: Línea 3143 (en tabla de verificaciones)
- **Label existente**: `thm:triple-convergencia`
- **Ubicación**: results.tex línea 177
- **Estado**: El teorema existe pero no se referencia desde tablas
- **Acción requerida**: Si hay tablas en .tex que mencionen "Triple Convergencia", agregar `\tref{thm:triple-convergencia}`

### discussion.tex

#### 13. §9: Números de Mersenne
- **Ocurrencias en paper.md**: Línea 135
- **Label existente**: `discussion`
- **Ubicación**: discussion.tex línea 1
- **Estado**: La sección existe pero necesita verificar si hay texto que mencione "§9" sin referencia
- **Acción requerida**: Buscar menciones de "Números de Mersenne" o "§9" que deberían referenciar `\ref{discussion}`

#### 14. §9.1: Espiral Áurea
- **Ocurrencias en paper.md**: Línea 3132 (en tabla de verificaciones)
- **Contexto**: "Geometría | Espiral Áurea | ✓ | §9.1"
- **Labels posibles**: `discussion`, buscar subsección específica sobre espiral áurea
- **Ubicación**: methods.tex línea 1721 menciona "Espiral áurea"
- **Estado**: Necesita identificar si hay subsección específica o usar `discussion`
- **Acción requerida**: Buscar subsección sobre "Espiral áurea" o usar `\ref{discussion}` si no existe subsección específica

#### 15. §9.2: Correspondencia Mersenne
- **Ocurrencias en paper.md**: Línea 3133 (en tabla de verificaciones)
- **Contexto**: "Binaria | Corresp. Mersenne | ✓ | §9.2"
- **Label sugerido**: `fig:sintesis_unificada` (según plan)
- **Ubicación**: discussion.tex línea 122
- **Estado**: La figura existe pero necesita verificar si es la referencia correcta
- **Acción requerida**: Verificar si `fig:sintesis_unificada` es la referencia correcta o si debe ser `\ref{mersenne}`

#### 16. §IX.0: Correspondencia Mersenne
- **Ocurrencias en paper.md**: Líneas 2623, 3044
- **Contexto línea 2623**: "Los dos descubrimientos principales—correspondencia con números de Mersenne (§IX.0-IX.1)"
- **Label existente**: `mersenne`
- **Ubicación**: results.tex línea 1092
- **Estado**: ✅ Ya corregido en results.tex línea 1092
- **Acción requerida**: Verificar si hay otras menciones

#### 17. §IX.1: Correspondencia Mersenne
- **Ocurrencias en paper.md**: Líneas 1984, 2269
- **Contexto línea 1984**: "Esta sección establece el puente entre la construcción geométrica del operador PCF (§3.3) y su correspondencia con números de Mersenne (§IX.1)"
- **Contexto línea 2269**: "Para σ=9, la verificación empírica (§IX.1) demuestra que p=31 proporciona:"
- **Label existente**: `mersenne` o `fig:correspondencia_logaritmica`
- **Ubicación**: 
  - results.tex línea 589: ✅ Ya corregido
  - Buscar línea 2269 equivalente en .tex
- **Estado**: Parcialmente corregido
- **Acción requerida**: Buscar texto sobre "verificación empírica" en results.tex y agregar `\ref{mersenne}` o `\ref{fig:correspondencia_logaritmica}` según contexto

#### 18. §IX.2: Predicción de ceros
- **Ocurrencias en paper.md**: Líneas 2623, 2647, 3045
- **Contexto línea 2647**: "**Conclusión de §IX.2:** La correspondencia geométrica |Ω|=1/2 ↔ Re(s)=1/2..."
- **Contexto línea 3045**: "2. **Analítica:** Predicción de ceros de ζ(s) con precisión 99.70% y mejora asintótica O(1/√log n), verificada hasta n ~ 10¹⁰ (§IX.2)"
- **Label existente**: `subsec:prediccion-ceros` ✅
- **Ubicación**: 
  - results.tex línea 1092: ✅ Ya corregido
  - Buscar otras menciones
- **Estado**: Parcialmente corregido
- **Acción requerida**: Buscar texto sobre "Predicción de ceros" o "Conclusión" en discussion.tex y agregar `\ref{subsec:prediccion-ceros}`

## Análisis de Tablas de Verificaciones

Muchas referencias faltantes están en **tablas de verificaciones** que pueden no existir en los archivos .tex. Estas tablas están en paper.md pero pueden no haberse migrado completamente a .tex.

### Referencias en Tablas (paper.md líneas 3115-3134)
- §3.2.6: Grupo C₃ (línea 3127)
- §3.7.4: Estructura matriz (línea 3137)
- §8.1: Triple Convergencia (línea 3143)
- §9.1: Espiral Áurea (línea 3132)
- §9.2: Corresp. Mersenne (línea 3133)

**Acción requerida**: Verificar si estas tablas existen en .tex. Si no existen, estas referencias no requieren corrección en .tex.

## Priorización de Correcciones

### Alta Prioridad (Referencias en texto principal - VERIFICAR EXISTENCIA)
1. **§3.2 en results.tex**: "estructura tripartita establecida en §3.2" (línea 1748 paper.md)
   - **Estado**: ❓ Texto equivalente no encontrado en results.tex
   - **Acción**: Verificar si el texto existe. Si no existe, no requiere corrección.

2. **§IX.1 en results.tex**: "verificación empírica (§IX.1)" (línea 2269 paper.md)
   - **Estado**: ❓ Texto equivalente no encontrado en results.tex
   - **Acción**: Verificar si el texto existe. Si no existe, no requiere corrección.

3. **§IX.2 en discussion.tex**: "Conclusión de §IX.2" (línea 2647 paper.md)
   - **Estado**: ❓ Texto equivalente no encontrado en discussion.tex
   - **Acción**: Verificar si el texto existe. Si no existe, no requiere corrección.

### Media Prioridad (Verificar contexto - PROBABLEMENTE YA CORREGIDAS)
4. **§4**: "Necesidad del toro complejo" (paper.md línea 120)
   - **Estado**: ✅ Ya referenciado en introduction.tex línea 78 con `\autoref{subsec:toro-lattice}`
   - **Acción**: Verificado - ya está corregido

5. **§5, §6, §7, §8**: Secciones principales
   - **Estado**: ✅ Ya referenciadas en introduction.tex línea 80 con `\autoref{convergencia}`, `\autoref{invariancia}`, `\autoref{hausdorff}`, `\autoref{triple}`
   - **Acción**: Verificado - ya están corregidas

6. **§9.1**: Espiral Áurea
   - **Estado**: ❓ Mencionado en methods.tex línea 1721 pero sin referencia específica
   - **Acción**: Verificar si necesita referencia a subsección específica o si `\ref{discussion}` es suficiente

### Baja Prioridad (Referencias en tablas - VERIFICAR EXISTENCIA DE TABLAS)
7. **§3.2.6, §3.7.4, §8.1, §9.1, §9.2**: Referencias en tablas de verificaciones
   - **Estado**: ❓ Tablas de verificaciones no encontradas en .tex
   - **Acción**: 
     - Verificar si existe `app:ttt` mencionado en introduction.tex
     - Si las tablas no existen en .tex, estas referencias no requieren corrección

## Notas Importantes

1. **Referencias en paper.md vs .tex**: Muchas referencias § están en paper.md pero el texto equivalente en .tex puede no mencionarlas explícitamente. Solo se deben agregar referencias donde el texto en .tex mencione el concepto.

2. **Tablas de verificaciones**: Las tablas en paper.md (líneas 3115-3134) pueden no existir en .tex. Verificar antes de agregar referencias.

3. **Contexto suficiente**: Al buscar texto equivalente, usar contexto suficiente para evitar falsos positivos.

4. **Macros correctos**: Recordar usar `\dref{}` para definiciones, `\pref{}` para proposiciones, `\tref{}` para teoremas, `\ref{}` para secciones.

## Verificación de Tablas de Verificaciones

### Estado de `app:ttt`
- **Mencionado en**: introduction.tex línea 80: `\autoref{app:ttt}`
- **Ubicación**: `src/supplementary/appendices.tex` ✅ **EXISTE**
- **Estado**: La tabla existe y ya tiene referencias, pero algunas pueden necesitar corrección según el plan

### Análisis de Referencias en Tabla (appendices.tex)

#### 13. Grupo $C_3$ (Línea 53) - Corresponde a §3.2.6
- **Estado actual**: `\autoref{def:matriz-PCF}`, `\autoref{prop:propiedades-matriz}`, y `\autoref{prop:separacion-angular}`
- **Referencia esperada según plan**: `\pref{prop:separacion-angular}`
- **Análisis**: ✅ **CORREGIDO** - Se agregó `\autoref{prop:separacion-angular}` a la línea 53
- **Acción requerida**: Ninguna - ya está corregido

#### 23. Estructura matriz (Línea 82) - Corresponde a §3.7.4
- **Estado actual**: `\autoref{def:matriz-PCF}`, `\autoref{prop:propiedades-matriz}`, y `\autoref{prop:funciones-escala-hilbert}`
- **Referencia esperada según plan**: `\pref{prop:funciones-escala-hilbert}`
- **Análisis**: ✅ **CORREGIDO** - Se agregó `\autoref{prop:funciones-escala-hilbert}` a la línea 82
- **Acción requerida**: Ninguna - ya está corregido

#### 29. Triple Convergencia (Línea 100) - Corresponde a §8.1
- **Estado actual**: `\autoref{thm:triple-convergencia}` y `\autoref{thm:coherencia-convergencias}`
- **Referencia esperada según plan**: `\tref{thm:triple-convergencia}`
- **Análisis**: ✅ **YA CORREGIDO** - Ya tiene `\autoref{thm:triple-convergencia}` que es equivalente
- **Acción requerida**: Ninguna - ya está corregido

#### 18. Espiral Áurea (Línea 68) - Corresponde a §9.1
- **Estado actual**: `\autoref{mersenne}` y `\autoref{prop:modulo-proyectado}`
- **Referencia esperada según plan**: `\ref{discussion}` o subsección específica
- **Análisis**: Ya tiene `\autoref{mersenne}` que es correcto. Podría agregarse referencia más específica si existe subsección sobre espiral áurea
- **Acción requerida**: Verificar si existe subsección específica sobre espiral áurea o si `\autoref{mersenne}` es suficiente

#### 19. Corresp. Mersenne (Línea 71) - Corresponde a §9.2
- **Estado actual**: `\autoref{prop:coincidencia-mersenne}` y `\autoref{fig:sintesis_unificada}`
- **Referencia esperada según plan**: `\ref{fig:sintesis_unificada}` o `\ref{mersenne}`
- **Análisis**: ✅ **CORREGIDO** - Se agregó `\autoref{fig:sintesis_unificada}` a la línea 71
- **Acción requerida**: Ninguna - ya está corregido

## Resumen Final de Estado

### Referencias Completamente Corregidas ✅ (15)
1. ✅ Label `subsec:espacios-adjuntos` creado
2. ✅ §2: Ya referenciado en `obs:conexion-curvas-elipticas`
3. ✅ §2.6: Ya referenciado en introduction.tex
4. ✅ §3.1: Ya referenciado en introduction.tex
5. ✅ §3.2.2: Agregado `\dref{def:fases-componentes}`
6. ✅ §3.2.1: Agregado `\dref{def:magnitudes-tripartitas}`
7. ✅ §3.2.3: Cambiado a `\dref{def:componentes-PCF}`
8. ✅ §3.5.2: Corregido a `\dref{def:modulo-topologico}`
9. ✅ §IX.0/§IX.1: Agregado `\ref{mersenne}`
10. ✅ §IX.2: Agregado `\ref{subsec:prediccion-ceros}` y label creado
11. ✅ §4, §5, §6, §7, §8: Ya referenciadas en introduction.tex
12. ✅ §8.1: Ya tiene `\autoref{thm:triple-convergencia}` en tabla (línea 100)
13. ✅ §3.2.6: Agregado `\autoref{prop:separacion-angular}` en tabla (línea 53)
14. ✅ §3.7.4: Agregado `\autoref{prop:funciones-escala-hilbert}` en tabla (línea 82)
15. ✅ §9.2: Agregado `\autoref{fig:sintesis_unificada}` en tabla (línea 71)

### Referencias Pendientes de Verificación (Texto puede no existir en .tex)
- ❓ **§3.2 en results.tex**: "estructura tripartita establecida en §3.2" - Texto no encontrado
- ❓ **§IX.1 en results.tex**: "verificación empírica (§IX.1)" - Texto no encontrado  
- ❓ **§IX.2 en discussion.tex**: "Conclusión de §IX.2" - Texto no encontrado

### Referencias en Tabla de Verificaciones (appendices.tex)
- ✅ **§3.2.6 (Línea 53)**: **CORREGIDO** - Agregado `\autoref{prop:separacion-angular}` a "Grupo $C_3$"
- ✅ **§3.7.4 (Línea 82)**: **CORREGIDO** - Agregado `\autoref{prop:funciones-escala-hilbert}` a "Estructura matriz"
- ❓ **§9.1 (Línea 68)**: Verificar si necesita referencia adicional a "Espiral Áurea" (ya tiene `\autoref{mersenne}`)
- ✅ **§9.2 (Línea 71)**: **CORREGIDO** - Agregado `\autoref{fig:sintesis_unificada}` a "Corresp. Mersenne"

## Acciones Recomendadas

### Prioridad Alta
1. ✅ **COMPLETADO**: Referencias en tabla corregidas:
   - ✅ Línea 53: Agregado `\autoref{prop:separacion-angular}` a "Grupo $C_3$"
   - ✅ Línea 82: Agregado `\autoref{prop:funciones-escala-hilbert}` a "Estructura matriz"
   - ✅ Línea 71: Agregado `\autoref{fig:sintesis_unificada}` a "Corresp. Mersenne"

### Prioridad Media
2. **Verificar referencias en tabla**:
   - ❓ Línea 68: Verificar si necesita referencia adicional a "Espiral Áurea" (ya tiene `\autoref{mersenne}`)

### Prioridad Baja
3. **Confirmar texto faltante**: 
   - Verificar que el texto "estructura tripartita establecida en §3.2", "verificación empírica (§IX.1)", y "Conclusión de §IX.2" no existe en .tex
   - Si no existe, marcar como "No requiere corrección (texto no migrado del paper.md)"

