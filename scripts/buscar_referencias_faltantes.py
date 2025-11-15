#!/usr/bin/env python3
"""
Script para encontrar referencias § en paper.md que faltan en los archivos .tex
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PAPER_MD = BASE_DIR / "paper.md"
TEX_DIR = BASE_DIR / "src" / "chapters"

def extract_all_section_refs(md_file):
    """Extrae todas las referencias § con su contexto"""
    refs = []
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        # Buscar referencias §X.Y.Z
        matches = re.finditer(r'§([0-9IXV]+(?:\.[0-9]+)*)', line)
        for match in matches:
            ref = match.group(1)
            context = line.strip()
            refs.append({
                'line': i,
                'reference': ref,
                'full_match': match.group(0),
                'context': context
            })
    
    return refs

def find_equivalent_text_in_tex(tex_dir, md_context, section_ref):
    """Busca texto equivalente en archivos .tex"""
    results = []
    
    # Normalizar contexto para búsqueda
    context_words = set(re.findall(r'\b\w+\b', md_context.lower()))
    
    for tex_file in tex_dir.glob('*.tex'):
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            line_lower = line.lower()
            line_words = set(re.findall(r'\b\w+\b', line_lower))
            
            # Si hay palabras clave en común, podría ser el texto equivalente
            common_words = context_words & line_words
            if len(common_words) >= 3:  # Al menos 3 palabras en común
                # Verificar si NO tiene referencia \ref{}
                if not re.search(r'\\ref\{[^}]+\}', line):
                    results.append({
                        'file': tex_file.name,
                        'line': i,
                        'content': line.strip(),
                        'common_words': len(common_words)
                    })
    
    return results

def main():
    print("Extrayendo referencias § de paper.md...")
    refs = extract_all_section_refs(PAPER_MD)
    print(f"Encontradas {len(refs)} referencias\n")
    
    print("Buscando referencias faltantes en .tex...\n")
    missing_refs = []
    
    for ref in refs:
        # Buscar texto equivalente en .tex
        equiv_texts = find_equivalent_text_in_tex(TEX_DIR, ref['context'], ref['reference'])
        
        if equiv_texts:
            # Verificar si alguna tiene \ref{}
            has_ref = any(re.search(r'\\ref\{[^}]+\}', t['content']) for t in equiv_texts)
            
            if not has_ref:
                missing_refs.append({
                    'md_ref': ref,
                    'tex_matches': equiv_texts
                })
    
    print(f"Referencias que podrían necesitar inserción: {len(missing_refs)}\n")
    
    for item in missing_refs[:20]:  # Mostrar primeras 20
        ref = item['md_ref']
        print(f"Línea {ref['line']} paper.md: §{ref['reference']}")
        print(f"  Contexto: {ref['context'][:80]}...")
        print(f"  Posibles ubicaciones en .tex:")
        for match in item['tex_matches'][:3]:  # Primeras 3 coincidencias
            print(f"    - {match['file']}:{match['line']} ({match['common_words']} palabras comunes)")
            print(f"      {match['content'][:80]}...")
        print()

if __name__ == '__main__':
    main()

