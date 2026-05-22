# PROJECT CHARTER — Tree Distance Sandbox

## Project Identity

| Field | Value |
|:------|:------|
| **Project Name** | tree-distance-sandbox |
| **Title** | Tree Distance Sandbox |
| **Type** | QWAV Spinoff — Interactive Artifact (D13) |
| **Created** | 2026-05-22 |
| **Deployed** | 2026-05-23 |
| **Live URL** | https://qnfo.github.io/tree-distance/ |
| **Repository** | QNFO/tree-distance |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## Purpose & Thesis

Interactive cophenetic, ultrametric, and Euclidean distance comparison. Users click tree leaves to discover triadic rigidity — the signature of ultrametric geometry.

## Technical Approach

Single HTML file, vanilla JavaScript, Canvas API. No dependencies.

## User Interaction

Click-based leaf selection. Three distance types computed and displayed per triangle.

## Evidence Contribution

All triples satisfy the strong triangle inequality. 649/649 triples ultrametric (The Tree Is Real validation).

## Success Criteria

1. Interactive elements respond to user input (verified by automated canvas check)
2. Deployed and loading at https://qnfo.github.io/tree-distance/
3. JavaScript executes without console errors
4. Cross-linked from QWAV Technical Site Hub
5. Demonstrates a specific, published QWAV result

## Constraints

- Zero external dependencies (no CDN, no npm)
- Single HTML file (inline CSS/JS)
- GitHub Pages deployment (no server)
- MIT licensed or equivalent open-source

## Relationship to QWAV Program

This project is one of 5 interactive artifacts (D13) that make QWAV's computational evidence tangible. Each demo demonstrates one key result:
- Error Confinement → strong triangle inequality visualization
- Q-PNA Playground → glass-box AI decision trees
- Convergence Explorer → ultrametric vs Euclidean comparison
- Tree Distance Sandbox → cophenetic distance computation
- Hardware Visualizer → neutral atom hardware mapping

Together, these 5 demos + the Technical Site Hub + the Virtual Qubit Showdown form the complete QWAV Gravity Portfolio.

---

*Project charter established 2026-05-22. Project completed 2026-05-23.*
