# Decisión Técnica 003: Selección Final de Keywords para Abstract

**Fecha**: 2025-01-28  
**Estado**: Aprobada  
**Impacto**: Abstract del paper (`src/chapters/abstract.tex`)

## Decisión

**Seleccionar 10 keywords** para el abstract, dentro del rango aceptable para papers interdisciplinarios (8-10 keywords), balanceando rigor técnico con estándares editoriales prácticos.

**Keywords finales seleccionados**:
1. Riemann hypothesis
2. Hilbert-Pólya conjecture
3. L-functions
4. Self-adjoint operators
5. Random matrix theory
6. Zeta function zeros
7. Mersenne primes
8. Modular spaces
9. Category theory
10. Arithmetic geometry

## Contexto

### Proceso de Selección

1. **Análisis inicial**: Se propusieron 20 keywords basados en análisis técnico exhaustivo del paper
2. **Validación con Perplexity**: Se creó prompt detallado (`docs/perplexity/PROMPT_VALIDACION_KEYWORDS_ABSTRACT.md`) para validar keywords contra literatura matemática estándar
3. **Análisis crítico**: Se identificaron sesgos en el reporte de Perplexity (`docs/analysis/ANALISIS_CRITICO_KEYWORDS_PERPLEXITY.md`), especialmente la clasificación errónea de "self-reference" como "filosófico"
4. **Rebuttal técnico**: Se creó validación técnica exhaustiva (`docs/perplexity/REBUTTAL_KEYWORDS_ADICIONALES_TECNICO.md`) documentando uso técnico sustancial de cada keyword
5. **Revisión editorial**: Perplexity proporcionó análisis de estándares editoriales indicando que 20 keywords exceden límites prácticos

### Estándares Editoriales Identificados

- **Promedio histórico**: 3.49 keywords en matemáticas (2015)
- **Rango estándar recomendado**: 3-5 keywords
- **Máximo permitido en journals principales**: 5-8 keywords
- **Máximo observado en papers interdisciplinarios**: 8-10 keywords
- **Riesgo con más de 10**: Rechazo automático por 95%+ de revistas internacionales

## Justificación

### Criterios de Selección Aplicados

Cada keyword seleccionado cumple **todos** los siguientes criterios:

1. **Uso técnico sustancial**: No solo mencionado, sino usado en construcciones matemáticas formales, teoremas, o ecuaciones
2. **Conexión verificada**: Relacionado con correspondencias verificadas empíricamente o estructuralmente
3. **Relevancia para búsqueda**: Investigadores en el área buscarían este término específico
4. **Estándares editoriales**: Dentro del rango aceptable (8-10 para papers interdisciplinarios)

### Justificación por Keyword

#### Núcleo Absoluto (5 keywords)

1. **Riemann hypothesis**
   - Tema central del paper
   - Término estándar en literatura matemática
   - Validado por Perplexity como ALTA frecuencia

2. **Hilbert-Pólya conjecture**
   - Marco teórico principal
   - Paper construye explícitamente operador relacionado
   - Término estándar validado

3. **L-functions**
   - Objeto de estudio explícito (zeta y otras L-funciones)
   - Mencionado múltiples veces en abstract
   - Término estándar con guión validado

4. **Self-adjoint operators**
   - Construcción técnica principal: $\hat{\Omega}: L^2(\mathbb{C}) \otimes \mathbb{C}^3 \to L^2(\mathbb{C}) \otimes \mathbb{C}^3$
   - Más específico que "Spectral theory"
   - Término estándar en análisis funcional

5. **Zeta function zeros**
   - Objeto específico de predicción verificada
   - Predicción con precisión 99.70% hasta altura $t \sim 10^{23}$
   - Término buscable específico

#### Conexiones Verificadas Empíricamente (3 keywords)

6. **Random matrix theory**
   - Conexión Montgomery-Dyson-Odlyzko establecida
   - Mencionado explícitamente en introduction.tex
   - Término estándar validado

7. **Mersenne primes**
   - Correspondencia verificada en 51 primos conocidos
   - Verificación sobre 25+ millones de órdenes de magnitud
   - Una de las dos correspondencias clave mencionadas en abstract
   - Contribución sustancial del paper

8. **Modular spaces**
   - Construcción técnica fundamental: $M_{PCF} = \mathbb{C}/\Lambda_{PCF} \cong T^2$
   - Pilar de la construcción (formal.tex línea 11)
   - Espacios de Teichmüller y módulos técnicamente usados

#### Conexiones Técnicas Sustanciales (2 keywords)

9. **Category theory**
   - Uso técnico explícito: Teorema de conmutatividad de functores (methods.tex línea 359)
   - Estructura tripartita categórica $P \leftrightarrow C \leftrightarrow F$
   - Referencias técnicas: Lawvere, Yanofsky, Baez-Stay
   - No solo mencionado, sino usado formalmente

10. **Arithmetic geometry**
    - Conexión explícita con Weil (results.tex línea 1103)
    - Aplicabilidad técnica a funciones L de geometría aritmética (formal.tex líneas 74-85)
    - Referencias técnicas: Weil, Borger, Buium
    - Conexión estructural verificada

### Keywords Removidos (pero bien documentados en texto)

Los siguientes términos tienen uso técnico sustancial pero fueron removidos para cumplir estándares editoriales. **Todos están bien documentados en el abstract y texto**, por lo que serán buscables mediante búsqueda de texto completo:

- **GUE**: Incluido implícitamente en "Random matrix theory"; mencionado explícitamente en abstract
- **Self-referential paradoxes**: Mencionado explícitamente en abstract (Lawvere-Yanofsky)
- **Bootstrap methods**: Mencionado explícitamente en abstract
- **Multi-domain coherence**: Concepto central mencionado múltiples veces en abstract
- **Complex plane**: Mencionado explícitamente en abstract como objeto fundamental
- **Spectral theory**: Incluido implícitamente en "Self-adjoint operators"
- **Operator eigenvalues**: Incluido implícitamente en "Self-adjoint operators"
- **Weil conjectures**: Mencionado en results.tex, conexión técnica documentada
- **Periods**: Mencionado en introduction.tex (Kontsevich-Zagier)
- **Fixed point theorems**: Uso técnico documentado en methods.tex (Lawvere)

## Referencias

### Documentos de Análisis

- **Prompt inicial**: `docs/perplexity/PROMPT_VALIDACION_KEYWORDS_ABSTRACT.md`
- **Análisis crítico**: `docs/analysis/ANALISIS_CRITICO_KEYWORDS_PERPLEXITY.md`
- **Rebuttal técnico**: `docs/perplexity/REBUTTAL_KEYWORDS_ADICIONALES_TECNICO.md`

### Evidencia Técnica del Paper

- **Abstract**: `src/chapters/abstract.tex`
- **Introduction**: `src/chapters/introduction.tex` (menciones de GUE, períodos, geometría aritmética)
- **Methods**: `src/chapters/methods.tex` (teorema de conmutatividad de functores, estructura categórica)
- **Results**: `src/chapters/results.tex` (correspondencia Mersenne, conexión Weil)
- **Formal**: `src/chapters/formal.tex` (cuatro correspondencias verificadas, aplicabilidad a geometría aritmética)

### Estándares Editoriales

- Análisis de Perplexity sobre estándares de keywords en matemáticas
- Rango recomendado: 3-5 keywords estándar, 8-10 para interdisciplinarios
- Riesgo de rechazo automático con más de 10 keywords

## Impacto

### Archivos Afectados

- `src/chapters/abstract.tex`: Keywords actualizados de 20 a 10

### Cambios Realizados

**Antes (20 keywords)**:
Riemann hypothesis, Hilbert-Pólya conjecture, L-functions, Random matrix theory, GUE, Self-adjoint operators, Self-referential paradoxes, Bootstrap methods, Zeta function zeros, Multi-domain coherence, Mersenne primes, Category theory, Arithmetic geometry, Modular spaces, Complex plane, Spectral theory, Operator eigenvalues, Weil conjectures, Periods, Fixed point theorems.

**Después (10 keywords)**:
Riemann hypothesis, Hilbert-Pólya conjecture, L-functions, Self-adjoint operators, Random matrix theory, Zeta function zeros, Mersenne primes, Modular spaces, Category theory, Arithmetic geometry.

### Términos Técnicos Preservados en Texto

Todos los términos removidos de keywords están explícitamente mencionados en:
- Abstract (búsqueda de texto completo)
- Introduction (contexto técnico)
- Methods/Results/Formal (construcciones técnicas)

Por lo tanto, **mantienen discoverability** mediante búsqueda de texto completo sin necesidad de ser keywords.

## Alternativas Consideradas

### Opción A: 8 keywords (Máximo conservador)
- Remover "Category theory" y "Arithmetic geometry"
- **Rechazada**: Perdería conexiones técnicas sustanciales documentadas

### Opción B: 10 keywords (Seleccionada)
- Balance entre rigor técnico y estándares editoriales
- **Aprobada**: Cumple estándares y mantiene conexiones técnicas importantes

### Opción C: 20 keywords (Inicial propuesta)
- Incluir todos los términos técnicamente validados
- **Rechazada**: Excede límites editoriales prácticos, riesgo de rechazo automático

### Opción D: 5 keywords (Mínimo estándar)
- Solo núcleo absoluto
- **Rechazada**: No reflejaría amplitud interdisciplinaria del paper

## Estrategia de Discoverability

### Keywords (10)
- Términos que investigadores buscarían específicamente como keywords
- Optimizados para indexing automático y búsquedas por keyword

### Texto Completo (términos removidos)
- Todos los términos técnicos removidos están explícitamente en abstract/texto
- Serán encontrados mediante búsqueda de texto completo
- Tienen contexto técnico completo en el paper

### Ventaja de esta Estrategia
- **Keywords**: Cumplen estándares editoriales, maximizan aceptación
- **Texto completo**: Mantiene discoverability de todos los términos técnicos
- **Balance**: Rigor técnico preservado sin riesgo editorial

## Verificación

- [x] 10 keywords seleccionados cumplen criterios técnicos
- [x] Todos los keywords tienen uso técnico sustancial documentado
- [x] Términos removidos están explícitamente en abstract/texto
- [x] Cumple estándares editoriales (8-10 para interdisciplinarios)
- [x] Abstract actualizado en `src/chapters/abstract.tex`
- [x] Documentación completa en `docs/analysis/` y `docs/perplexity/`

## Lecciones Aprendidas

1. **Balance entre rigor y pragmatismo**: Rigor técnico debe balancearse con estándares editoriales prácticos
2. **Discoverability no depende solo de keywords**: Términos bien documentados en texto completo son igualmente buscables
3. **Análisis crítico de herramientas**: Perplexity proporcionó información útil pero con sesgos que requirieron corrección
4. **Validación técnica vs. estándares editoriales**: Ambos son importantes y deben balancearse

## Notas Adicionales

### Si el Journal Permite Más Keywords

Si durante el proceso de publicación se identifica que el journal objetivo permite más keywords (ej: 12-15), se pueden agregar prioritariamente:
- GUE (específico de Random matrix theory)
- Self-referential paradoxes (concepto central con formalización matemática)
- Bootstrap methods (metodología explícita)

### Si el Journal Requiere Menos Keywords

Si el journal requiere menos keywords (ej: 5-6), se puede reducir a núcleo absoluto:
1. Riemann hypothesis
2. Hilbert-Pólya conjecture
3. L-functions
4. Self-adjoint operators
5. Random matrix theory
6. Zeta function zeros

Los demás términos permanecen en abstract/texto para discoverability.

### Validación Continua

Los keywords seleccionados están técnicamente validados contra:
- Contenido real del paper
- Literatura matemática estándar
- Estándares editoriales prácticos
- Criterios de discoverability

Esta validación puede actualizarse si se identifican journals específicos con requisitos diferentes.

