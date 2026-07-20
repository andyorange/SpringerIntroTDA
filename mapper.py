import os
import pandas as pd
import numpy as np
import kmapper as km
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.datasets import load_diabetes

# Absoluten Pfad für die HTML-Datei im aktuellen Skript-Ordner definieren
current_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_dir, "kmapper_diabetes_clustering.html")

# Datensatz laden (Hinweis: scaled=False, damit wir StandardScaler sauber nutzen)
dfX, y = load_diabetes(as_frame=True, return_X_y=True, scaled=False)

# Daten skalieren (Wichtig für Distanzmetriken)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(dfX)

# KeplerMapper initialisieren
mapper = km.KeplerMapper(verbose=1)

# Sinnvolle Projektion wählen (z.B. PCA auf 2 Komponenten)
# "projection=[0, 1]" extrahiert Spalten, aber wir übergeben eine echte Projektion:
projected_data = mapper.fit_transform(X_scaled, projection="pca(2)")

# Graph erstellen mit korrigierten Clustereinstellungen,
# eps=1.5 gewährt DBSCAN in standardisierten Räumen genügend Spielraum
graph = mapper.map(
    projected_data, 
    X_scaled,
    clusterer=DBSCAN(eps=1.5, min_samples=3),  
    cover=km.Cover(n_cubes=10, perc_overlap=0.2), # n_cubes leicht reduziert für stabilere Überlappungen
)

# 6. Visualisierungsdaten: Kmapper kann nicht korrekt Daten schreiben in einer virtuellen Umgebung.
# Daher der kleine Umweg per content Variable.
html_doc = mapper.visualize(
    graph,
    title='Diabetes Clustering (PCA Projection)',
    X=dfX.values,              # Unskalierte Rohdaten für lesbare Tooltips
    X_names=list(dfX.columns)  # Spaltennamen
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"Visualisierung erfolgreich unter '{output_path}' gespeichert!")
