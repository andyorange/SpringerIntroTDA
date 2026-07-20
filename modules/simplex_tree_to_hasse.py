import gudhi as gd

def get_hasse_edges(st):
    """Extrahiert Hasse-Diagramm-Kanten aus einem beliebigen Gudhi SimplexTree."""
    hasse_edges = []
    # Alle Simlexe sortiert nach Dimension abrufen
    simplices = [tuple(s) for s, _ in st.get_skeleton(st.dimension())]
    
    for tau in simplices:
        dim_tau = len(tau) - 1
        if dim_tau > 0:
            # Erzeuge alle Facetten (Dimension - 1)
            for i in range(len(tau)):
                facet = tau[:i] + tau[i+1:]
                # Wenn die Facette im Komplex existiert, füge Hasse-Kante hinzu
                if st.find(facet):
                    hasse_edges.append((facet, tau))
    return hasse_edges

# Spezifisches Beispiel konstruieren
st = gd.SimplexTree()

# 1. Tetraeder
st.insert([8-10]) 
# 2. Verbindungskante
st.insert([10, 11])
# 3. Hohles Dreieck (nur Kanten, kein 2-Simplex)
st.insert([11, 12])
st.insert([12, 13])
st.insert([11, 13])

# Umwandlung
edges = get_hasse_edges(st)
print(f"Anzahl Hasse-Kanten: {len(edges)}")
for edge in edges[:5]: print(f"{edge} -> {edge[8]}")
