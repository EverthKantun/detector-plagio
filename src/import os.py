import os
import re
import random
from collections import defaultdict
from itertools import combinations

def generar_txts(carpeta, cantidad=100):
    os.makedirs(carpeta, exist_ok=True)
    parrafos_base = [
        "El estudiante debe presentar su tarea a tiempo para evitar penalizaciones.",
        "La universidad ofrece múltiples programas de investigación para sus alumnos.",
        "El plagio es una falta grave que puede tener consecuencias académicas.",
        "Los docentes fomentan el pensamiento crítico a través de debates y ensayos.",
        "La ciencia avanza gracias a la colaboración entre investigadores de todo el mundo.",
        "La tarea asignada requiere un análisis detallado de los datos proporcionados.",
        "Los estudiantes deben citar correctamente sus fuentes para evitar problemas de autoría."
    ]
    for i in range(cantidad):
        contenido = "\n\n".join(random.choices(parrafos_base, k=5))
        with open(os.path.join(carpeta, f"documento_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(contenido)

def cargar_documentos(ruta):
    documentos = {}
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            with open(os.path.join(ruta, archivo), "r", encoding="utf-8") as f:
                documentos[archivo] = f.read()
    return documentos

def preprocesar_texto(texto, n=3):
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto.lower())
    palabras = texto.split()
    return [tuple(palabras[i:i+n]) for i in range(len(palabras)-n+1)]

def construir_tabla_hash(documentos, n=3):
    tablas = {}
    for nombre, texto in documentos.items():
        ngramas = preprocesar_texto(texto, n)
        tabla_hash = set(hash(ng) for ng in ngramas)
        tablas[nombre] = tabla_hash
    return tablas

def similitud_jaccard(set1, set2):
    interseccion = len(set1 & set2)
    union = len(set1 | set2)
    return interseccion / union if union != 0 else 0

def comparar_documentos(tablas):
    similitudes = []
    for doc1, doc2 in combinations(tablas.keys(), 2):
        sim = similitud_jaccard(tablas[doc1], tablas[doc2])
        similitudes.append((doc1, doc2, sim))
    return similitudes

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]
        
        merge_sort(izquierda)
        merge_sort(derecha)
        
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i][2] > derecha[j][2]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

def mostrar_top_similares(similitudes, top_n=10):
    merge_sort(similitudes)
    print("Top", top_n, "documentos más similares:")
    for i in range(min(top_n, len(similitudes))):
        print(f"{similitudes[i][0]} - {similitudes[i][1]}: {similitudes[i][2]:.2f}")

# Ruta específica en el escritorio
ruta_escritorio = r"C:\\Users\\esteb\\OneDrive\\Desktop\\txt_docs"

# Generar archivos de prueba
generar_txts(ruta_escritorio, 100)

# Procesar documentos
documentos = cargar_documentos(ruta_escritorio)
tablas_hash = construir_tabla_hash(documentos)
similitudes = comparar_documentos(tablas_hash)
mostrar_top_similares(similitudes, 10)
