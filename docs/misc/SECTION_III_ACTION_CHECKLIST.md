# SECTION III PHASE 1B ACTION CHECKLIST

## ANALYSIS DOCUMENT LOCATION
- Main Analysis: `SECTION_III_ANALYSIS.md`
- Quick Reference: `SECTION_III_QUICK_REFERENCE.txt`
- This Checklist: `SECTION_III_ACTION_CHECKLIST.md`

---

## PRE-CONVERSION FIXES (MUST DO FIRST)

### Fix #1: III.3 Duplicate Numbering Crisis
**Severity:** CRITICAL  
**File:** `src/chapters/methods.tex`  
**Affected Lines:** 719-803 and 838-1142

**Tasks:**
- [ ] Line 719: Find text `\textbf{Definición 3.3.1 (Cilindro base)}`
      Replace with: `\textbf{Definición 3.3.9 (Cilindro base)}`

- [ ] Line 751: Find text `\textbf{Proposición 3.3.2 (Verificación del cilindro)}`
      Replace with: `\textbf{Proposición 3.3.10 (Verificación del cilindro)}`

- [ ] Line 803: Find text `\textbf{Proposición 3.3.3 (Separación angular)}`
      Replace with: `\textbf{Proposición 3.3.11 (Separación angular)}`

- [ ] Lines 838-1142: For all items numbered 3.3.11 through 3.3.29, ADD 1 to each number:
      - 3.3.11 → 3.3.12
      - 3.3.12 → 3.3.13
      - ... (continue for all)
      - 3.3.29 → 3.3.30
      
      **Tool Tip:** Use Find & Replace with careful regex:
      ```
      Find:    \textbf{([A-Z]+ 3\.3\.(\d+))
      Replace: \textbf{$1 (with manual number increment check)
      ```
      OR manually edit each (28 items total):
      Line 838 (11→12), 852 (12→13), 861 (13→14), 879 (14→15), 897 (15→16),
      914 (16→17), 955 (17→18), 969 (18→19), 982 (19→20), 997 (20→21),
      1016 (21→22), 1024 (22→23), 1032 (23→24), 1046 (24→25), 1084 (25→26),
      1098 (26→27), 1116 (27→28), 1128 (28→29), 1132 (29→30)

**Verification:**
- [ ] After fix, items 3.3.1-3.3.8 appear in lines 648-690 (FIRST group)
- [ ] After fix, items 3.3.9-3.3.11 appear in lines 719-803 (SECOND group)
- [ ] After fix, items 3.3.12-3.3.30 appear in lines 838-1142 (THIRD group)
- [ ] No duplicate numbers exist
- [ ] Sequential numbering 3.3.1 through 3.3.30 with no gaps

---

### Fix #2: III.4 Missing Number
**Severity:** MEDIUM  
**File:** `src/chapters/methods.tex`  
**Affected Lines:** 1239-1252

**Investigation Tasks:**
- [ ] Read lines 1239-1252 carefully
- [ ] Check if content between 3.4.10 and 3.4.12 should be numbered 3.4.11
- [ ] If YES: Add new item and number as 3.4.11, renumber 3.4.12-15 to 3.4.13-16
- [ ] If NO: Renumber all items 3.4.12-15 to 3.4.11-14

**Expected Outcome:**
- [ ] Either sequential 3.4.1 through 3.4.15 (if we ADD 3.4.11)
- [ ] OR sequential 3.4.1 through 3.4.14 (if we REMOVE gap)

---

### Fix #3: III.5 Wrong Subsection Number
**Severity:** HIGH  
**File:** `src/chapters/methods.tex`  
**Affected Line:** 1378

**Task:**
- [ ] Line 1378: Find text `\textbf{Definición 3.4.8 (Base extendida)}`
      Replace with: `\textbf{Definición 3.5.8 (Base extendida)}`

**Verification:**
- [ ] After fix, all items in III.5 (lines ~1322-1532) have numbers starting with 3.5.
- [ ] No item in III.5 has number starting with 3.4.

---

### Fix #4: III.8 Nested Numbering Decision
**Severity:** MEDIUM  
**File:** `src/chapters/methods.tex`  
**Affected Lines:** 1728, 1860

**Decision Required (Pick ONE):**

**OPTION A: Keep as nested (less disruptive)**
- [ ] Accept 3.8.3.2 as valid nested numbering
- [ ] Note: This is non-standard for amsthm, may need special handling in conversion
- [ ] No renumbering needed now

**OPTION B: Convert to sequential (standard)**
- [ ] Line 1860: Change `3.8.3.2` to `3.8.4`
- [ ] Line 1869: Change `3.8.4` to `3.8.5`
- [ ] Line 1879: Change `3.8.5` to `3.8.6`
- [ ] Line 1888: Change `3.8.6` to `3.8.7`
- [ ] Line 1897: Change `3.8.7` to `3.8.8`
- [ ] Line 1899: Change `3.8.8` to `3.8.9`
- [ ] Line 1909: Change `3.8.9` to `3.8.10`
- [ ] Line 1928: Change `3.8.10` to `3.8.11`

**Recommendation:** OPTION B (for consistency with amsthm standard)

**Verification:**
- [ ] Final count: Either 10 items (3.8.1-3.8.10) with one nested, 
       OR 11 items (3.8.1-3.8.11) all sequential

---

## CONVERSION TO AMSTHM (AFTER PRE-FIXES)

### Round 1: No Dependencies (Start Immediately After Fixes)

#### III.2: Construcción desde el Módulo (13 items)
**Lines:** 481-643  
**Items:** 6 Definitions + 5 Propositions + 1 Lemma + 1 Corollary

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.2.X items (e.g., `def:matrix-generator`, `prop:algebraic-props`, etc.)
- [ ] Convert all \textbf{Definición 3.2.X} → \begin{definition}...\end{definition}
- [ ] Convert all \textbf{Proposición 3.2.X} → \begin{proposition}...\end{proposition}
- [ ] Convert all \textbf{Lema 3.2.X} → \begin{lemma}...\end{lemma}
- [ ] Convert all \textbf{Corolario 3.2.X} → \begin{corollary}...\end{corollary}
- [ ] Add \label{} commands to each environment
- [ ] Verify no \ref{} or \pageref{} commands break

**Items to Convert:**
- [ ] Line 494: Definición 3.2.0
- [ ] Line 506: Proposición 3.2.0.1
- [ ] Line 557: Definición 3.2.1
- [ ] Line 562: Proposición 3.2.2
- [ ] Line 571: Lema 3.2.3
- [ ] Line 586: Definición 3.2.4
- [ ] Line 591: Definición 3.2.5
- [ ] Line 598: Proposición 3.2.6
- [ ] Line 603: Proposición 3.2.7
- [ ] Line 611: Definición 3.2.8
- [ ] Line 623: Definición 3.2.9
- [ ] Line 628: Proposición 3.2.10
- [ ] Line 642: Corolario 3.2.11

---

#### III.6: Rotación de Wick (8 items)
**Lines:** 1534-1619  
**Items:** 3 Propositions + 2 Definitions + 2 Theorems + 1 Corollary

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.6.X items
- [ ] Convert all items to appropriate amsthm environments
- [ ] Add \label{} commands
- [ ] Verify references work

**Items to Convert:**
- [ ] Line 1538: Proposición 3.6.1
- [ ] Line 1545: Proposición 3.6.2
- [ ] Line 1550: Definición 3.6.3
- [ ] Line 1555: Proposición 3.6.4
- [ ] Line 1562: Definición 3.6.5
- [ ] Line 1576: Teorema 3.6.6
- [ ] Line 1599: Teorema 3.6.7
- [ ] Line 1616: Corolario 3.6.8

---

#### III.7: Métrica Logarítmica (1 item)
**Lines:** 1621-1654  
**Items:** 1 Proposition

**Conversion Tasks:**
- [ ] Convert item 3.7.2 to \begin{proposition}...\end{proposition}
- [ ] Add label

**Item to Convert:**
- [ ] Line 1635: Proposición 3.7.2

---

### Round 2: After Numbering Fixes

#### III.4: Proyección al Plano Complejo (15 items)
**Lines:** 1143-1532  
**Items:** 3 Definitions + 5 Propositions + 3 Theorems + 1 Corollary + 3 Observations

**Prerequisite:** Fix #2 must be completed (resolve 3.4.11 issue)

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.4.X items
- [ ] Convert all items to appropriate amsthm environments
- [ ] NOTE: Some "Observations" may use custom environment or amsthm

**Items to Convert:** (List all 15)
- [ ] Line 1149: Definición 3.4.1
- [ ] Line 1156: Proposición 3.4.2
- [ ] Line 1163: Observación 3.4.3
- [ ] Line 1167: Teorema 3.4.4
- [ ] Line 1173: Definición 3.4.5
- [ ] Line 1180: Teorema 3.4.6
- [ ] Line 1200: Corolario 3.4.7
- [ ] Line 1209: Observación 3.4.8
- [ ] Line 1225: Teorema 3.4.9
- [ ] Line 1239: Proposición 3.4.10
- [ ] Line 1252: Definición 3.4.12 (or 3.4.11 after fix)
- [ ] Line 1257: Proposición 3.4.13 (or 3.4.12)
- [ ] Line 1266: Teorema 3.4.14 (or 3.4.13)
- [ ] Line 1273: Observación 3.4.15 (or 3.4.14)

---

#### III.5: Espacio Adjunto (14 items)
**Lines:** ~1322-1532  
**Items:** 3 Definitions + 5 Propositions + 2 Theorems + 2 Corollaries + 2 Observations

**Prerequisite:** Fix #3 must be completed (change 3.4.8 to 3.5.8)

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.5.X items
- [ ] Convert all items to appropriate amsthm environments
- [ ] Verify that 3.5.8 (formerly 3.4.8) gets correct label

**Items to Convert:**
- [ ] Line 1322: Definición 3.5.1
- [ ] Line 1327: Proposición 3.5.2
- [ ] Line 1341: Proposición 3.5.3
- [ ] Line 1351: Observación 3.5.4
- [ ] Line 1363: Corolario 3.5.5
- [ ] Line 1367: Proposición 3.5.6
- [ ] Line 1374: Corolario 3.5.7
- [ ] Line 1378: Definición 3.5.8 (AFTER FIX #3)
- [ ] Line 1397: Proposición 3.5.9
- [ ] Line 1413: Teorema 3.5.10
- [ ] Line 1452: Teorema 3.5.11
- [ ] Line 1488: Proposición 3.5.12
- [ ] Line 1509: Observación 3.5.13
- [ ] Line 1520: Proposición 3.5.14

---

### Round 3: After Duplicate Fix

#### III.3: Geometría del Círculo (30 items, formerly 29)
**Lines:** 644-1142  
**Items:** ~4 Definitions + ~13 Propositions + ~6 Theorems + ~4 Corollaries + ~6 Observations

**Prerequisite:** Fix #1 must be completed (renumber duplicates)

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.3.X items
- [ ] Convert all items to appropriate amsthm environments
- [ ] NOTE: Large subsection with multiple nested subsubsections - take care with structure
- [ ] Consider if subsubsection headings need special formatting

**Items to Convert:** (30 items total)
- [ ] Line 648: Proposición 3.3.1
- [ ] Line 653: Corolario 3.3.2
- [ ] Line 660: Proposición 3.3.3
- [ ] Line 670: Corolario 3.3.4
- [ ] Line 677: Observación 3.3.5
- [ ] Line 681: Observación 3.3.6
- [ ] Line 685: Definición 3.3.7
- [ ] Line 690: Proposición 3.3.8
- [ ] Line 719: Definición 3.3.9 (AFTER FIX #1, was 3.3.1)
- [ ] Line 751: Proposición 3.3.10 (AFTER FIX #1, was 3.3.2)
- [ ] Line 803: Proposición 3.3.11 (AFTER FIX #1, was 3.3.3)
- [ ] Line 838: Proposición 3.3.12 (AFTER FIX #1, was 3.3.11)
- [ ] Line 852: Observación 3.3.13 (AFTER FIX #1, was 3.3.12)
- [ ] Line 861: Definición 3.3.14 (AFTER FIX #1, was 3.3.13)
- [ ] Line 879: Teorema 3.3.15 (AFTER FIX #1, was 3.3.14)
- [ ] Line 897: Proposición 3.3.16 (AFTER FIX #1, was 3.3.15)
- [ ] Line 914: Teorema 3.3.17 (AFTER FIX #1, was 3.3.16)
- [ ] Line 955: Corolario 3.3.18 (AFTER FIX #1, was 3.3.17)
- [ ] Line 969: Proposición 3.3.19 (AFTER FIX #1, was 3.3.18)
- [ ] Line 982: Teorema 3.3.20 (AFTER FIX #1, was 3.3.19)
- [ ] Line 997: Proposición 3.3.21 (AFTER FIX #1, was 3.3.20)
- [ ] Line 1016: Teorema 3.3.22 (AFTER FIX #1, was 3.3.21)
- [ ] Line 1024: Observación 3.3.23 (AFTER FIX #1, was 3.3.22)
- [ ] Line 1032: Proposición 3.3.24 (AFTER FIX #1, was 3.3.23)
- [ ] Line 1046: Teorema 3.3.25 (AFTER FIX #1, was 3.3.24)
- [ ] Line 1084: Corolario 3.3.26 (AFTER FIX #1, was 3.3.25)
- [ ] Line 1098: Proposición 3.3.27 (AFTER FIX #1, was 3.3.26)
- [ ] Line 1116: Teorema 3.3.28 (AFTER FIX #1, was 3.3.27)
- [ ] Line 1128: Proposición 3.3.29 (AFTER FIX #1, was 3.3.28)
- [ ] Line 1132: Observación 3.3.30 (AFTER FIX #1, was 3.3.29)

---

### Round 4: Final Sections

#### III.1: Axiomas (Complete Partial Conversion)
**Lines:** 330-479  
**Items:** 11 (PARTIAL conversion, need to finish)

**Items Already converted:** 11 amsthm items  
**Items Still \textbf:** 2 items (Observation at line 350, Remark at line 386)

**Conversion Tasks:**
- [ ] Convert Observation at line 350 to \begin{observation}...\end{observation}
- [ ] Convert Remark at line 386 to \begin{remark}...\end{remark}
- [ ] Add \label{} to these items
- [ ] Ensure consistency with other III.1 items

**Items to Complete:**
- [ ] Line 350: Observation (Singularidad estructural)
- [ ] Line 386: Remark (Convención notacional)

---

#### III.8: Funcionalización: Espacio de Hilbert (10 items)
**Lines:** 1655-1935  
**Items:** 1 Definition + 5 Theorems + 3 Propositions + 2 Corollaries

**Prerequisite:** Fix #4 must be completed (resolve 3.8.3.2 nesting)

**Conversion Tasks:**
- [ ] Create labeling scheme for 3.8.X items
- [ ] Convert all items to appropriate amsthm environments
- [ ] Handle 3.8.3.2 (now 3.8.4 if using Option B) carefully

**Items to Convert:**
- [ ] Line 1659: Proposición 3.8.1
- [ ] Line 1688: Definición 3.8.2
- [ ] Line 1728: Teorema 3.8.3
- [ ] Line 1860: Teorema 3.8.3.2 (or 3.8.4 AFTER FIX #4)
- [ ] Line 1869: Proposición 3.8.4 (or 3.8.5)
- [ ] Line 1879: Teorema 3.8.5 (or 3.8.6)
- [ ] Line 1888: Teorema 3.8.6 (or 3.8.7)
- [ ] Line 1897: Corolario 3.8.7 (or 3.8.8)
- [ ] Line 1899: Proposición 3.8.8 (or 3.8.9)
- [ ] Line 1909: Teorema 3.8.9 (or 3.8.10)
- [ ] Line 1928: Corolario 3.8.10 (or 3.8.11)

---

## VERIFICATION CHECKLIST (After All Conversions)

### Structural Verification
- [ ] All items in III.1 through III.8 use \begin{type}...\end{type} format
- [ ] No \textbf{Definición/Proposición/etc.} remains in Section III
- [ ] All items have \label{} commands
- [ ] All items have appropriate [Optional Title] in square brackets

### Numbering Verification
- [ ] III.1: Items numbered 1.1 through 1.5 (in amsthm) + standalone items
- [ ] III.2: Items numbered 3.2.0 through 3.2.11 (sequential, no gaps)
- [ ] III.3: Items numbered 3.3.1 through 3.3.30 (sequential, no gaps, no duplicates)
- [ ] III.4: Items numbered 3.4.1 through 3.4.15 or 3.4.14 (after fix #2)
- [ ] III.5: Items numbered 3.5.1 through 3.5.14 (with 3.5.8 correctly labeled)
- [ ] III.6: Items numbered 3.6.1 through 3.6.8 (sequential, no gaps)
- [ ] III.7: Item numbered 3.7.2 (only one item)
- [ ] III.8: Items numbered 3.8.1 through 3.8.10 or 3.8.11 (depending on fix #4)

### Reference Verification
- [ ] No broken \ref{} commands
- [ ] No broken \pageref{} commands
- [ ] All \label{} names are unique
- [ ] All label names follow consistent naming scheme

### File Compilation
- [ ] LaTeX compilation successful
- [ ] No undefined references
- [ ] PDF generated without errors
- [ ] Numbering displays correctly in PDF

---

## EXECUTION TIMELINE

**Estimated Timeline:** 6-8 hours total (depending on automation)

**Phase 1 (Pre-Fixes): 1-2 hours**
- Fix #1: III.3 duplicates (30 minutes with careful Find & Replace)
- Fix #2: III.4 missing number (15 minutes for investigation + decision)
- Fix #3: III.5 wrong number (5 minutes)
- Fix #4: III.8 nesting decision (5 minutes)

**Phase 2 (Round 1 Conversions): 1.5-2 hours**
- III.2 (13 items): 30 minutes
- III.6 (8 items): 20 minutes
- III.7 (1 item): 5 minutes
- Testing/Verification: 20 minutes

**Phase 3 (Round 2 Conversions): 1.5 hours**
- III.4 (15 items): 40 minutes
- III.5 (14 items): 40 minutes
- Testing/Verification: 15 minutes

**Phase 4 (Round 3 Conversions): 2 hours**
- III.3 (30 items): 80 minutes (largest section)
- Testing/Verification: 20 minutes

**Phase 5 (Final Round): 1 hour**
- III.1 (2 items remaining): 10 minutes
- III.8 (10 items): 30 minutes
- Final full verification: 20 minutes

---

## SUCCESS CRITERIA

1. No duplicate item numbers in entire Section III
2. No gaps in sequential numbering (3.X.Y continuous)
3. All items use correct amsthm format
4. All items have unique \label{} commands
5. All items have [Optional Title] in appropriate format
6. LaTeX compilation succeeds
7. PDF renders without errors
8. All cross-references work correctly
9. Document structure clear and navigable

