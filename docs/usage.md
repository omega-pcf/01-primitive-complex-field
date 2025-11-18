# Uso del Pipeline de Releases

## Desarrollo

**Template:** LaPreprint (`lapreprint.cls`)

**Workflow diario:** LaTeX Workshop (James Yu) en VS Code
- Compila automáticamente a `build/main.pdf`
- Preview en tiempo real

**Verificación pre-release:**
```bash
pnpm run build
sha256sum build/document-v*.pdf build/main.pdf  # Deben coincidir
```

## Commits y Changelog

**Conventional Commits:** Todos los commits deben seguir el formato [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Tipos comunes:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bugs
- `docs`: Cambios en documentación
- `refactor`: Refactorización de código
- `chore`: Tareas de mantenimiento (build, config, etc.)

**Ejemplos:**
```bash
git commit -m "feat(release): add dotenv-cli to load GITHUB_TOKEN from .env"
git commit -m "fix(release): use automatic changelog from plugin"
git commit -m "refactor(scripts): remove legacy code and clean up unused utilities"
```

**Changelog automático:** El plugin `@release-it/conventional-changelog` genera automáticamente `CHANGELOG.md` basándose en los commits convencionales. El changelog se actualiza durante cada release con solo los cambios de la versión actual.

## Releases

**Build independiente:**
```bash
pnpm run build
```

**Release completo:**
```bash
pnpm run release
```

**Dry-run (sin cambios):**
```bash
pnpm run release:dry-run
```

## Instalación

```bash
pnpm install
```

**Requisitos:** Node.js 20+, pnpm 9+, Docker
