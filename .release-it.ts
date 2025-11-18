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
    autoGenerate: false,
    assets: ['build/document-v*.pdf', 'checksums.txt'],
    releaseNotes:
      'cat CHANGELOG.md && printf "\\n\\n## Files\\n\\n- **PDF**: `build/document-v${version}.pdf` - Compiled preprint document\\n\\n## DOI\\n\\nDOI: 10.5281/zenodo.17619486"',
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

