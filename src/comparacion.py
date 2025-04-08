
from itertools import combinations

# 6. Comparar documentos usando similitud de Jaccard (solo para sets)
def similitud_jaccard(set1, set2):
    interseccion = len(set1 & set2)
    union = len(set1 | set2)
    return interseccion / union if union != 0 else 0

def comparar_documentos(tablas, usar_bloom=False, ngramas_originales=None):
    similitudes = []
    for doc1, doc2 in combinations(tablas.keys(), 2):
        if usar_bloom:
            # Usamos los ngramas de doc1 para comprobar si están en el filtro de doc2
            interseccion = sum(1 for ng in ngramas_originales[doc1] if ng in tablas[doc2])
            union = len(set(ngramas_originales[doc1])) + len(set(ngramas_originales[doc2])) - interseccion
            sim = interseccion / union if union != 0 else 0
        else:
            sim = similitud_jaccard(tablas[doc1], tablas[doc2])
        similitudes.append((doc1, doc2, sim))
    return similitudes
