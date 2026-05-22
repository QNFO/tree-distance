# DEFINITION OF DONE — Tree Distance Sandbox

## What "Done" Means

This project is **done** when a visitor can click any 2 (or 3) points on a tree and instantly understand that ultrametric distance is qualitatively different from Euclidean distance, including the triadic rigidity property.

---

## GATE 1: FUNCTIONAL COMPLETENESS

| # | Requirement | Test | Status |
|:--|:-----------|:-----|:------|
| F1 | Tree renders with selectable leaf nodes | Click detection within 10px radius of each leaf | ❌ UNTESTED |
| F2 | Selecting 2 leaves displays all 3 distance values | Verify: cophenetic ≥ 0, ultrametric ∈ [0,1], Euclidean ≥ 0 | ❌ UNTESTED |
| F3 | LCA path highlighted between selected leaves | Visual verification: colored path from leaf A to leaf B via LCA | ❌ UNTESTED |
| F4 | **Triadic rigidity demonstration:** select 3 leaves → two of the three ultrametric distances are equal | Test: for 20 random leaf triples, verify min(d12,d13,d23) = mid(d12,d13,d23) | ❌ NOT BUILT |
| F5 | Distance values update on new selection within 50ms | Timing measurement | ❌ UNTESTED |
| F6 | Explanation panel describes what each distance metric means | Reader test: 3/3 readers can explain the 3 distance types | ❌ NOT BUILT |
| F7 | Cross-links to A1 (Error Confinement) and A3 (Convergence) | Verify links functional | ❌ NOT BUILT |

## GATE 2: TEST EXECUTION

### Test Suite 1: Distance Correctness
```
File: test_plan.py
Test: For tree p=3, d=4:
  1. Select all pairs of leaves
  2. Verify cophenetic distance = depth_of_LCA * 2
  3. Verify ultrametric distance = cophenetic / max_cophenetic
  4. Verify strong triangle inequality holds for all triples
Status: NOT YET WRITTEN
```

### Test Suite 2: Triadic Rigidity
```
File: test_plan.py
Test: For 100 random triples:
  1. Compute d12, d13, d23
  2. Sort: a ≤ b ≤ c
  3. Verify a = b (two smallest are equal — triadic rigidity)
Status: NOT YET WRITTEN
```

## GATE 3-5: Same standards as A1 (Deployment, QWAV Integration, Documentation)

---

## CURRENT STATUS vs DONE

| Gate | Requirements | Met | Status |
|:-----|:------------|:---|:------|
| GATE 1 | Functional (7 items) | 0/7 | 🔴 UNTESTED |
| GATE 2 | Test Execution (2 suites) | 0/2 | 🔴 NO TESTS |
| GATE 3 | Deployment | 4/6 | 🟡 URL loads |
| GATE 4 | QWAV Integration | 1/3 | 🔴 NO CROSS-LINKS |
| GATE 5 | Documentation | 1/4 | 🔴 BLOCKED |

**OVERALL:** 6/22 requirements met (27%). **Prototype — needs triadic rigidity demo, explanation, and tests.**

---

*Updated: 2026-05-23*
