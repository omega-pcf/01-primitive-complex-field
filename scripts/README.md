# Scripts de Verificación

## verificar_numeracion.py

Script para verificar inconsistencias en la numeración de secciones y teoremas.

### Uso

```bash
python3 scripts/verificar_numeracion.py
```

### Qué hace

1. **Analiza el código fuente**: Busca todas las secciones, subsecciones, subsubsecciones y construcciones matemáticas en `src/chapters/*.tex`
2. **Compila el documento**: Ejecuta `pdflatex` dos veces para generar el PDF
3. **Extrae texto del PDF**: Usa `pdftotext` para extraer el texto compilado
4. **Compara numeraciones**: Busca inconsistencias entre el código fuente y el PDF compilado
5. **Reporta problemas**: Muestra referencias hardcodeadas y numeraciones incorrectas

### Requisitos

- Python 3
- `pdflatex` en el PATH
- `pdftotext` en el PATH (opcional, pero recomendado)

### Salida

El script muestra:
- Lista de todas las secciones encontradas
- Lista de construcciones matemáticas (teoremas, definiciones, etc.)
- Referencias hardcodeadas encontradas
- Problemas de numeración detectados en el PDF

### Ejemplo de uso

```bash
cd /home/aficio/Documents/DevelopmentV2/01-omega-phi-primitive-complex-plane
python3 scripts/verificar_numeracion.py
```

