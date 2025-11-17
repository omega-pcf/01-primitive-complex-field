import { parse, stringify } from 'yaml';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import type { CitationFile } from '../types.js';

const CITATION_PATH = 'CITATION.cff';

export function updateCitationDate(): void {
  if (!existsSync(CITATION_PATH)) {
    throw new Error(`CITATION.cff not found at ${CITATION_PATH}`);
  }
  
  const content = readFileSync(CITATION_PATH, 'utf8');
  const citation = parse(content) as CitationFile;
  
  citation['date-released'] = new Date().toISOString().split('T')[0];
  
  writeFileSync(CITATION_PATH, stringify(citation));
  console.log(`✓ Updated date-released to ${citation['date-released']}`);
}

