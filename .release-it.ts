import type { Config } from 'release-it';

export default {
  git: {
    commitMessage: 'chore: release v${version}',
    tagName: 'v${version}',
    requireCleanWorkingDir: true,
    requireBranch: 'main',
    requireUpstream: true,
    push: true,
    commit: true,
    tag: true,
    addUntrackedFiles: true,
  },
  github: {
    release: true,
    releaseName: 'v${version}',
    // No especificar autoGenerate ni releaseNotes
    // release-it automáticamente usa context.changelog del plugin
    // que contiene solo los cambios de la versión actual
    assets: ['build/document-v*.pdf', 'checksums.txt'],
  },
  npm: {
    publish: false,
  },
  hooks: {
    'after:bump': [
      'pnpm run generate:figures',
      'pnpm run generate:zenodo',
      'pnpm exec tsx scripts/build.ts ${version}',
    ],
    // Generate figures first, then generate .zenodo.json from CITATION.cff,
    // then build PDF with correct version number
    // release-it automatically does `git add . --update` before commit
  },
  plugins: {
    '@release-it/bumper': {
      in: 'package.json',
      out: [
        {
          file: 'CITATION.cff',
          path: 'version',
          type: 'text/yaml',
        },
        // .zenodo.json is now generated from CITATION.cff via cffconvert
        // in scripts/tasks/citation.ts, so we don't update it here
      ],
    },
    '@release-it/conventional-changelog': {
      preset: {
        name: 'conventionalcommits',
      },
      infile: 'CHANGELOG.md',
    },
  },
} satisfies Config;

