from itertools import combinations

def build_hasse_diagram(simplicial_complex):
    """
    Erzeugt das Hasse-Diagramm für einen beliebigen Simplizialkomplex.
    Input: Liste von Tupeln/Sets (z.B. [(0,), (0,1), ...])
    Output: Liste von gerichteten Kanten (Facet -> Simplex)
    """
    # Simlexe in frozensets umwandeln (für Hashability) und nach Dimension sortieren
    nodes = sorted([frozenset(s) for s in simplicial_complex], key=len)
    hasse_edges = []

    # Vergleiche jedes Paar von Simlexe
    for i, sigma in enumerate(nodes):
        for tau in nodes[i+1:]:
            # Covering Relation: sigma ist Facette von tau, wenn:
            # 1. sigma Teilmenge von tau ist
            # 2. Die Dimension von tau genau um 1 größer ist (|tau| = |sigma| + 1)
            if len(tau) == len(sigma) + 1 and sigma.issubset(tau):
                hasse_edges.append((tuple(sorted(sigma)), tuple(sorted(tau))))
    
    return hasse_edges

def identify_beat_points(hasse_edges, nodes):
    """ Identifiziert Up- und Down-Beat-Points nach Barmak. """
    out_degree = {tuple(sorted(n)): 0 for n in nodes}
    in_degree = {tuple(sorted(n)): 0 for n in nodes}
    
    for u, v in hasse_edges:
        out_degree[u] += 1
        in_degree[v] += 1
        
    up_beats = [n for n, deg in out_degree.items() if deg == 1]
    down_beats = [n for n, deg in in_degree.items() if deg == 1]
    return up_beats, down_beats

# --- BEISPIEL: 3-Simplex (Tetraeder) ---
vertices = {0, 1, 2, 3}
# Erzeuge alle nicht-leeren Teilmengen (den vollen Simplizialkomplex des Tetraeders)
tetrahedron_complex = []
for r in range(1, len(vertices) + 1):
    tetrahedron_complex.extend(list(combinations(vertices, r)))

# Hasse-Diagramm berechnen
edges = build_hasse_diagram(tetrahedron_complex)
up, down = identify_beat_points(edges, tetrahedron_complex)

print(f"Anzahl Hasse-Kanten: {len(edges)}") # 4 Ecken -> 6 Kanten -> 4 Flächen -> 1 Volumen
print(f"Up-Beat-Points (z.B. Facetten): {up}")
