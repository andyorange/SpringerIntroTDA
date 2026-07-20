import gudhi as gd

def build_hasse_from_gudhi(st):
    """Extrahiert die Covering Relation für das Hasse-Diagramm aus einem SimplexTree."""
    # Alle Simplexe extrahieren
    simplices = [tuple(s) for s, _ in st.get_skeleton(st.dimension())]
    hasse_edges = []
    
    # Covering Relation: sigma < tau und dim(tau) = dim(sigma) + 1
    for sigma in simplices:
        for tau in simplices:
            if len(tau) == len(sigma) + 1 and set(sigma).issubset(set(tau)):
                hasse_edges.append((sigma, tau))
    return simplices, hasse_edges

# 1. Gudhi SimplexTree initialisieren
st = gd.SimplexTree()

#TODO: unser beispiel tetraeder pus Kante plus hohles Dreieck
# 2. Tetraeder einfügen (fügt automatisch alle Unter-Simplexe ein) [8]
st.insert([0-3])

# 3. Zusätzliche Kante einfügen
st.insert([4, 5])

#. hohles Dreieck einfügen
st.insert([6, 7, 8], filtration=1.0) # Filration notwendig??

# 4. Hasse-Struktur berechnen
nodes, edges = build_hasse_from_gudhi(st)

# 5. Beat-Point Analyse (Logik aus Barmak Theorie) [9]
out_degree = {n: 0 for n in nodes}
in_degree = {n: 0 for n in nodes}
for u, v in edges:
    out_degree[u] += 1
    in_degree[v] += 1

up_beats = [n for n, deg in out_degree.items() if deg == 1]
down_beats = [n for n, deg in in_degree.items() if deg == 1]
