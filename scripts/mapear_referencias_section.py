#!/usr/bin/env python3
"""
Script para mapear referencias con símbolo § de paper.md a labels de LaTeX en archivos .tex
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# Rutas
BASE_DIR = Path(__file__).parent.parent
PAPER_MD = BASE_DIR / "paper.md"
TEX_DIR = BASE_DIR / "src" / "chapters"

def extract_section_references(md_file):
    """Extrae todas las referencias § del paper.md"""
    references = []
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        # Buscar referencias §X.Y.Z
        matches = re.finditer(r'§([0-9IXV]+(?:\.[0-9]+)*)', line)
        for match in matches:
            ref = match.group(1)
            context_start = max(0, i - 2)
            context_end = min(len(lines), i + 2)
            context = ''.join(lines[context_start:context_end])
            references.append({
                'line': i,
                'reference': ref,
                'full_match': match.group(0),
                'context': context
            })
    
    return references

def find_section_in_md(md_file, section_num):
    """Busca una sección en paper.md por su numeración"""
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Normalizar la búsqueda
    section_num_clean = section_num.strip()
    
    # Buscar títulos de sección que coincidan
    patterns = [
        rf'^###? {re.escape(section_num_clean)}\s',  # ### 2.5 o ## 2.5
        rf'^###? {re.escape(section_num_clean)}\\',  # ### 2.5\ (con escape)
    ]
    
    for i, line in enumerate(lines, 1):
        for pattern in patterns:
            if re.match(pattern, line):
                # Extraer título
                title = re.sub(r'^###?\s*[0-9IXV.]+\\?\s*', '', line).strip()
                title = re.sub(r'\*\*', '', title)  # Remover markdown bold
                return {
                    'line': i,
                    'title': title,
                    'full_line': line.strip()
                }
    
    return None

def find_label_in_tex(tex_dir, section_title, section_num):
    """Busca el label correspondiente en archivos .tex"""
    labels = []
    
    # Normalizar título para búsqueda
    title_clean = re.sub(r'[^\w\s]', '', section_title.lower())
    title_words = set(title_clean.split())
    
    for tex_file in tex_dir.glob('*.tex'):
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Buscar secciones con títulos similares
        for i, line in enumerate(lines):
            # Buscar \section, \subsection, \subsubsection con labels
            section_match = re.search(r'\\(?:sub)*section\{([^}]+)\}\\label\{([^}]+)\}', line)
            if section_match:
                tex_title = section_match.group(1)
                label = section_match.group(2)
                
                # Comparar títulos
                tex_title_clean = re.sub(r'[^\w\s]', '', tex_title.lower())
                tex_title_words = set(tex_title_clean.split())
                
                # Si hay palabras clave en común, es probable que sea la misma sección
                common_words = title_words & tex_title_words
                if len(common_words) >= 2 or (len(common_words) >= 1 and len(title_words) <= 3):
                    labels.append({
                        'file': tex_file.name,
                        'line': i + 1,
                        'title': tex_title,
                        'label': label,
                        'full_line': line
                    })
    
    return labels

def find_hardcoded_refs_in_tex(tex_dir):
    """Busca referencias hardcodeadas en archivos .tex"""
    hardcoded = []
    
    for tex_file in tex_dir.glob('*.tex'):
        with open(tex_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines, 1):
            # Buscar referencias con § o \S seguido de números
            if re.search(r'[§\\]S\s*[0-9IXV]+(?:\.[0-9]+)*', line):
                hardcoded.append({
                    'file': tex_file.name,
                    'line': i,
                    'content': line.strip()
                })
    
    return hardcoded

def main():
    print("Extrayendo referencias de paper.md...")
    references = extract_section_references(PAPER_MD)
    print(f"Encontradas {len(references)} referencias")
    
    print("\nBuscando secciones correspondientes...")
    mapping = defaultdict(list)
    
    for ref in references:
        section = find_section_in_md(PAPER_MD, ref['reference'])
        if section:
            ref['section_info'] = section
            mapping[ref['reference']].append(ref)
        else:
            print(f"  ⚠️  No se encontró sección para §{ref['reference']} (línea {ref['line']})")
    
    print(f"\nMapeando a labels de LaTeX...")
    for section_num, refs in mapping.items():
        if refs and 'section_info' in refs[0]:
            section_title = refs[0]['section_info']['title']
            labels = find_label_in_tex(TEX_DIR, section_title, section_num)
            if labels:
                print(f"  §{section_num}: {section_title}")
                for label in labels:
                    print(f"    → {label['file']}:{label['line']} \\label{{{label['label']}}}")
            else:
                print(f"  ⚠️  §{section_num}: {section_title} - No se encontró label")
    
    print("\nBuscando referencias hardcodeadas en .tex...")
    hardcoded = find_hardcoded_refs_in_tex(TEX_DIR)
    if hardcoded:
        print(f"Encontradas {len(hardcoded)} referencias hardcodeadas:")
        for h in hardcoded:
            print(f"  {h['file']}:{h['line']}: {h['content'][:80]}")
    else:
        print("  ✓ No se encontraron referencias hardcodeadas")
    
    # Generar reporte
    report_file = BASE_DIR / "docs" / "reports" / "MAPEO_REFERENCIAS_SECTION.md"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Mapeo de Referencias con Símbolo §\n\n")
        f.write(f"**Total de referencias encontradas**: {len(references)}\n\n")
        f.write("## Referencias por Sección\n\n")
        
        for section_num in sorted(mapping.keys(), key=lambda x: (len(x.split('.')), x)):
            refs = mapping[section_num]
            if refs and 'section_info' in refs[0]:
                section_title = refs[0]['section_info']['title']
                f.write(f"### §{section_num}: {section_title}\n\n")
                f.write(f"**Ubicación en paper.md**: Línea {refs[0]['section_info']['line']}\n\n")
                
                labels = find_label_in_tex(TEX_DIR, section_title, section_num)
                if labels:
                    f.write("**Labels en .tex**:\n")
                    for label in labels:
                        f.write(f"- `\\label{{{label['label']}}}` en {label['file']}:{label['line']}\n")
                    f.write("\n")
                
                f.write(f"**Referencias encontradas** ({len(refs)}):\n")
                for ref in refs:
                    f.write(f"- Línea {ref['line']}: `{ref['full_match']}`\n")
                f.write("\n")
    
    print(f"\n✓ Reporte generado en {report_file}")

if __name__ == '__main__':
    main()

