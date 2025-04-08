import os
import re
from collections import defaultdict
from itertools import combinations
import hashlib
from pybloom_live import BloomFilter
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

# Paso 1: Cargar Documentos
def cargar_documentos(carpeta=r"C:\Users\esteb\OneDrive\Desktop\txt_docs"):
    documentos = {}
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                documentos[archivo] = f.read()
    return documentos

# Paso 2: Preprocesamiento
def limpiar_y_tokenizar(texto, n=3):
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto.split()
    ngramas = [' '.join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]
    return ngramas

def hash_personalizado(ngrama):
    return int(hashlib.sha256(ngrama.encode('utf-8')).hexdigest(), 16)

# Paso 3: Crear Tabla Hash
def crear_tabla_hash(ngramas, usar_bloom=True):
    tabla = set()
    bloom = BloomFilter(capacity=10000, error_rate=0.001) if usar_bloom else None
    for n in ngramas:
        h = hash_personalizado(n)
        if usar_bloom:
            bloom.add(h)
        tabla.add(h)
    return tabla

# Paso 4: Similitud Jaccard
def similitud_jaccard(set1, set2):
    interseccion = len(set1 & set2)
    union = len(set1 | set2)
    return interseccion / union if union else 0

# Paso 5: Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    return merge(merge_sort(lista[:medio]), merge_sort(lista[medio:]))

def merge(izq, der):
    resultado = []
    while izq and der:
        resultado.append(izq.pop(0) if izq[0][2] > der[0][2] else der.pop(0))
    return resultado + izq + der

# Paso 6: Comparar Documentos
def encontrar_similitudes(documentos, n=5):
    hash_docs = {doc: crear_tabla_hash(limpiar_y_tokenizar(texto)) for doc, texto in documentos.items()}
    resultados = []
    for doc1, doc2 in combinations(hash_docs, 2):
        sim = similitud_jaccard(hash_docs[doc1], hash_docs[doc2])
        resultados.append((doc1, doc2, sim))
    return merge_sort(resultados)[:n]

# Visualizar Resultados en Tabla
def mostrar_tabla(similitudes):
    headers = ["Documento 1", "Documento 2", "Similitud"]
    tabla = [(d1, d2, f"{sim*100:.2f}%") for d1, d2, sim in similitudes]
    print("\n📊 Top documentos más similares:\n")
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))

# Visualización del Grafo
def visualizar_grafo(similitudes):
    G = nx.Graph()
    for d1, d2, sim in similitudes:
        G.add_edge(d1, d2, weight=round(sim, 2))
    pos = nx.spring_layout(G, k=0.5, seed=42)
    weights = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
            node_size=2500, font_size=10, font_weight='bold', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=9)
    plt.title("🔗 Grafo de Similitud entre Documentos", fontsize=14)
    plt.axis('off')
    plt.show()

# Menú Interactivo
def menu():
    while True:
        print("\n---  Sistema de Detección de Similitud de Textos ---")
        print("1. Cargar documentos y mostrar similitudes")
        print("2. Ver grafo de similitud")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            documentos = cargar_documentos()
            similitudes = encontrar_similitudes(documentos)
            mostrar_tabla(similitudes)
        elif opcion == "2":
            if 'similitudes' not in locals():
                documentos = cargar_documentos()
                similitudes = encontrar_similitudes(documentos)
            visualizar_grafo(similitudes)
        elif opcion == "3":
            print("¡Hasta luego, Esteban! 👋")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
