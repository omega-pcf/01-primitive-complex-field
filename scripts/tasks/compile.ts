import { execSync } from 'child_process';
import { existsSync, renameSync } from 'fs';
import { getCommitEpoch } from '../utils/git.js';
import type { ReleaseConfig } from '../types.js';

// Usar kjarosh/latex por mejor versionado explícito
// Alternativa: blang/latex:ubuntu (más popular pero menos versionado)
const DOCKER_IMAGE = 'kjarosh/latex:2024.4-full';

export function compilePDF(config: ReleaseConfig): void {
  const { sourceTex, outputPdf } = config;
  const commitEpoch = getCommitEpoch();
  
  const dockerCmd = `docker run --rm \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e SOURCE_DATE_EPOCH=${commitEpoch} \
    -e LC_ALL=C \
    -e LANG=C \
    -e TZ=UTC \
    ${DOCKER_IMAGE} \
    pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`;
  
  console.log(`\n📄 Compiling PDF with SOURCE_DATE_EPOCH=${commitEpoch}...`);
  execSync(dockerCmd, { stdio: 'inherit' });
  
  const sourcePdf = 'build/main.pdf';
  if (!existsSync(sourcePdf)) {
    throw new Error(`PDF compilation failed - ${sourcePdf} not found`);
  }
  
  renameSync(sourcePdf, outputPdf);
  console.log(`✓ Compiled ${outputPdf} with SOURCE_DATE_EPOCH=${commitEpoch}`);
}

