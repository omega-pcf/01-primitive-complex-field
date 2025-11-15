# Prompt para Perplexity: Investigación sobre Numeración de Subsubsecciones en LaTeX

## Contexto del Problema

Estoy trabajando en un documento LaTeX que necesita numerar las subsubsecciones en formato `n.x.x` (por ejemplo, `1.1.1`, `1.1.2`, `2.3.1`), pero actualmente solo se están numerando hasta el nivel de subsección (`n.x`). El documento compila correctamente, pero las subsubsecciones no muestran números.

## Estructura del Proyecto

- **Clase base**: `extarticle` (cargada a través de `lapreprint.cls`)
- **Clase personalizada**: `lapreprint.cls` (basada en eLife template)
- **Paquete de títulos**: `titlesec` con opción `[explicit]`
- **Opción de numeración**: La clase se carga con opción `secnum`

## Archivos Relevantes

### 1. Clase `lapreprint.cls` (Líneas 222-242)

```latex
% Format title
\if@secnum\else\setcounter{secnumdepth}{0}\fi
\RequirePackage[explicit]{titlesec}
\titleformat{\section}
  {\color{MediumGrey}\Large\bfseries}
  {\thesection}{10pt}{#1}[]
\titleformat{\subsection}
  {\large\bfseries}
  {\thesubsection}{10pt}{#1}[]
\titleformat{\subsubsection}
  {\large}
  {\thesubsubsection}{10pt}{#1}[]    
\titleformat{\paragraph}
  {\color{MediumGrey}\large}
  {\theparagraph}{10pt}{#1}[]

% Title spacing
\titlespacing*{\section}{0pc}{3ex \@plus4pt \@minus3pt}{2pt}
\titlespacing*{\subsection}{0pc}{2.5ex \@plus3pt \@minus2pt}{1pt}
\titlespacing*{\subsubsection}{0pc}{2ex \@plus2.5pt \@minus1.5pt}{0pt}
\titlespacing*{\paragraph}{0pc}{1.5ex \@plus2pt \@minus1pt}{0pt}
```

**Observaciones importantes**:
- La línea 223 establece `secnumdepth` a 0 SOLO si `@secnum` es falso
- Si `@secnum` es verdadero (nuestro caso), NO se establece `secnumdepth`, dejando el valor por defecto
- `titlesec` se carga con opción `[explicit]`, lo que requiere usar `#1` para el título
- El formato de `\subsubsection` ya incluye `{\thesubsubsection}`, lo que sugiere que debería mostrar números

### 2. Archivo Principal `main.tex` (Relevante)

```latex
% Declare document class
\documentclass[9pt,Preprint,secnum,spanish]{lapreprint}

% Configuración de numeración de secciones: habilitar numeración hasta subsubsecciones (n.x.x)
% Debe establecerse después de cargar la clase pero antes de que titlesec procese los formatos
\setcounter{secnumdepth}{3}

% ... otros paquetes ...

% Espacio en títulos de sección (titlesec ya está cargado por lapreprint.cls)
% Asegurar que secnumdepth esté en 3 antes de redefinir formatos
\setcounter{secnumdepth}{3}
% Redefinir formato de subsubsection para asegurar que muestre numeración
% El formato debe incluir el título (#1) como en la definición original
\titleformat{\subsubsection}
  {\large}
  {\thesubsubsection}{10pt}{#1}[]
\titlespacing*{\section}{0pt}{2\baselineskip}{1\baselineskip}
\titlespacing*{\subsection}{0pt}{1.5\baselineskip}{0.75\baselineskip}
\titlespacing*{\subsubsection}{0pt}{1.25\baselineskip}{0.5\baselineskip}

% ... más código ...

\AtBeginDocument{%
  % Asegurar que secnumdepth esté en 3 (subsubsecciones) después de todas las configuraciones
  \setcounter{secnumdepth}{3}%
  % ... otras configuraciones ...
}
```

**Intentos realizados**:
1. Establecer `\setcounter{secnumdepth}{3}` justo después de cargar la clase
2. Establecer `\setcounter{secnumdepth}{3}` antes de redefinir `\titleformat{\subsubsection}`
3. Establecer `\setcounter{secnumdepth}{3}` en `\AtBeginDocument`
4. Redefinir `\titleformat{\subsubsection}` para asegurar que incluya `{\thesubsubsection}`

### 3. Ejemplo de Uso de Subsubsecciones

En `src/chapters/methods.tex`:
```latex
\subsection[Espacios Adjuntos: Re-parametrizaciones de C]{Espacios Adjuntos: Re-parametrizaciones de $\mathbb{C}$}

\subsubsection{Equivalencia Métrica}
\subsubsection{Espacio Adjunto I: Spacetime de Minkowski}
\subsubsection{Espacio Adjunto II: Espacio de Hilbert}
```

## Información sobre Valores de `secnumdepth`

Según documentación estándar de LaTeX:
- `-1`: `\part`
- `0`: `\chapter` (en clases book/report)
- `1`: `\section`
- `2`: `\subsection`
- `3`: `\subsubsection`
- `4`: `\paragraph`
- `5`: `\subparagraph`

**Para clase `article`/`extarticle`**:
- Valor por defecto de `secnumdepth`: `2` (solo secciones y subsecciones)
- Para numerar subsubsecciones: `secnumdepth = 3`

## Lo que Necesito que Investigue Perplexity

### 1. Comportamiento de `secnumdepth` con `titlesec` y opción `[explicit]`

- ¿El paquete `titlesec` con opción `[explicit]` puede interferir con `secnumdepth`?
- ¿Hay algún orden específico requerido entre establecer `secnumdepth` y definir `\titleformat`?
- ¿La opción `[explicit]` de `titlesec` requiere algún tratamiento especial para la numeración?

### 2. Interacción entre Clase Personalizada y `secnumdepth`

- ¿Puede una clase personalizada que carga `titlesec` internamente interferir con `secnumdepth` establecido después?
- ¿Hay algún hook o momento específico donde deba establecerse `secnumdepth` cuando se usa una clase personalizada?
- ¿El hecho de que `lapreprint.cls` establezca `secnumdepth` condicionalmente (solo si `@secnum` es falso) puede causar problemas?

### 3. Valores Correctos para `extarticle`

- ¿El valor por defecto de `secnumdepth` en `extarticle` es realmente `2`?
- ¿Hay alguna diferencia entre `article` y `extarticle` respecto a `secnumdepth`?
- ¿Necesito establecer `secnumdepth` a un valor diferente para `extarticle`?

### 4. Soluciones Alternativas

- ¿Hay alguna forma de forzar la numeración de subsubsecciones sin depender de `secnumdepth`?
- ¿Puedo modificar directamente el contador de subsubsecciones o su formato de manera más directa?
- ¿Existe algún paquete o comando específico para este propósito?

### 5. Documentación Específica a Consultar

Por favor, consulta y referencia:
- Documentación oficial de `titlesec` en CTAN
- Documentación de `extarticle` (extsizes package)
- Stack Exchange/TeX.SX preguntas sobre `secnumdepth` con `titlesec`
- Documentación de LaTeX2e sobre contadores de secciones
- Cualquier guía sobre clases personalizadas y numeración de secciones

### 6. Validación de Hipótesis

Por favor, valida o refuta estas hipótesis:

**Hipótesis 1**: `titlesec` con `[explicit]` requiere que `secnumdepth` se establezca ANTES de cargar el paquete, no después.

**Hipótesis 2**: Cuando una clase personalizada carga `titlesec` internamente, el `secnumdepth` establecido en el documento principal puede ser sobrescrito.

**Hipótesis 3**: El formato `\titleformat{\subsubsection}` necesita algún parámetro adicional o diferente cuando `secnumdepth=3`.

**Hipótesis 4**: Hay un conflicto entre el `\titleformat` definido en la clase y el redefinido en el documento principal.

**Hipótesis 5**: El valor por defecto de `secnumdepth` en `extarticle` cuando se usa con `titlesec` puede ser diferente.

## Formato de Respuesta Esperado

Por favor, proporciona:

1. **Diagnóstico del problema**: ¿Qué está causando que las subsubsecciones no se numeren?

2. **Solución específica**: Código LaTeX exacto que debo agregar/modificar, incluyendo:
   - Dónde colocar el código (en qué archivo, en qué posición)
   - Orden exacto de comandos
   - Cualquier modificación necesaria en `lapreprint.cls` si es requerida

3. **Explicación técnica**: Por qué la solución funciona, referenciando documentación oficial.

4. **Alternativas**: Si hay múltiples formas de resolverlo, lista todas con pros/contras.

5. **Referencias**: Enlaces a documentación oficial, preguntas relevantes en Stack Exchange, etc.

## Información Adicional

- **Compilador**: Probablemente `pdflatex` o `xelatex` (el proyecto tiene soporte para ambos)
- **Versión de LaTeX**: No especificada, pero asumir distribución moderna (TeX Live 2020+)
- **Restricciones**: No puedo modificar fácilmente `lapreprint.cls` (es una clase externa), pero puedo hacerlo si es absolutamente necesario
- **Resultado esperado**: Las subsubsecciones deben aparecer como `1.1.1`, `1.1.2`, `2.3.1`, etc. en el PDF compilado

## Ejemplo de Comportamiento Esperado

**Actual** (incorrecto):
```
1. Sección
   1.1 Subsección
       Subsubsección (sin número)
       Subsubsección (sin número)
```

**Deseado** (correcto):
```
1. Sección
   1.1 Subsección
      1.1.1 Subsubsección
      1.1.2 Subsubsección
```

---

**Nota para el usuario**: Este prompt está diseñado para ser copiado y pegado directamente en Perplexity. Incluye todo el contexto necesario para que Perplexity pueda investigar el problema sin acceso al proyecto ni al REPL.

