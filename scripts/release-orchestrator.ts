#!/usr/bin/env tsx
import { stageReleaseFiles } from './tasks/git-stage.js';
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
  const version = process.argv[2];
  
  if (!version) {
    console.error('Error: Version argument required');
    process.exit(1);
  }
  
  const config = createReleaseConfig(version);
  
  try {
    console.log(`\n📦 Staging release files for v${version}...\n`);
    
    // Only stage files - build should have been done already
    stageReleaseFiles(config);
    
    console.log(`\n✅ Files staged successfully for v${version}\n`);
  } catch (error) {
    console.error(`\n❌ Staging failed:`, error);
    process.exit(1);
  }
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
