import { execSync } from 'child_process';
import { existsSync } from 'fs';

export function getCommitEpoch(): number {
  const epoch = execSync('git log -1 --pretty=%ct', { encoding: 'utf8' }).trim();
  return parseInt(epoch, 10);
}

export function stageFiles(files: string[]): void {
  const existingFiles = files.filter(f => existsSync(f));

  if (existingFiles.length === 0) {
    console.log('⚠ No files to stage');
    return;
  }

  execSync(`git add ${existingFiles.join(' ')}`, { stdio: 'inherit' });
  console.log(`✓ Staged files: ${existingFiles.join(', ')}`);
}

