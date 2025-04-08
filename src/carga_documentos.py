import os

def cargar_documentos(ruta, n=2):
    documentos = {}
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            with open(os.path.join(ruta, archivo), "r", encoding="utf-8") as f:
                contenido = f.read()
                documentos[archivo] = contenido
    return documentos