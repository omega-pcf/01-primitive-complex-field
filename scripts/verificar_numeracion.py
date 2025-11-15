#!/usr/bin/env python3
"""
Script para verificar inconsistencias en la numeración de secciones y teoremas.
Compila el documento y compara la numeración en el código fuente vs el PDF.
"""

import re
import subprocess
import sys
from pathlib import Path

# Colores para output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def find_numbered_sections(tex_file):
    """Encuentra todas las secciones numeradas en un archivo .tex"""
    content = tex_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    sections = []
    section_stack = [0, 0, 0]  # section, subsection, subsubsection
    
    for i, line in enumerate(lines, 1):
        if re.search(r'\\section\{', line):
            section_stack[0] += 1
            section_stack[1] = 0
            section_stack[2] = 0
            title = re.search(r'\\section\{([^}]+)', line)
            title = title.group(1) if title else ""
            sections.append(('section', f"{section_stack[0]}", title, i, tex_file.name))
        elif re.search(r'\\subsection\{', line):
            section_stack[1] += 1
            section_stack[2] = 0
            title = re.search(r'\\subsection\{([^}]+)', line)
            title = title.group(1) if title else ""
            num = f"{section_stack[0]}.{section_stack[1]}"
            sections.append(('subsection', num, title, i, tex_file.name))
        elif re.search(r'\\subsubsection\{', line):
            section_stack[2] += 1
            title = re.search(r'\\subsubsection\{([^}]+)', line)
            title = title.group(1) if title else ""
            num = f"{section_stack[0]}.{section_stack[1]}.{section_stack[2]}"
            sections.append(('subsubsection', num, title, i, tex_file.name))
    
    return sections

def find_theorems(tex_file):
    """Encuentra todas las construcciones matemáticas"""
    content = tex_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    theorems = []
    section_stack = [0, 0, 0]
    theorem_counter = 0
    current_subsection = None
    
    for i, line in enumerate(lines, 1):
        if re.search(r'\\section\{', line):
            section_stack[0] += 1
            section_stack[1] = 0
            section_stack[2] = 0
            theorem_counter = 0
        elif re.search(r'\\subsection\{', line):
            section_stack[1] += 1
            section_stack[2] = 0
            theorem_counter = 0
            current_subsection = f"{section_stack[0]}.{section_stack[1]}"
        elif re.search(r'\\subsubsection', line):
            section_stack[2] += 1
        
        match = re.search(r'\\begin\{(theorem|proposition|definition|lemma|corollary|construction|observation|example|remark|conjecture)\}', line)
        if match:
            theorem_counter += 1
            env_type = match.group(1)
            label_match = re.search(r'\\label\{([^}]+)', line)
            label = label_match.group(1) if label_match else ""
            expected_num = f"{current_subsection}.{theorem_counter}" if current_subsection else f"{theorem_counter}"
            theorems.append((env_type, expected_num, label, i, tex_file.name, current_subsection))
    
    return theorems

def compile_document():
    """Compila el documento LaTeX"""
    print(f"{Colors.BLUE}Compilando documento...{Colors.RESET}")
    
    build_dir = Path("build")
    for ext in ['.aux', '.toc', '.out']:
        for f in build_dir.glob(f"*{ext}"):
            try:
                f.unlink()
            except:
                pass
    
    for i in range(2):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory=build', 'main.tex'],
            capture_output=True,
            text=True,
            errors='replace'
        )
        if result.returncode != 0:
            print(f"{Colors.RED}✗ Error en compilación (paso {i+1}){Colors.RESET}")
            if result.stderr:
                print(result.stderr[:500])
            return False
    
    print(f"{Colors.GREEN}✓ Compilación exitosa{Colors.RESET}")
    return True

def extract_pdf_text():
    """Extrae texto del PDF compilado"""
    pdf_path = Path("build/main.pdf")
    if not pdf_path.exists():
        return None
    
    try:
        result = subprocess.run(
            ['pdftotext', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            errors='replace'
        )
        return result.stdout
    except:
        return None

def find_all_numberings_in_pdf(pdf_text):
    """Encuentra todas las numeraciones n.x.x en el PDF"""
    if not pdf_text:
        return []
    
    # Buscar todas las numeraciones tipo n.x o n.x.x
    pattern = r'\b(\d+\.\d+(?:\.\d+)?)\b'
    matches = []
    
    for match in re.finditer(pattern, pdf_text):
        num = match.group(1)
        pos = match.start()
        
        # Obtener contexto
        context_start = max(0, pos - 150)
        context_end = min(len(pdf_text), pos + 150)
        context = pdf_text[context_start:context_end]
        
        # Filtrar: debe estar cerca de palabras clave de secciones/teoremas
        context_lower = context.lower()
        keywords = ['sección', 'subsección', 'definición', 'proposición', 'teorema', 'lema', 
                   'corolario', 'construcción', 'observación', 'ejemplo', 'nota', 'conjetura',
                   'section', 'subsection', 'definition', 'proposition', 'theorem', 'lemma']
        
        if any(keyword in context_lower for keyword in keywords):
            # Excluir si es parte de una fórmula matemática
            if not re.search(r'[=≈×·]|rad|°|^\d+\.\d+$', context):
                matches.append((num, pos, context))
    
    return matches

def check_consistencies():
    """Función principal"""
    print(f"{Colors.BLUE}{'='*80}{Colors.RESET}")
    print(f"{Colors.BLUE}VERIFICACIÓN DE NUMERACIÓN{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*80}{Colors.RESET}\n")
    
    # 1. Analizar código fuente
    print(f"{Colors.BLUE}1. Analizando código fuente...{Colors.RESET}")
    chapters_dir = Path("src/chapters")
    all_sections = []
    all_theorems = []
    
    for tex_file in sorted(chapters_dir.glob("*.tex")):
        sections = find_numbered_sections(tex_file)
        theorems = find_theorems(tex_file)
        all_sections.extend(sections)
        all_theorems.extend(theorems)
    
    print(f"  ✓ {len(all_sections)} secciones encontradas")
    print(f"  ✓ {len(all_theorems)} construcciones matemáticas encontradas")
    
    # 2. Compilar
    print(f"\n{Colors.BLUE}2. Compilando documento...{Colors.RESET}")
    if not compile_document():
        return False
    
    # 3. Extraer PDF
    print(f"\n{Colors.BLUE}3. Extrayendo texto del PDF...{Colors.RESET}")
    pdf_text = extract_pdf_text()
    
    if not pdf_text:
        print(f"{Colors.YELLOW}⚠ No se pudo extraer texto del PDF{Colors.RESET}")
        return False
    
    # 4. Buscar todas las numeraciones en PDF
    print(f"\n{Colors.BLUE}4. Buscando TODAS las numeraciones n.x.x en el PDF...{Colors.RESET}")
    pdf_numberings = find_all_numberings_in_pdf(pdf_text)
    
    # Agrupar por número
    numbering_counts = {}
    for num, pos, context in pdf_numberings:
        if num not in numbering_counts:
            numbering_counts[num] = []
        numbering_counts[num].append((pos, context))
    
    print(f"  ✓ Encontradas {len(pdf_numberings)} numeraciones tipo sección/teorema")
    print(f"  ✓ {len(numbering_counts)} números únicos")
    
    # 5. Comparar con código fuente
    print(f"\n{Colors.BLUE}5. Comparando con código fuente...{Colors.RESET}")
    
    # Crear sets de numeraciones esperadas
    expected_section_nums = {num for _, num, _, _, _ in all_sections}
    expected_theorem_nums = {num for _, num, _, _, _, _ in all_theorems}
    all_expected = expected_section_nums | expected_theorem_nums
    
    # Encontrar inconsistencias
    inconsistencies = []
    for pdf_num in sorted(numbering_counts.keys()):
        if pdf_num not in all_expected:
            # Verificar si es similar a alguna esperada (puede ser un error de offset)
            is_similar = False
            for expected in all_expected:
                # Comparar estructura: si difiere en un nivel, puede ser problema
                pdf_parts = pdf_num.split('.')
                exp_parts = expected.split('.')
                if len(pdf_parts) == len(exp_parts):
                    # Si solo difiere en el último número, puede ser problema de contador
                    if pdf_parts[:-1] == exp_parts[:-1]:
                        is_similar = True
                        inconsistencies.append(('similar', pdf_num, expected, 
                                              f"Similar a {expected} pero diferente"))
                        break
            
            if not is_similar:
                # Verificar contexto para determinar tipo
                sample_context = numbering_counts[pdf_num][0][1].lower()
                if any(kw in sample_context for kw in ['definición', 'proposición', 'teorema']):
                    inconsistencies.append(('theorem', pdf_num, None, 
                                          f"Encontrada en PDF, no en código fuente"))
                else:
                    inconsistencies.append(('section', pdf_num, None, 
                                          f"Encontrada en PDF, no en código fuente"))
    
    # Mostrar resultados
    if inconsistencies:
        print(f"\n{Colors.RED}✗ INCONSISTENCIAS ENCONTRADAS: {len(inconsistencies)}{Colors.RESET}\n")
        
        # Agrupar por tipo
        by_type = {'section': [], 'theorem': [], 'similar': []}
        for inc in inconsistencies:
            by_type[inc[0]].append(inc)
        
        if by_type['similar']:
            print(f"{Colors.YELLOW}⚠ Numeraciones similares (posible error de offset):{Colors.RESET}")
            for inc_type, pdf_num, expected, reason in by_type['similar'][:20]:
                print(f"  PDF: {pdf_num:10} | Esperado: {expected:10} | {reason}")
        
        if by_type['theorem']:
            print(f"\n{Colors.RED}✗ Teoremas/Definiciones con numeración incorrecta:{Colors.RESET}")
            for inc_type, pdf_num, expected, reason in by_type['theorem'][:20]:
                count = len(numbering_counts[pdf_num])
                print(f"  {pdf_num:10} | {count:3} ocurrencias | {reason}")
                # Mostrar una muestra de contexto
                sample = numbering_counts[pdf_num][0][1]
                print(f"    Contexto: ...{sample[:100]}...")
        
        if by_type['section']:
            print(f"\n{Colors.RED}✗ Secciones con numeración incorrecta:{Colors.RESET}")
            for inc_type, pdf_num, expected, reason in by_type['section'][:20]:
                count = len(numbering_counts[pdf_num])
                print(f"  {pdf_num:10} | {count:3} ocurrencias | {reason}")
    else:
        print(f"{Colors.GREEN}✓ No se encontraron inconsistencias{Colors.RESET}")
    
    # Resumen
    print(f"\n{Colors.BLUE}{'='*80}{Colors.RESET}")
    print(f"{Colors.BLUE}RESUMEN{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*80}{Colors.RESET}")
    print(f"  Secciones en código: {len(all_sections)}")
    print(f"  Teoremas en código: {len(all_theorems)}")
    print(f"  Numeraciones en PDF: {len(pdf_numberings)}")
    print(f"  Inconsistencias: {len(inconsistencies)}")
    
    return len(inconsistencies) == 0

if __name__ == "__main__":
    try:
        success = check_consistencies()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrumpido{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}✗ Error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
