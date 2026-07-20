import gudhi as gd
"""
Der manuelle BFS/DFS-Ansatz auf dem Hasse-Diagramm dient vor allem der Identifikation von Zusammenhangskomponenten. 
Gudhi hingegen nutzt für die Reduktionspezialisierte Datenstrukturen (SimplexTree), die deutlich performanter sind
als eine allgemeine Graph-Traversierung
"""
# 1. SimplexTree erstellen
st = gd.SimplexTree()

# Tetraeder {0,1,2,3} einfügen
st.insert([0-3]) 

# Zusätzliche Kante {3,4} einfügen (erzeugt automatisch Knoten {4})
st.insert([4, 5])

print(f"Simplexe vor dem Peeling: {st.num_simplices()}")

# 2. Der Peeling-Prozess (Edge Collapse)
# Dieser Schritt reduziert den Komplex homotopieäquivalent
# Entspricht dem Entfernen von Beat-Points im Hasse-Diagramm
st.collapse_edges()

print(f"Simplexe nach dem Peeling: {st.num_simplices()}")

# 3. Optional: Expansion auf höhere Dimensionen
# Falls man nach dem Kollaps wieder die volle Skelett-Struktur braucht
st.expansion(3)

# Nach st.collapse_edges() und st.expansion(3)

"""
Mathematischer Hintergrund
Betti-Zahlen: Der Rang der n-ten Homologiegruppe Hn wird als n-te Betti-Zahl βn bezeichnet.
Komponenten: β0 gibt die Anzahl der Wegzusammenhangskomponenten an. 
Für einen zusammenhängenden Raum wie den Tetraeder gilt β0=1.
Löcher: βn für n>0 misst höherdimensionale „Löcher“. Da der volle Tetraeder und die zusätzliche Kante keine Hohlräume umschließen, müssen diese nach der Reduktion 0 sein.
Invarianz: Da der Peeling-Prozess eine schwache Homotopieäquivalenz (über Beat-Points bzw. starke Kollapse) darstellt, bleiben diese Zahlen während der Vereinfachung konstant.
Gudhi nutzt für diese Berechnung intern die Reduktion der Randmatrix
"""

# 1. Persistenz berechnen (Voraussetzung für Betti-Zahlen)
st.persistence()

# 2. Betti-Zahlen extrahieren
betti = st.betti_numbers()

print(f"Betti-Zahlen (b0, b1, b2, ...): {betti}")

# Prüfung auf Zusammenziehbarkeit:
# Ein Raum ist (schwach) auf einen Punkt zusammenziehbar, 
# wenn b0=1 und alle anderen bi=0 sind.
if betti == [1] or (len(betti) > 0 and betti == 1 and all(b == 0 for b in betti[1:])):
    print("Der Raum wurde erfolgreich auf einen Punkt (Core) reduziert.")
