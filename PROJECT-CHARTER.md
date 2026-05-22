# PROJECT CHARTER — Tree Distance Sandbox

## 1. PROJECT IDENTITY

| Field | Value |
|:------|:------|
| **Project Name** | `tree-distance-sandbox` |
| **Title** | Tree Distance Sandbox |
| **Type** | QWAV Spinoff — Interactive Artifact (D13) |
| **QWAV Strategy Reference** | `strategy/3.0.md` — Build Gravity, Tier 1 Artifact A4 |
| **Created** | 2026-05-22 |
| **Repository** | `QNFO/tree-distance` |
| **Live Target** | `https://qnfo.github.io/tree-distance/` |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## 2. RAISON D'ÊTRE — QWAV STRATEGY NEXUS

**This project exists because the claim that "distance" means fundamentally different things in different geometries requires an interactive comparison to be understood.**

Most people know only Euclidean distance. The concept that cophenetic distance (tree-based) and ultrametric distance behave differently — and that the strong triangle inequality makes ultrametric distance qualitatively distinct — is abstract without interaction. This sandbox lets users click two points on a tree and see three different distance values instantly.

The Tree Distance publication (DOI: `10.5281/zenodo.20213043`) provides the formal treatment. This artifact makes it intuitive.

**Strategic contribution:**
- Provides the educational on-ramp — before someone can understand error confinement or convergence, they need to understand ultrametric distance
- The triadic rigidity demonstration (3 points, 2 distances must be equal) is a memorable "aha" moment
- Lower technical barrier than A1-A3 — accessible to anyone

**Without this project, visitors to A1-A3 may lack the geometric intuition to understand what they're seeing.**

## 3. SCOPE

### In Scope
- Interactive tree with clickable leaf nodes
- Three distance displays: cophenetic (tree depth of LCA), ultrametric (normalized cophenetic), Euclidean (spatial)
- Triadic rigidity visualization — select 3 points, show which 2 distances are equal
- Visual highlighting of the LCA path for each pair
- Responsive design

### Out of Scope
- Non-tree distance metrics (Manhattan, cosine, etc.)
- Large-scale tree exploration (> depth 5)
- Mathematical proofs (link to paper)

## 4. CURRENT STATUS (2026-05-23)

**Phase:** PROTOTYPE — Functional but minimal

**What exists:** A single `index.html` (9 KB, 146 lines JS) with tree rendering, leaf selection, and distance displays. Three distance values computed. Click interaction works.

**What's missing:**
- **Triadic rigidity demonstration.** The core "aha" moment is not built.
- **No explanation of what distances mean.** Values displayed but no context.
- **No test suite.**
- **No cross-links to A1-A3.**

---

*Updated: 2026-05-23 | QWAV Strategy: Build Gravity v3.0 | Artifact: Tier 1 — A4*
