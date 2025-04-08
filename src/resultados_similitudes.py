from tabulate import tabulate
from .ordenamiento import merge_sort
from pathlib import Path

def mostrar_top_similares(similitudes, top_n=10):
    merge_sort(similitudes)
    print("Top", top_n, "documentos más similares:")
    for i in range(min(top_n, len(similitudes))):
        print(f"{similitudes[i][0]} - {similitudes[i][1]}: {similitudes[i][2]*100:.5f}%")

def mostrar_tabla(similitudes):
    ruta_base = Path(__file__).resolve().parent.parent
    ruta_resultados = ruta_base / "resultados"
    ruta_resultados.mkdir(parents=True, exist_ok=True)

    ruta_archivo = ruta_resultados / "resultados_similitud.txt"
    
    headers = ["Documento 1", "Documento 2", "Similitud"]
    tabla = [(d1, d2, f"{sim*100:.2f}%") for d1, d2, sim in similitudes[:10]]
    tabla_formateada = tabulate(tabla, headers=headers, tablefmt="fancy_grid")
    
    print("\n📊 Top 10 documentos más similares:\n")
    print(tabla_formateada)
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("RESULTADOS DE SIMILITUD ENTRE DOCUMENTOS\n")
        f.write("="*50 + "\n\n")
        f.write(tabla_formateada)
    
    print(f"\n✅ Tabla guardada en: {ruta_archivo}\n")