import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
matplotlib.use('Qt5Agg')  # Usar Qt5 como backend
import matplotlib.pyplot as plt

def visualizar_similitudes(similitudes, nombre_archivo="grafo_similitudes.png"):
    ruta_base = Path(__file__).resolve().parent.parent
    ruta_resultados = ruta_base / "resultados"
    ruta_resultados.mkdir(parents=True, exist_ok=True)
    ruta_completa = ruta_resultados / nombre_archivo
    
    G = nx.Graph()
    for doc1, doc2, sim in similitudes:
        if sim > 0:
            G.add_edge(doc1, doc2, weight=round(sim, 2))

    pos = nx.spring_layout(G, k=0.15, iterations=2)
    etiquetas = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=9, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    plt.title("Grafo de Similitud entre Documentos")
    plt.savefig(ruta_completa, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Gráfico guardado en: {ruta_completa}")