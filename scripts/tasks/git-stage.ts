import { execSync } from 'child_process';
import { existsSync } from 'fs';
import type { ReleaseConfig } from '../types.js';

export function stageReleaseFiles(config: ReleaseConfig): void {
  const { outputPdf, checksumsFile } = config;
  
  const files = [
    'CITATION.cff',
    '.zenodo.json',
    outputPdf,
    checksumsFile,
  ];
  
  const existingFiles = files.filter(f => existsSync(f));
  
  if (existingFiles.length === 0) {
    console.log('⚠ No files to stage');
    return;
  }
  
  execSync(`git add ${existingFiles.join(' ')}`, { stdio: 'inherit' });
  console.log(`✓ Staged files for commit: ${existingFiles.join(', ')}`);
}

