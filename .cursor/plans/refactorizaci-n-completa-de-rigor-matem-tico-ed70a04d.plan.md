<!-- ed70a04d-608d-4282-81a1-65f2b0fbeebc 81b88326-42fd-4d00-9dc6-dc8ab20d7148 -->
# Plan: Refactorización Completa de Rigor Matemático

## Objetivo

Aplicar sistemáticamente todas las mejoras del spec `REFACTORING_MATHEMATICAL_RIGOR_SPEC.md` a todos los archivos en `src/chapters/`, mejorando concisión, rigor y densidad informativa para audiencia experta.

## Archivos a Revisar

- `src/chapters/methods.tex` (146 estructuras matemáticas)
- `src/chapters/results.tex` (49 estructuras matemáticas)
- `src/chapters/discussion.tex` (3 estructuras matemáticas)
- `src/chapters/formal.tex`, `src/chapters/introduction.tex`, `src/chapters/abstract.tex` (revisión menor)

## Fases de Implementación

### Fase 1: Revisión y Condensación de Demostraciones (Prioridad Alta)

#### 1.1 Demostraciones "Por Sustitución Directa" sin cálculo explícito

**Archivos afectados:**

- `src/chapters/results.tex:67,98,112` - 3 demostraciones
- `src/chapters/methods.tex:616,1690` - 2 demostraciones

**Acción:** Para cada una:

- Si la sustitución es trivial → mostrar cálculo explícito en 1-2 líneas
- Si es inmediata → eliminar proof completamente
- Mantener solo si el cálculo aporta claridad

#### 1.2 Demostraciones "Por Construcción" con pasos intermedios obvios

**Archivos afectados:**

- `src/chapters/methods.tex:554,645,1067,1109,1242,1379` - 6 demostraciones

**Acción:** Revisar cada una y aplicar patrón de condensación:

- Eliminar pasos intermedios obvios
- Mantener solo conexión lógica esencial
- Seguir patrón exitoso de `methods.tex:2148-2155`

#### 1.3 Demostraciones "Por Verificación/Aplicación Directa"

**Archivos afectados:**

- `src/chapters/methods.tex:2032,2188` - 2 demostraciones

**Acción:** Evaluar si pueden condensarse siguiendo mismo patrón

### Fase 2: Eliminación de Redundancias Verbales (Prioridad Media)

#### 2.1 Frases "Por tanto" redundantes

**Archivos afectados:**

- `src/chapters/methods.tex:633,1272,1572`
- `src/chapters/results.tex:294`
- `src/chapters/discussion.tex:179`

**Acción:** Para cada ocurrencia:

- Si conclusión es inmediata → cambiar a "luego" o integrar en frase anterior
- Si es necesaria para claridad → mantener

#### 2.2 Frases "lo cual establece" redundantes

**Archivos afectados:**

- `src/chapters/methods.tex:1266,1272,1663`

**Acción:** Evaluar si pueden eliminarse o condensarse

### Fase 3: Mejora de Títulos (Prioridad Baja)

#### 3.1 Análisis sistemático de títulos

**Método:** Para cada archivo con estructuras matemáticas:

1. Extraer todos los títulos con `grep`
2. Evaluar según criterios:

- Longitud > 60 caracteres → condensar
- Palabras genéricas ("Propiedades", "Conexión") → hacer específicos
- Redundancias → eliminar
- Densidad informativa → maximizar

#### 3.2 Archivos prioritarios

- `src/chapters/methods.tex` - 146 estructuras (mayor impacto)
- `src/chapters/results.tex` - 49 estructuras

### Fase 4: Revisión de DRY y Fragmentación (Prioridad Media)

#### 4.1 Identificar repeticiones conceptuales

**Método:** Buscar:

- Conceptos repetidos en múltiples proposiciones/observaciones
- Información duplicada entre demostraciones
- Fragmentación innecesaria de ideas relacionadas

#### 4.2 Aplicar DRY

- Consolidar información repetida
- Usar referencias cruzadas en lugar de repetir
- Integrar contenido fragmentado cuando mejore claridad

## Criterios de Decisión

Para cada mejora propuesta:

1. **¿Es obvio para audiencia experta?** → Eliminar/condensar
2. **¿Mejora densidad informativa?** → Aplicar
3. **¿Mantiene rigor matemático?** → Verificar antes de aplicar
4. **¿Sigue patrón exitoso ya aplicado?** → Usar como referencia

## Métricas de Éxito

- **Demostraciones condensadas**: ~30-50% reducción en líneas innecesarias
- **Redundancias eliminadas**: 0 frases obviamente redundantes
- **Títulos mejorados**: Todos > 60 caracteres evaluados y mejorados si aplica
- **Rigor mantenido**: Todas las demostraciones siguen siendo matemáticamente correctas

## Orden de Ejecución

1. **Fase 1** (Demostraciones) - Mayor impacto en concisión
2. **Fase 2** (Redundancias) - Mejora fluidez de lectura
3. **Fase 4** (DRY) - Mejora organización estructural
4. **Fase 3** (Títulos) - Pulido final

## Referencias

- Spec completo: `docs/specs/REFACTORING_MATHEMATICAL_RIGOR_SPEC.md`
- Patrón exitoso: `src/chapters/methods.tex:2148-2155` (hermiticidad operador integral)
- Style Guide: `docs/style/STYLE_GUIDE.md`

### To-dos

- [ ] Revisar y mejorar 5 demostraciones 'Por Sustitución Directa' en results.tex (67,98,112) y methods.tex (616,1690) - mostrar cálculo o eliminar si trivial
- [ ] Revisar y condensar 6 demostraciones 'Por Construcción' en methods.tex (554,645,1067,1109,1242,1379) eliminando pasos intermedios obvios
- [ ] Evaluar y condensar 2 demostraciones 'Por Verificación/Aplicación Directa' en methods.tex (2032,2188)
- [ ] Revisar y condensar 5 ocurrencias de 'Por tanto' redundantes en methods.tex, results.tex y discussion.tex
- [ ] Evaluar y condensar 3 ocurrencias de 'lo cual establece' en methods.tex si son redundantes
- [ ] Identificar y aplicar DRY: consolidar repeticiones conceptuales, usar referencias cruzadas, integrar contenido fragmentado
- [ ] Revisar y mejorar títulos de 146 estructuras matemáticas en methods.tex: evaluar longitud, especificidad y densidad
- [ ] Revisar y mejorar títulos de 49 estructuras matemáticas en results.tex aplicando mismos criterios