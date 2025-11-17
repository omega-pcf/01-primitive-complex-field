import { existsSync, mkdirSync, renameSync, readFileSync, writeFileSync } from 'fs';
import { dirname } from 'path';

export function ensureDirectory(path: string): void {
  const dir = dirname(path);
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
}

export function ensureFileExists(filePath: string, errorMessage: string): void {
  if (!existsSync(filePath)) {
    throw new Error(errorMessage);
  }
}

export function readTextFile(filePath: string): string {
  return readFileSync(filePath, 'utf8');
}

export function writeTextFile(filePath: string, content: string): void {
  ensureDirectory(filePath);
  writeFileSync(filePath, content, 'utf8');
}

export function moveFile(source: string, target: string): void {
  ensureDirectory(target);
  renameSync(source, target);
}

