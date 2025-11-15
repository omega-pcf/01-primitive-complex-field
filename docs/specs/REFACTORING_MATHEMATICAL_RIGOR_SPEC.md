# Spec: Refactorización para Rigor Matemático y Concisión

**Objetivo**: Eliminar redundancias REALES y mejorar concisión sin introducir artificialidad. Mantener el flujo natural del español académico.

**Principio Fundamental**: 
- ✅ Eliminar redundancias REALES (checkmarks, verificaciones obvias, pasos intermedios innecesarios)
- ✅ Mantener lenguaje natural válido en español académico
- ✅ NO introducir artificialidad ni "legalese" matemático
- ✅ Los términos técnicos densos están bien si están bien usados, pero NO artificialidad
- ❌ NO cambiar frases naturales válidas por versiones más "formales" que interrumpen el flujo
- ✅ Estandarizar títulos de proofs: si "Por" suena estándar, mantenerlo, pero TODOS deben seguir el mismo patrón

---

## ⚠️ PROBLEMA PRINCIPAL IDENTIFICADO

### Títulos de Proofs: Agregar "Por" Innecesariamente

**Problema:** En el diff se están agregando "Por" en títulos de proofs donde no tiene sentido:
- ❌ `[Por construcción]` - "Por" no aporta, debería ser `[Construcción]`
- ❌ `[Por sustitución]` - "Por" no aporta, debería ser `[Sustitución]`
- ❌ `[Por cálculo directo]` - "Por" no aporta, debería ser `[Cálculo directo]`

**Criterio:** Solo usar "Por" cuando realmente indica un método de demostración estándar:
- ✅ `[Por contradicción]` - método estándar
- ✅ `[Por inducción]` - método estándar
- ✅ `[Por definición]` - razón específica
- ❌ `[Por construcción]` → `[Construcción]` - técnica, no método
- ❌ `[Por sustitución]` → `[Sustitución]` - técnica, no método
- ❌ `[Por cálculo directo]` → `[Cálculo directo]` - proceso, no método

**Análisis completo:** Ver `docs/analysis/ANALISIS_TITULOS_PROOFS.md`

---

## 1. Eliminación de Checkmarks y Verificaciones Redundantes

### Problema Identificado
Los checkmarks (✓) son vestigios de un estilo pedagógico que no corresponde a papers formales. Las verificaciones numéricas deben integrarse en el texto o eliminarse si son triviales.

### Archivos Afectados
- `src/chapters/methods.tex:1299` - Verificaciones con checkmarks en proposición de vértices
- `src/chapters/results.tex:946,950` - Checkmarks en verificaciones numéricas
- `src/chapters/methods.tex:2109` - Checkmark en tabla (evaluar si es necesario)

### Acciones
1. **methods.tex:1299**: Eliminar checkmarks y reformular como verificación formal:
   ```latex
   % Antes:
   Verificación: $z_C = \varphi \cdot 2.598 = 4.204$ $\checkmark$, $z_F = \varphi \cdot (-2.598) = -4.204$ $\checkmark$
   
   % Después:
   Se verifica que $z_C = \varphi \cdot 2.598 = 4.204$ y $z_F = \varphi \cdot (-2.598) = -4.204$, confirmando la regla de acoplamiento $z = \varphi y$.
   ```

2. **results.tex:946,950**: Integrar verificaciones numéricas en el texto sin checkmarks:
   ```latex
   % Antes:
   $\to$ Razón: $7/4.854 = 1.442 \approx \lambda$ \checkmark%
   
   % Después:
   La razón $7/4.854 = 1.442 \approx \lambda$ confirma la correspondencia estructural.
   ```

3. **methods.tex:2109**: Evaluar si el checkmark en tabla es necesario o puede reemplazarse por "Sí" en texto.

---

## 2. Estandarización de Títulos de Proofs

### Problema Identificado
Los títulos de proofs tienen inconsistencias: algunos tienen "Por" y otros no, sin criterio claro. Necesitamos estandarizar TODOS siguiendo un criterio consistente.

### Regla de Estandarización: Usar "Por" para Métodos Estándar

**Criterio:** Si "Por" suena estándar en matemáticas, mantenerlo. Pero TODOS deben seguir el mismo patrón.

**Métodos estándar que usan "Por" (MANTENER):**
- ✅ `[Por construcción]` - estándar en matemáticas
- ✅ `[Por sustitución]` - estándar en matemáticas
- ✅ `[Por contradicción]` - método estándar
- ✅ `[Por inducción]` - método estándar
- ✅ `[Por definición]` - razón estándar
- ✅ `[Por hipótesis]` - razón estándar
- ✅ `[Por cálculo directo]` - mantener "Por" para consistencia
- ✅ `[Por verificación directa]` - mantener "Por" para consistencia
- ✅ `[Por aplicación directa]` - mantener "Por" para consistencia

**Estandarizar los que NO tienen "Por" (AGREGAR "Por" para consistencia):**
- ❌ `[Cálculo directo]` → `[Por cálculo directo]` (líneas 625, 923, 1633)
- ❌ `[Esquema de demostración]` → mantener sin "Por" (es diferente, no es método)

### Archivos Afectados
- `src/chapters/methods.tex` - 16 proofs: estandarizar 3 que no tienen "Por"
- `src/chapters/results.tex` - 6 proofs: todos ya tienen "Por" o son casos especiales

### Acciones
1. Revisar todos los títulos de proofs
2. Agregar "Por" a los que no lo tienen para mantener consistencia con métodos estándar
3. Estandarizar formato: `[Por método/técnica]` para métodos estándar
4. Excepciones: títulos que no son métodos (ej: `[Esquema de demostración]`) se mantienen sin "Por"

---

## 3. Condensación de Demostraciones "Por Sustitución Directa"

### Problema Identificado
Las demostraciones que solo dicen "Por sustitución directa" sin mostrar el cálculo son inadecuadas para audiencia experta. Deben mostrar la sustitución o eliminarse si es trivial.

### Archivos Afectados
- `src/chapters/methods.tex:1837` - Prueba que solo menciona sustitución sin mostrarla
- `src/chapters/results.tex:67,98,112` - Varias pruebas similares

### Acciones
1. **methods.tex:1837**: Mostrar la sustitución o eliminar la prueba si es trivial:
   ```latex
   % Antes:
   \begin{proof}[Sustitución directa]
   Por sustitución directa de definiciones (\dref{def:fases-componentes} y §\ref{subsubsec:acoplamiento-optimo}).
   \end{proof}
   
   % Después (opción 1 - mostrar sustitución):
   \begin{proof}[Por sustitución]
   Sustituyendo $\arg(\Omega) = 3\arg(z) + \pi\varepsilon(\sigma)$ y $\log(\varepsilon(\sigma)) = \log(\varepsilon_0) + \sigma\log(\varphi)$ en la ecuación de acoplamiento se obtiene directamente el resultado.
   \end{proof}
   
   % Después (opción 2 - eliminar si trivial):
   % Eliminar proof completamente si la sustitución es inmediata y obvia
   ```

2. **results.tex**: Revisar cada prueba "Por sustitución directa" y aplicar el mismo criterio.

---

## 4. Condensación de Demostraciones "Por Construcción"

### Problema Identificado
Las demostraciones "Por construcción" a menudo tienen pasos intermedios obvios que pueden condensarse siguiendo el patrón aplicado a la demostración de hermiticidad del operador integral.

### Archivos Afectados
- `src/chapters/methods.tex:554,645,1067,1110,1244,1383` - Múltiples pruebas "Por construcción"

### Acciones
1. **Revisar cada demostración** y aplicar el principio:
   - Si los pasos intermedios son obvios para audiencia experta, condensarlos
   - Mantener solo los pasos esenciales que establecen la conexión lógica
   - Eliminar explicaciones verbales redundantes

2. **Ejemplo de patrón a seguir** (basado en hermiticidad del operador integral):
   ```latex
   % Patrón condensado exitoso:
   \begin{proof}[Por cálculo directo]
   Por (\ref{thm:referencia}), condición X. Para objetos Y, Z:
   \begin{align*}
   Expresión_1 &= Paso_1 \\
   &= Paso_2 \\
   &= Resultado
   \end{align*}
   \end{proof}
   ```

---

## 5. Eliminación de Frases Redundantes REALES

### Problema Identificado
Solo eliminar redundancias REALES. "Por tanto" es válido en español académico y NO debe cambiarse a "Se concluye que" o "lo cual establece" - eso introduce artificialidad.

### ⚠️ ADVERTENCIA CRÍTICA
**NO hacer cambios que introduzcan artificialidad:**
- ❌ Convertir frases naturales válidas a "legalese" matemático innecesario
- ❌ Agregar explicaciones que interrumpen el flujo natural del español
- ❌ Cambiar significado innecesariamente
- ✅ "Por tanto" y "Se concluye que" son ambos válidos - usar el que fluya mejor

### Acciones CORRECTAS
1. **Solo eliminar "Por tanto"** cuando es REALMENTE redundante y la conexión es inmediata:
   ```latex
   % Solo si es realmente redundante:
   % Antes: Se tiene X. Por tanto, Y. (donde Y es inmediato de X)
   % Después: Se tiene X, luego Y.
   ```

2. **NO cambiar lenguaje natural válido:**
   ```latex
   % "Por tanto" es válido - NO cambiar:
   ✅ Por tanto, $\psi$ y $\pi$ son mutuamente inversas.
   ❌ Por tanto, $\psi$ y $\pi$ son mutuamente inversas en sus respectivos dominios.
   ❌ Se concluye que $\psi$ y $\pi$ son mutuamente inversas.
   ```

3. **Eliminar solo redundancias REALES:**
   ```latex
   % Solo si es realmente redundante:
   % Antes: X satisface Y. Esto implica directamente que Z. (donde Z es obvio)
   % Después: X satisface Y, luego Z.
   ```

---

## 6. Mejora de Títulos: Concisión SIN Artificialidad

### Problema Identificado
Algunos títulos son demasiado largos. PERO: NO hacer títulos más formales y largos que interrumpen la lectura.

### ⚠️ ADVERTENCIA CRÍTICA
**Los títulos largos y formales están BIEN si son precisos y densos en información.**
- ✅ Títulos largos y formales son correctos si capturan el contenido esencial
- ✅ No hay problema con títulos > 60 caracteres si son precisos
- ❌ Solo evitar títulos que sean artificiales o que interrumpan el flujo

### Criterios de Evaluación CORRECTOS
- **Concisión**: Títulos cortos y claros
- **Precisión**: Deben capturar el contenido esencial
- **Naturalidad**: Lenguaje natural válido, NO artificialidad

### Acciones CORRECTAS
1. **Solo condensar títulos REALMENTE largos (> 80 caracteres)**:
   ```latex
   % Solo si es realmente largo y puede condensarse sin perder claridad:
   % Antes: [Separación conceptual entre vértices geométricos y componentes funcionales]
   % Después: [Separación entre vértices geométricos y componentes funcionales]
   ```

2. **Mantener títulos concisos y naturales:**
   ```latex
   ✅ [Invariancia modular exacta]
   ✅ [Contraste con cilindro infinito]
   ✅ [Equivalencia y privilegio de perspectiva]
   ```

3. **NO hacer títulos más formales innecesariamente:**
   ```latex
   ❌ [Constancia del módulo topológico bajo escalamiento]
   ❌ [Separación vertical cilíndrica versus igualdad radial toroidal]
   ```

---

## 7. Principios de Aplicación CORRECTOS

### Reglas de Oro
1. **Eliminar solo redundancias REALES**: No cambiar lenguaje natural válido
2. **Mantener flujo natural del español**: No introducir artificialidad
3. **DRY solo para repeticiones REALES**: No eliminar contenido valioso que aporta contexto
4. **Términos técnicos densos están bien**: Si están bien usados, no son artificialidad
5. **Concisión sin sacrificar claridad**: Eliminar solo lo realmente innecesario

### ⚠️ Criterios de Decisión CORRECTOS
Antes de cada cambio, preguntar:

1. **¿El cambio mejora claridad?** → Si NO, no hacerlo
2. **¿El cambio mantiene flujo natural del español?** → Si NO, no hacerlo
3. **¿El cambio elimina redundancia REAL?** → Si NO, no hacerlo
4. **¿El cambio preserva contenido valioso?** → Si NO, no hacerlo
5. **¿El cambio introduce artificialidad?** → Si SÍ, NO hacerlo

### Ejemplos de Cambios INCORRECTOS (introducen artificialidad)
- ❌ Convertir frases naturales válidas a "legalese" matemático innecesario
- ❌ Agregar explicaciones que interrumpen el flujo natural del español
- ❌ Cambiar significado innecesariamente (ej: "Resolución de contradicción" → "Independencia de propiedades")
- ❌ Eliminar párrafos que aportan contexto valioso (reduce riqueza conceptual)
- ❌ Cambios de estilo innecesarios que no mejoran claridad

### Ejemplos de Cambios CORRECTOS (eliminan redundancias reales)
- ✅ Eliminar checkmarks (✓) de verificaciones numéricas
- ✅ Condensar demostraciones con pasos intermedios obvios
- ✅ Eliminar frases realmente redundantes como "Esto implica directamente que" cuando la implicación es obvia

---

## 8. Plan de Implementación CORREGIDO

### Fase 1: Estandarización de Títulos de Proofs (Prioridad CRÍTICA) ⚠️
- [ ] Revisar todos los títulos de proofs en methods.tex (16 proofs)
- [ ] Revisar todos los títulos de proofs en results.tex (6 proofs)
- [ ] Agregar "Por" a los que no lo tienen para consistencia (líneas 625, 923, 1633 en methods.tex)
- [ ] Estandarizar formato: `[Por método/técnica]` para métodos estándar
- [ ] Mantener sin "Por" solo casos especiales como `[Esquema de demostración]`
- [ ] Ver análisis completo en `docs/analysis/ANALISIS_TITULOS_PROOFS.md`

### Fase 2: Eliminación de Checkmarks (Prioridad Alta) ✅
- [ ] methods.tex:1299
- [ ] results.tex:946,950
- [ ] methods.tex:2109 (evaluar)

### Fase 3: Condensación de Demostraciones (Prioridad Alta) ✅
- [ ] methods.tex:1837
- [ ] results.tex:67,98,112
- [ ] Revisar demostraciones "Por construcción" con pasos REALMENTE obvios

### Fase 4: REVERTIR Cambios que Introducen Artificialidad (Prioridad Media) ⚠️
- [ ] Revisar diff completo para identificar cambios que introducen artificialidad
- [ ] Revertir cambios que convierten frases naturales a "legalese" innecesario
- [ ] Revertir cambios que alteran significado innecesariamente
- [ ] Restaurar párrafos eliminados que aportan contexto valioso

### Fase 5: Eliminación de Redundancias REALES (Prioridad Media)
- [ ] Buscar y eliminar SOLO "Por tanto" REALMENTE redundantes (muy pocos casos)
- [ ] Eliminar SOLO "Esto implica directamente" cuando la implicación es REALMENTE obvia

### Fase 6: Mejora de Títulos (Prioridad Baja)
- [ ] Revisar SOLO títulos > 80 caracteres (no 60)
- [ ] Condensar SOLO si puede hacerse sin perder claridad
- [ ] NO hacer títulos más formales innecesariamente

---

## 9. Métricas de Éxito

- **Reducción de longitud**: Demostraciones condensadas en ~30-50% menos líneas
- **Eliminación de redundancias**: 0 checkmarks, 0 frases redundantes obvias
- **Mejora de densidad**: Títulos más descriptivos y concisos
- **Mantenimiento de rigor**: Todas las demostraciones siguen siendo matemáticamente rigurosas

---

## 10. Referencias

- Patrón exitoso aplicado: `methods.tex:2148-2155` (demostración de hermiticidad del operador integral)
- Style Guide: `docs/style/STYLE_GUIDE.md`
- Principios de programación aplicados: DRY, concisión, formalidad rigurosa

