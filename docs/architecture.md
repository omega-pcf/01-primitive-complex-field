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
  → @release-it/bumper: actualiza versiones en package.json, CITATION.cff, .zenodo.json
  
  → after:bump: pnpm run build
    → cleanup: elimina document-v*.pdf anteriores
    → citation: actualiza date-released
    → compile: Docker con SOURCE_DATE_EPOCH (git commit timestamp)
    → checksums: SHA256 del PDF
  
  → Git: commit + tag v${version} + push (release-it stagea automáticamente con addUntrackedFiles)
  
  → GitHub: Release con assets (PDF, checksums)
  
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
├── build.ts              # Build independiente (hook after:bump)
├── tasks/                # Tareas atómicas
│   ├── checksums.ts
│   ├── citation.ts
│   ├── cleanup.ts
│   └── compile.ts
├── types.ts              # Tipos TypeScript
└── utils/
    └── git.ts            # Utilidades Git (getCommitEpoch)
```

## Metadata

**Source of truth:** `package.json` version

**Sincronización automática:**
- `CITATION.cff` version (vía @release-it/bumper)
- `.zenodo.json` version (vía @release-it/bumper)
- `CITATION.cff` date-released (vía hook after:bump → build.ts)

**Zenodo:** Lee `.zenodo.json` del tag, crea versión bajo mismo Concept DOI
