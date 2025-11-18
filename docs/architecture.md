# Arquitectura

## Stack

- **release-it**: Versionado semántico + GitHub releases
- **@release-it/bumper**: Sincroniza versión `package.json` → `CITATION.cff`, `.zenodo.json`
- **TypeScript + tsx**: Scripts de orquestación
- **Docker** (`kjarosh/latex:2024.4-full`): Compilación LaTeX reproducible
- **Zenodo webhook**: Integración automática desde GitHub

## Flujo

```
pnpm run release
  → before:bump: pnpm run build
    → cleanup: elimina document-v*.pdf anteriores
    → citation: actualiza date-released
    → compile: Docker con SOURCE_DATE_EPOCH (git commit timestamp)
    → checksums: SHA256 del PDF
  
  → @release-it/bumper: actualiza versiones
  
  → after:bump: stagea archivos (PDF, checksums, metadata)
  
  → Git: commit + tag v${version} + push
  
  → GitHub: Release con assets
  
  → Zenodo: webhook automático → nueva versión + DOI
```

## Reproducibilidad

**SOURCE_DATE_EPOCH:** Extraído de `git log -1 --pretty=%ct`

**LaTeX primitives:** `\pdfinfoomitdate=1`, `\pdftrailerid{}`, etc. (ver `main.tex`)

**Docker pinned:** `kjarosh/latex:2024.4-full` (versión explícita)

Mismo commit = mismo PDF hash (garantizado)

## Estructura

```
scripts/
├── build.ts              # Build independiente
├── release-orchestrator.ts  # Hook after:bump (staging)
├── tasks/                # Tareas atómicas
└── utils/                # Utilidades compartidas
```

## Metadata

**Source of truth:** `package.json` version

**Sincronización automática:**
- `CITATION.cff` version (vía @release-it/bumper)
- `.zenodo.json` version (vía @release-it/bumper)
- `CITATION.cff` date-released (vía hook before:bump)

**Zenodo:** Lee `.zenodo.json` del tag, crea versión bajo mismo Concept DOI
