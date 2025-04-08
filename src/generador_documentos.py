import os
import random

def generar_txts(carpeta, cantidad=100):
    os.makedirs(carpeta, exist_ok=True)
    palabras_base = [
        "estudiante", "universidad", "tarea", "plagio", "docente", "investigación", "ciencia",
        "aprendizaje", "conocimiento", "disciplina", "método", "estudio", "ensayo", "análisis", "criterio",
        "creatividad", "descubrimiento", "innovación", "teoría",
    ]
    for i in range(cantidad):
        contenido = " ".join(random.choices(palabras_base, k=200))
        with open(os.path.join(carpeta, f"documento_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(contenido)