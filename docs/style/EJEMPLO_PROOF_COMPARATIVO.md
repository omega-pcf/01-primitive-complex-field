# Ejemplo Comparativo: `\begin{proof}` vs `\qed` Manual

## Ejemplo Real del Documento

### ❌ Forma Actual (Redundante)

```latex
\begin{proposition}[Verificación del cilindro]\label{prop:verificacion-cilindro}
Los tres vértices satisfacen la ecuación del cilindro.
\begin{proof}
Verificamos cada vértice:
\begin{align*}
\sqrt{x_F^2 + y_F^2} &= \sqrt{{(-1.5)}^2 + {(-2.598)}^2} \\
&= \sqrt{2.25 + 6.75} = 3
\end{align*}
\qed % chktex 1  ← REDUNDANTE
\end{proof}
\end{proposition}
```

**Problema**: Se usa `\begin{proof}...\end{proof}` pero también `\qed` manual. `amsthm` ya coloca el QED automáticamente, así que el `\qed` manual es redundante.

### ✅ Forma Recomendada

```latex
\begin{proposition}[Verificación del cilindro]\label{prop:verificacion-cilindro}
Los tres vértices satisfacen la ecuación del cilindro.
\begin{proof}
Verificamos cada vértice:
\begin{align*}
\sqrt{x_F^2 + y_F^2} &= \sqrt{{(-1.5)}^2 + {(-2.598)}^2} \\
&= \sqrt{2.25 + 6.75} = 3
\end{align*}
Por lo tanto, todos los vértices satisfacen la ecuación del cilindro.
\end{proof}
\end{proposition}
```

**Ventaja**: `amsthm` coloca el QED automáticamente al final, sin necesidad de `\qed` manual.

## Comparación Visual

### Con `\begin{proof}...\end{proof}` (Recomendado)

**Resultado en PDF:**
```
Proposición 3.3.2 (Verificación del cilindro). Los tres vértices satisfacen 
la ecuación del cilindro.

Demostración. Verificamos cada vértice:
[ecuación alineada]
Por lo tanto, todos los vértices satisfacen la ecuación del cilindro. □
```

**Características:**
- Indentación automática del texto de la prueba
- Espaciado consistente antes y después
- Símbolo QED (□) colocado automáticamente al final
- Formato consistente con todas las demás pruebas

### Con `\qed` Manual (No Recomendado)

**Resultado en PDF:**
```
Proposición 3.3.2 (Verificación del cilindro). Los tres vértices satisfacen 
la ecuación del cilindro.

Demostración. Verificamos cada vértice:
[ecuación alineada]
□
```

**Problemas:**
- El QED puede quedar en línea extra si no se maneja correctamente
- Formato inconsistente si algunas pruebas usan `\qed` y otras no
- Requiere `% chktex 1` para evitar warnings
- Fácil olvidar el `\qed` en alguna prueba

## Casos Especiales

### Prueba que Termina con Ecuación Display

```latex
\begin{proof}
Por definición del módulo y propiedades de la norma:
\[
|z|^2 = z \cdot \bar{z} = (x + iy)(x - iy) = x^2 + y^2
\]
Por lo tanto, $|z| = \sqrt{x^2 + y^2}$.
\end{proof}
```

**Resultado**: El QED se coloca correctamente después de la ecuación, en la misma línea si hay espacio, o en línea nueva si es necesario.

### Prueba Larga con Múltiples Pasos

```latex
\begin{proof}
La demostración procede en tres pasos.

\textit{Paso 1}: Verificamos que la estructura es cerrada bajo operaciones.
[Contenido del paso 1]

\textit{Paso 2}: Mostramos que preserva la métrica.
[Contenido del paso 2]

\textit{Paso 3}: Concluimos que es isomorfismo.
[Contenido del paso 3]

Por lo tanto, la estructura es isomorfa al plano complejo.
\end{proof}
```

**Resultado**: El QED se coloca al final de todo el argumento, después del último párrafo.

## Recomendación Final

**✅ USAR `\begin{proof}...\end{proof}` exclusivamente**

1. Eliminar todos los `\qed` manuales dentro de entornos `proof`
2. Dejar que `amsthm` maneje el símbolo QED automáticamente
3. Solo usar `\qed` manual si la prueba NO está en un entorno `proof` (caso muy raro)

**Configuración opcional en `main.tex`:**
```latex
% Personalizar símbolo QED (opcional)
\renewcommand{\qedsymbol}{$\blacksquare$}  % Cuadrado negro
% O mantener el default: \renewcommand{\qedsymbol}{$\square$}  % Cuadrado vacío
```

