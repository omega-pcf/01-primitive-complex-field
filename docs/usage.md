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
