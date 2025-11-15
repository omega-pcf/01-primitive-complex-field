# Diagnóstico: Problema de Hyphenation en Español

## Problema Identificado

El análisis del log de compilación del POC (`test_hyphenation.tex`) muestra:

```
Package babel Info: Hyphen rules for 'spanish' set to \l@english
(babel)             (\language0). Reported on input line 23.
```

**Esto confirma que los patrones de hyphenation para español NO están instalados en el sistema.** Babel está usando las reglas de hyphenation de inglés para español, lo cual causa divisiones incorrectas como "fun-" en lugar de "fun-cio-nes".

## Evidencia del Sistema

### Verificación de Paquetes
```bash
$ dpkg -l texlive-lang-spanish
Status: Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
```
**Resultado:** El paquete NO está instalado.

### Verificación de Archivos de Patrones
```bash
$ find /usr/share/texlive -type f -name "*eshyph*" -o -name "*spanish.hyp*"
```
**Resultado:** No se encontraron archivos de patrones de hyphenation para español.

### Verificación de Directorio de Patrones
```bash
$ ls /usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/
```
**Resultado:** El directorio existe pero no contiene archivos para español.

## Solución

### Paso 1: Instalar el paquete de patrones de hyphenation

```bash
sudo apt-get update
sudo apt-get install texlive-lang-spanish
```

### Paso 2: Actualizar la base de datos de TeX

```bash
sudo texhash
```

### Paso 3: Verificar la instalación

Después de instalar, el log de compilación debería mostrar:

```
Package babel Info: Hyphen rules for 'spanish' set to \l@spanish
```

En lugar de:

```
Package babel Info: Hyphen rules for 'spanish' set to \l@english
```

### Paso 4: Recompilar el documento

```bash
# Limpiar archivos auxiliares
rm -f *.aux *.log *.out *.toc *.bbl *.bcf *.blg *.run.xml

# Recompilar
pdflatex main.tex
```

## Configuración Aplicada en main.tex

La configuración en `main.tex` es correcta:

1. **Carga de español con babel moderno:**
   ```latex
   \babelprovide[import,main]{spanish}%
   \selectlanguage{spanish}%
   ```

2. **Configuración de mínimos de hyphenation:**
   ```latex
   \babelhyphenmins{spanish}{2}{2}%
   ```

3. **Activación explícita de patrones:**
   ```latex
   \useshorthands{spanish}%
   \languageshorthands{spanish}%
   ```

**Conclusión:** El problema NO es de configuración de LaTeX, sino de dependencias del sistema. Una vez instalado `texlive-lang-spanish`, el hyphenation debería funcionar correctamente.

## Archivos de Prueba Creados

- `test_hyphenation.tex`: POC mínimo para probar hyphenation (eliminado después del diagnóstico)
- `docs/diagnostico_hyphenation.tex`: Documento LaTeX con diagnóstico completo

