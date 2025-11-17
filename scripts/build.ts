#!/usr/bin/env tsx
import { updateCitationDate } from './tasks/citation.js';
import { cleanupOldVersions } from './tasks/cleanup.js';
import { compilePDF } from './tasks/compile.js';
import { generateChecksums } from './tasks/checksums.js';
import type { ReleaseConfig } from './types.js';

function createReleaseConfig(version: string): ReleaseConfig {
  return {
    version,
    buildDir: 'build',
    sourceTex: 'main.tex',
    outputPdf: `build/document-v${version}.pdf`,
    checksumsFile: 'checksums.txt',
  };
}

async function main(): Promise<void> {
  // Get version from package.json
  const packageJsonPath = new URL('../package.json', import.meta.url);
  const packageJson = JSON.parse(await import('fs').then(m => m.promises.readFile(packageJsonPath, 'utf8')));
  const version = packageJson.version;
  
  if (!version) {
    console.error('Error: Version not found in package.json');
    process.exit(1);
  }
  
  const config = createReleaseConfig(version);
  
  try {
    console.log(`\n🔨 Building release artifacts for v${version}...\n`);
    
    cleanupOldVersions(config.buildDir);
    updateCitationDate();
    compilePDF(config);
    generateChecksums(config);
    
    console.log(`\n✅ Build completed successfully for v${version}\n`);
    console.log(`Generated files:`);
    console.log(`  - ${config.outputPdf}`);
    console.log(`  - ${config.checksumsFile}`);
    console.log(`  - CITATION.cff (updated)`);
    console.log(`  - .zenodo.json (updated by @release-it/bumper)\n`);
  } catch (error) {
    console.error(`\n❌ Build failed:`, error);
    process.exit(1);
  }
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});

