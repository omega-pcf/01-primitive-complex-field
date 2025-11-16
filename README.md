[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.17619486.svg)](https://doi.org/10.5281/zenodo.17619486)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KExRnNtx91TjVyYD0FlcB_TLQwZB4GKq?usp=sharing)

# GENERAL INFORMATION

## Title of Dataset/Repository

**The Ω_PCF Operator and the Primitive Structure of the Complex Plane: From Mersenne to Riemann via Geometric Coupling φ-i-S₃**

This repository contains the LaTeX source files, computational verification code, and supplementary material for a reaserch paper developing the Ω_PCF operator as an analytical tool of the complex plane through three-dimensional modularization coupled to the golden ratio.

## Author/Principal Investigator Information

**Name:** Jorge Armando González García  
**ORCID:** N/A  
**Institution:** TTAMAYO PUNTO COM, S.A.P.I. de C.V.  
**Address:** Mexico  
**Email:** [GitHub Issues](https://github.com/omega-pcf/01-primitive-complex-field/issues)

## Author/Associate or Co-investigator Information

**Name:** Víctor Manuel González García  
**ORCID:** [0009-0009-0935-2954](https://orcid.org/0009-0009-0935-2954)  
**Institution:** TTAMAYO PUNTO COM, S.A.P.I. de C.V.  
**Address:** Mexico  
**Email:** [GitHub Issues](https://github.com/omega-pcf/01-primitive-complex-field/issues)

## Additional Authors

- **Itzel Marion Dressler Pérez** (Independent Researcher)
- **Luz María García Ordóñez** (TTAMAYO PUNTO COM, S.A.P.I. de C.V., Mexico)
- **Pablo Tenorio** (Independent Researcher)
- **Mario Moreno** (Independent Researcher)

**Date of data collection:** Ongoing research project  
**Geographic location of data collection:** Mexico  
**Information about funding sources:** Not specified

---

# SHARING/ACCESS INFORMATION

## Licenses/Restrictions

See LICENSE file for details.

## Links to Publications

- **Repository:** [GitHub Repository](https://github.com/omega-pcf/01-primitive-complex-field)
- **Preprint:** Available in repository (LaTeX source)

## Links to Other Publicly Accessible Locations

- **GitHub Repository:** https://github.com/omega-pcf/01-primitive-complex-field
- **Issue Tracker:** https://github.com/omega-pcf/01-primitive-complex-field/issues

## Links/Relationships to Ancillary Data Sets

Computational verification code and test suites are included in the `test/` directory. Supplementary material (appendices and resources) is available in `src/supplementary/`.

## Was Data Derived from Another Source?

No. This is original mathematical research.

## Recommended Citation

González García, J. A., González García, V. M., Dressler Pérez, I. M., García Ordóñez, L. M., Tenorio, P., & Moreno, M. (Year). *The Ω_PCF Operator and the Primitive Structure of the Complex Plane: From Mersenne to Riemann via Geometric Coupling φ-i-S₃*. [Preprint]. GitHub. https://github.com/omega-pcf/01-primitive-complex-field

---

# DATA & FILE OVERVIEW

## File List

### Main Document Files
- `main.tex` - Main LaTeX document entry point
- `lapreprint.cls` - LaPreprint document class (custom class based on eLife template)

### Source Files (`src/`)
- `src/chapters/` - Main content chapters:
  - `abstract.tex` - Abstract
  - `introduction.tex` - Introduction and historical context
  - `methods.tex` - Construction methods
  - `results.tex` - Results and findings
  - `discussion.tex` - Discussion and implications
  - `formal.tex` - Formal mathematical development
- `src/bibliography.bib` - Bibliographic references (BibLaTeX format)
- `src/figures/` - Figure files (images, diagrams)
- `src/images/` - Additional image files
- `src/tables/` - LaTeX table definitions
- `src/supplementary/` - Appendices and supplementary material:
  - `appendices.tex` - Appendices
  - `resources.tex` - Additional resources

### Computational Verification (`test/`)
- `test/` - Computational verification code and test suites for:
  - Spectral prediction verification
  - Mersenne prime verification
  - Precision analysis
  - Structural robustness tests

## Relationship Between Files

The document follows a hierarchical structure:
1. `main.tex` includes all chapter files from `src/chapters/`
2. `src/bibliography.bib` provides references cited throughout the document
3. Figures and tables are referenced from their respective directories
4. Supplementary material is included via `src/supplementary/`
5. Computational verification code in `test/` validates theoretical predictions independently

## Additional Related Data

Computational verification results and numerical data supporting the paper's claims are documented in the supplementary material and test suites.

## Are There Multiple Versions of the Dataset?

This is a version-controlled repository. Version history is available through Git.

---

# METHODOLOGICAL INFORMATION

## Description of Methods Used for Collection/Generation of Data

This repository contains:
1. **Mathematical manuscript** (LaTeX): Theoretical development of the Ω_PCF operator construction
2. **Computational verification code**: Numerical validation of theoretical predictions

The mathematical construction develops an operator as an analytical tool of the complex plane through:
- Multi-domain coherence bootstrap principles avoiding self-reference problems
- Three-dimensional modularization of the complex plane coupled to the golden ratio
- Geometric coupling φ-i-S₃ generating emergent hermiticity with constant magnitude |Ω| = 1/2
- Modular space interpretation: M_PCF = ℂ/Λ_PCF ≅ T² preserving all constituents of ℂ
- The operator is constructed independently of ζ(s); its spectrum exhibits correlation with zeros a posteriori

## Methods for Processing the Data

### Document Compilation

The LaTeX document is compiled using:
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

### Computational Verification

Verification code in `test/` directory includes:
- Tests for spectral predictions of ζ(s) zeros using formula λ_n = K_σ√t_n where K_σ = M_PCF/φ^σ
- Tests for logarithmic isomorphism between continuous golden tower R_σ = 3φ^σ and discrete Mersenne tower M_p = 2^p-1 (51 primes from M₂ to M₈₂₅₈₉₉₃₃)
- Precision analysis for results (n ~ 10¹⁰, height t ~ 10²³)
- Analysis of discrepancies and computational precision limits
- Verification that the operator maintains integrity when manipulating extremely large integers (Mersenne primes with millions of digits)

## Instrument- or Software-Specific Information

### Required Software

- **LaTeX Distribution:** TeX Live, MiKTeX, or MacTeX (with full installation)
- **BibLaTeX Backend:** Biber (included with modern LaTeX distributions)
- **PDF Viewer:** Any PDF viewer for compiled output

### Required LaTeX Packages

The document uses the LaPreprint class which loads:
- `babel` (Spanish/English)
- `amsmath`, `amsthm` (mathematical typesetting)
- `biblatex` with `biber` backend
- `hyperref` (hyperlinks)
- `snotez` (sidenotes)
- `tcolorbox` (theorem environments)
- And additional packages listed in `main.tex`

### Computational Verification Requirements

- Python 3.x (for test suites)
- Numerical libraries (numpy, scipy, mpmath) - as required by verification code
- High-precision arithmetic capabilities for Mersenne prime verification

### Standards and Calibration Information

- Mathematical notation follows standard conventions
- Theorem environments use AMS standard numbering (hierarchical: section.subsection.theorem)
- Computational precision is defined in the document (see definition of computational precision)

### Environmental/Experimental Conditions

- Document compilation: Standard LaTeX environment (Overleaf, TeXShop, TeXstudio, or command line)
- Computational verification: Standard scientific computing environment

### Quality-Assurance Procedures

- LaTeX compilation verified across multiple platforms
- Cross-references validated
- Bibliography consistency checked
- Computational verification code designed for reproducibility
- Numerical results validated against theoretical predictions

### People Involved

- **Mathematical Development:** All authors
- **Computational Verification:** See test suite documentation
- **Document Preparation:** All authors

---

# DATA-SPECIFIC INFORMATION

## For: LaTeX Source Files (`src/chapters/*.tex`)

**Number of files:** 6 main chapter files  
**Format:** LaTeX (.tex)  
**Encoding:** UTF-8  
**Structure:** Each file contains one major section of the paper

**File Descriptions:**
- `abstract.tex`: Abstract with keywords (Riemann hypothesis, Hilbert-Pólya conjecture, L-functions, Self-adjoint operators, Random matrix theory, Zeta function zeros, Mersenne primes, Modular spaces)
- `introduction.tex`: Historical context, obstacles, and scope
- `methods.tex`: Construction methodology
- `results.tex`: Results and computational verifications
- `discussion.tex`: Discussion and implications
- `formal.tex`: Rigorous mathematical development

**Specialized formats:** LaTeX mathematical notation, theorem environments, sidenotes

## For: Bibliography (`src/bibliography.bib`)

**Format:** BibLaTeX (.bib)  
**Encoding:** UTF-8  
**Structure:** Standard BibLaTeX format with entries for:
- Journal articles
- Preprints
- Books
- Conference proceedings

**Missing data codes:** N/A (bibliographic database)

## For: Computational Verification Code (`test/`)

**Number of test suites:** Multiple (see directory contents)  
**Format:** Python scripts, test files  
**Purpose:** Validate theoretical predictions through numerical computation

**Test Categories:**
- Spectral prediction accuracy tests
- Modular invariance verification
- Arithmetic correspondence validation (Mersenne primes)
- Precision limit analysis

**Dependencies:** Python 3.x, numerical libraries (as specified in test documentation)

## For: Supplementary Material (`src/supplementary/`)

**Files:**
- `appendices.tex`: Mathematical appendices
- `resources.tex`: Additional resources and parameters

**Format:** LaTeX (.tex)  
**Purpose:** Supplementary material referenced in main document

---

# ABSTRACT

Through multi-domain coherence bootstrap principles, we transcend self-reference problems of the Lawvere-Yanofsky type that have limited several previous attempts to construct the Hilbert-Pólya operator, as well as other approaches to the Riemann Hypothesis. We develop an operator as an analytical tool of the complex plane through three-dimensional modularization coupled to the golden ratio—a reorganization that preserves all constituents of ℂ while revealing underlying toroidal structure. Through lattice Λ_PCF and module M_PCF = ℂ/Λ_PCF ≅ T², unlike classical algebraic extensions that add new elements and may lose fundamental properties (e.g., octonions 𝕆 lose associativity). Our modularization preserves all properties of ℂ through geometric coupling φ-i-S₃. The rigidity of our construction preserves not only the known properties of ℂ, but also a rich spectrum of structures that emerge from multi-domain coherence. The generating matrix Ω̂ in ℂ³ is normal but not Hermitian. The matrix Ω̂ operates in component space ℂ³ encoding directionality of the tripartite structure (P, C, F) through symmetry S₃ of the equilateral triangle; its non-Hermiticity reflects the geometry of the system, not an algebraic defect. Meanwhile, the hermiticity of the integral operator in L²(ℝ) emerges from the construction mechanism through a symmetrized kernel—the kernel is constructed through terms δ(x-y) + ε(x,y) that introduce symmetrization, allowing hermiticity to emerge even though Ω̂ is not Hermitian—not from algebraic properties of Ω̂. The φ-i-S₃ coupling generates this emergent hermiticity with constant magnitude |Ω| = 1/2, establishing correspondence between self-similar scales of the complex plane. The constant module |Ω| = 1/2 acts as a functional fixed point that anchors the entire construction through distributed self-reference in tripartite structure P ↔ C ↔ F that avoids prohibited cycles D₁ → D₂ → D₁ identified by Lawvere and Yanofsky. This strategy avoids self-reference through multi-domain coherence with preserved invariants, formalized in conformal bootstrap by Guillarmou et al. and in modular bootstrap by Benjamin-Chang.

The operator's analysis reveals two fundamental structural correspondences. First, a logarithmic isomorphism between the continuous golden tower R_σ = 3φ^σ and the discrete Mersenne tower M_p = 2^p-1 through conversion factor λ = ln(2)/ln(φ) ≈ 1.440, where both towers are straight lines in logarithmic space with related slopes—a topological correspondence (preserves exponential structure) not metric, verified over more than 25 million orders of magnitude from M₂ to M₈₂₅₈₉₉₃₃, mediated by critical module |Ω| = 1/2 = 2⁻¹ that establishes the only possible bridge between golden and binary scaling. Second, spectral prediction of ζ(s) zeros through formula λ_n = K_σ√t_n where K_σ = M_PCF/φ^σ, with precision that improves asymptotically as height t increases (discrepancies < 10⁻¹⁴ in first 100 zeros, verified up to n ~ 10¹⁰ with height t ~ 8.3 × 10²³). The operator is constructed independently of ζ(s); its spectrum exhibits structural correlation with zeros a posteriori.

Numerical verification confirms the operator's structural robustness: observed discrepancies reflect computational precision limits, not mathematical deficiency. The operator maintains integrity even when manipulating extremely large integers (Mersenne primes with millions of digits), preserving invariants under the action of coupling φ-i-S₃ across all self-similar scales. This robustness—where discrete and continuous coexist coherently in the spectrum—demonstrates that the operator captures fundamental mathematical invariants of ℂ.

**Keywords:** Riemann hypothesis, Hilbert-Pólya conjecture, L-functions, Self-adjoint operators, Random matrix theory, Zeta function zeros, Mersenne primes, Modular spaces.

---

# CONTACT

For correspondence, please use the [GitHub Issues](https://github.com/omega-pcf/01-primitive-complex-field/issues) page.
