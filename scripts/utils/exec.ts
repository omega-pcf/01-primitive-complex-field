import { execSync } from 'child_process';

export interface ExecOptions {
  cwd?: string;
  env?: NodeJS.ProcessEnv;
  stdio?: 'inherit' | 'pipe' | 'ignore';
}

export function exec(command: string, options: ExecOptions = {}): string {
  const { cwd, env, stdio = 'pipe' } = options;
  
  return execSync(command, {
    encoding: 'utf8',
    cwd,
    env: { ...process.env, ...env },
    stdio,
  }).trim();
}

export function execInherit(command: string, options: Omit<ExecOptions, 'stdio'> = {}): void {
  exec(command, { ...options, stdio: 'inherit' });
}

