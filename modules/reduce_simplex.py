def reduce_to_core(nodes, edges):
    """
    Rekursiver Pseudocode:
    Input: Hasse-Diagramm H einer Zusammenhangskomponente.
    Finde alle aktuellen Beat-Points (In-Degree=1 oder Out-Degree=1).
    Falls keine Beat-Points existieren: Return H (dies ist der Core).
    Wähle einen Beat-Point x, entferne ihn und alle inzidenten Kanten.
    Rekursion: Rufe den Algorithmus mit dem verkleinerten Diagramm H∖{x} auf
"""
    # Hilfsfunktion für Grade
    in_deg = {n: 0 for n in nodes}
    out_deg = {n: 0 for n in nodes}
    for u, v in edges:
        out_deg[u] += 1
        in_deg[v] += 1
    
    # Beat-Point finden (Barmak-Definition)
    beat_point = None
    for n in nodes:
        if in_deg[n] == 1 or out_deg[n] == 1:
            beat_point = n
            break
            
    if beat_point is None:
        return nodes, edges # Minimaler Raum erreicht
    
    # Punkt entfernen und rekursiv weitermachen
    new_nodes = [n for n in nodes if n != beat_point]
    new_edges = [(u, v) for u, v in edges if u != beat_point and v != beat_point]
    
    return reduce_to_core(new_nodes, new_edges)

