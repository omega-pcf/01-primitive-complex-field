# Documentación del Proyecto

Este directorio contiene toda la documentación técnica del proyecto, incluyendo guías de uso, arquitectura, especificaciones y consultas de investigación.

## Estructura

```
docs/
├── README.md              # Este archivo
├── usage.md               # Guía de uso del pipeline de releases
├── architecture.md        # Arquitectura del sistema de releases
├── specs/                 # Especificaciones técnicas formales
└── perplexity/            # Consultas y respuestas de investigación técnica
```

## Documentación Principal

### Guías de Uso

- **usage.md**: Guía completa de uso del pipeline de releases
  - Workflow de desarrollo con LaTeX Workshop
  - Conventional Commits y generación automática de changelog
  - Comandos de build y release
  - Instalación y requisitos

### Arquitectura

- **architecture.md**: Arquitectura del sistema de releases
  - Stack tecnológico (release-it, plugins, Docker)
  - Flujo de ejecución completo
  - Medidas de reproducibilidad
  - Estructura de scripts y metadata

### Especificaciones

- **specs/**: Especificaciones técnicas formales
  - Configuración de release-it y plugins
  - Schemas de metadata (CITATION.cff, .zenodo.json)
  - Integración con Zenodo webhook

## Investigación Técnica

El directorio `perplexity/` contiene consultas detalladas y respuestas de investigación sobre problemas técnicos específicos. Los archivos están numerados cronológicamente y distinguen entre prompts (consultas) y responses (respuestas).

**Temas investigados:**
- Integración Zenodo CI
- Dependencias LaTeX en Docker
- Template de Release Notes en TypeScript
- GitHub Action y Release Notes
- Changelog solo de versión actual

## Convenciones

### Conventional Commits

Todos los commits deben seguir el formato [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```

**Tipos comunes:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bugs
- `docs`: Cambios en documentación
- `refactor`: Refactorización de código
- `chore`: Tareas de mantenimiento

### Nomenclatura de Archivos

- **perplexity/**: Formato `NNN_type-tema-descriptivo.md`
  - `NNN`: Número secuencial (001, 002, ...)
  - `type`: `prompt` o `response`
  - `tema-descriptivo`: Descripción semántica del tema
