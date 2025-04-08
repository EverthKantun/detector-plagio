from pybloom_live import BloomFilter
from .preprocesamiento import preprocesar_texto

def construir_tabla_bloom(documentos, usar_bloom=False, n=3):
    tablas = {}
    ngramas_originales = {}
    for nombre, texto in documentos.items():
        ngramas = preprocesar_texto(texto, n)
        ngramas_originales[nombre] = ngramas
        if usar_bloom:
            bloom = BloomFilter(capacity=1000, error_rate=0.001)
            for ng in ngramas:
                bloom.add(ng)
            tablas[nombre] = bloom
        else:
            tablas[nombre] = set(hash(ng) for ng in ngramas)
    return tablas, ngramas_originales