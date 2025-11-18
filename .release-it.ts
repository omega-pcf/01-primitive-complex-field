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
    'after:bump': 'pnpm exec tsx scripts/build.ts ${version}',
    // Build after version bump so PDF uses correct version number
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
        {
          file: '.zenodo.json',
          path: 'version',
          type: 'application/json',
        },
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

