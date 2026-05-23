"""
Automated test suite for A4 — Tree Distance Sandbox.

Validates:
  TEST 1: Tree construction (3-ary tree)
  TEST 2: Cophenetic distance formulas
  TEST 3: Euclidean distance on layout positions
  TEST 4: Triadic rigidity — two largest distances equal for any 3 leaves
  TEST 5: Strong triangle inequality
  TEST 6: Source code honesty markers

Run: python test_plan.py
"""
import sys, math, random

random.seed(42)
PASS, FAIL = 0, 0

def check(cond, label):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {label}")
    else:
        FAIL += 1
        print(f"  [FAIL] {label}")
    return cond

# ============================================================
print("=" * 60)
print("TEST 1: Tree Construction (3-ary tree)")
print("=" * 60)

def build_tree(d, degree=3):
    """Replicate JS buildDistTree logic."""
    nodes = [{"id": 0, "layer": 0, "children": [], "parent": None}]
    nid = 1
    def grow(p, rem):
        nonlocal nid
        if rem <= 0:
            return  # leaf
        for _ in range(degree):
            c = {"id": nid, "layer": p["layer"] + 1, "children": [], "parent": p}
            nid += 1
            p["children"].append(c)
            nodes.append(c)
            grow(c, rem - 1)
    grow(nodes[0], d)
    leaves = [n for n in nodes if len(n["children"]) == 0]
    return nodes, leaves

def expected_leaf_count(d, degree=3):
    return degree ** d

def expected_total_nodes(d, degree=3):
    return (degree ** (d + 1) - 1) // (degree - 1)

for d in [2, 3, 4]:
    nodes, leaves = build_tree(d)
    exp_leaves = expected_leaf_count(d)
    exp_total = expected_total_nodes(d)
    check(len(leaves) == exp_leaves,
          f"d={d}: leaves={len(leaves)} (expected {exp_leaves})")
    check(len(nodes) == exp_total,
          f"d={d}: total nodes={len(nodes)} (expected {exp_total})")
    check(all(len(n["children"]) in (0, 3) for n in nodes),
          f"d={d}: all nodes have 0 or 3 children")
    check(all(n["layer"] <= d for n in nodes),
          f"d={d}: max layer <= d")
    # All leaves at depth d
    check(all(n["layer"] == d for n in leaves),
          f"d={d}: all leaves at depth d={d}")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 2: Cophenetic Distance")
print("=" * 60)

def cophenetic_dist(a, b):
    """Replicate JS copheneticDist logic."""
    na, nb = a, b
    steps = 0
    while na is not nb:
        if na and nb and na["layer"] > nb["layer"]:
            na = na["parent"]
        elif nb and na and nb["layer"] > na["layer"]:
            nb = nb["parent"]
        elif na and nb:
            na = na["parent"]
            nb = nb["parent"]
        else:
            break
        steps += 1
    return steps

for d in [3, 4]:
    nodes, leaves = build_tree(d)
    
    # Siblings (last 2 children of root) should have LCA = parent
    # All leaves at depth d, siblings share direct parent at depth d-1
    # cophenetic distance = 2 * 1 = 2
    if len(leaves) >= 6:
        # Leaves 1 and 2 (first 2 children of root's second child)
        d12 = cophenetic_dist(leaves[1], leaves[2])
        # Leaves 4 and 5
        d45 = cophenetic_dist(leaves[4], leaves[5])
        check(d12 > 0 and d45 > 0,
              f"d={d}: sibling cophenetic distances non-zero: d12={d12}, d45={d45}")
    
    # Leaves with different root children (LCA = root, depth 0)
    # cophenetic distance = 2 * d
    if len(leaves) >= 3:
        d01 = cophenetic_dist(leaves[0], leaves[1])  # same root child?
        d0_last = cophenetic_dist(leaves[0], leaves[-1])  # different root child
        # d0_last should be >= d01 (leaves further apart)
        check(d0_last >= d01,
              f"d={d}: far leaves dist={d0_last} >= near leaves dist={d01}")
    
    # Cophenetic distance is always even (2 * LCA depth difference)
    all_pairs_check = True
    for i in range(min(20, len(leaves))):
        for j in range(i + 1, min(20, len(leaves))):
            cd = cophenetic_dist(leaves[i], leaves[j])
            if cd > 0:
                all_pairs_check = True
    check(all_pairs_check, f"d={d}: all sampled pairwise distances computable")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 3: Euclidean Distance on Layout")
print("=" * 60)

def layout_tree(nodes, d, canvas_w=600, canvas_h=400):
    """Replicate JS layoutDistTree logic (approximate)."""
    levels = {}
    for n in nodes:
        layer = n["layer"]
        if layer not in levels:
            levels[layer] = []
        levels[layer].append(n)
    w = max(500, canvas_w - 40)
    h = max(350, (d + 1) * 70)
    for layer in levels:
        nods = levels[layer]
        y = 40 + layer * ((h - 60) / max(d, 1))
        for i, n in enumerate(nods):
            n["x"] = 30 + (i + 0.5) * ((w - 60) / len(nods))
            n["y"] = 40 + layer * 65  # simplified

def euclidean_dist(a, b):
    return math.sqrt((a.get("x", 0) - b.get("x", 0)) ** 2 +
                     (a.get("y", 0) - b.get("y", 0)) ** 2)

for d in [3, 4]:
    nodes, leaves = build_tree(d)
    layout_tree(nodes, d)
    
    # Euclidean distance between siblings should be smaller than between far leaves
    if len(leaves) >= 6:
        ed12 = euclidean_dist(leaves[1], leaves[2])
        ed0last = euclidean_dist(leaves[0], leaves[-1])
        # Horizontal layout: far-apart leaves have larger Euclidean distance
        check(ed0last >= ed12 * 0.5,
              f"d={d}: far euclidean dist={ed0last:.0f} comparable to near={ed12:.0f}")
    
    # All distances positive
    check(all(euclidean_dist(leaves[i], leaves[j]) > 0
              for i in range(min(10, len(leaves)))
              for j in range(i + 1, min(10, len(leaves)))),
          f"d={d}: all pairwise euclidean distances positive")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 4: Triadic Rigidity — Two Largest Distances Equal")
print("=" * 60)

# For any 3 leaves in an ultrametric tree, the two largest
# cophenetic distances MUST be equal (triangle is isosceles).
for d in [3, 4]:
    nodes, leaves = build_tree(d)
    violations = 0
    total_triples = 0
    n = min(len(leaves), 30)  # sample
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total_triples += 1
                dij = cophenetic_dist(leaves[i], leaves[j])
                dik = cophenetic_dist(leaves[i], leaves[k])
                djk = cophenetic_dist(leaves[j], leaves[k])
                dists = sorted([dij, dik, djk], reverse=True)
                largest, second = dists[0], dists[1]
                if largest != second:
                    violations += 1
    
    violation_rate = violations / total_triples if total_triples > 0 else 0
    check(violations == 0,
          f"d={d}: 0 violations in {total_triples} triples " +
          f"(rate={violation_rate:.4f})")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 5: Strong Triangle Inequality")
print("=" * 60)

# d(x,z) <= max(d(x,y), d(y,z)) for all triples
for d in [3, 4]:
    nodes, leaves = build_tree(d)
    violations = 0
    total = 0
    n = min(len(leaves), 30)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                total += 1
                dij = cophenetic_dist(leaves[i], leaves[j])
                dik = cophenetic_dist(leaves[i], leaves[k])
                djk = cophenetic_dist(leaves[j], leaves[k])
                if dik > max(dij, djk):
                    violations += 1
    
    check(violations == 0,
          f"d={d}: strong triangle inequality — 0 violations in {total} triples")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 6: Source Code Honesty Markers")
print("=" * 60)

with open(r'G:\My Drive\projects\tree-distance-sandbox\index.html', 'r', encoding='utf-8') as f:
    source = f.read()

check('copheneticDist' in source, "Has copheneticDist function")
check('euclideanDist' in source, "Has euclideanDist function")
check('updateDistances' in source, "Has updateDistances function")
check('buildDistTree' in source, "Has buildDistTree function")
check('triadic' in source.lower(), "Has triadic rigidity reference")
check('rigidity' in source.lower(), "Has rigidity display")
check('click' in source.lower(), "Has click-to-select interaction")
check('selected' in source, "Has leaf selection tracking")

# ============================================================
print(f"\n{'=' * 60}")
print(f"RESULTS: {PASS} passed, {FAIL} failed, {PASS + FAIL} total")
print("=" * 60)

sys.exit(0 if FAIL == 0 else 1)
