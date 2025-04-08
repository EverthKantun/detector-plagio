from src.carga_documentos import cargar_documentos
from src.generador_documentos import generar_txts
from src.bloom_filter import construir_tabla_bloom
from src.comparacion import comparar_documentos, similitud_jaccard
from src.resultados_similitudes import mostrar_tabla, mostrar_top_similares
from src.visualizacion_grafo import visualizar_similitudes
from src.preprocesamiento import preprocesar_texto
from pathlib import Path

def encontrar_similitudes(documentos, usar_bloom=True, n=2):
    tablas, ngramas_originales = construir_tabla_bloom(documentos, usar_bloom=usar_bloom, n=n)
    similitudes = comparar_documentos(tablas, usar_bloom=usar_bloom, ngramas_originales=ngramas_originales)
    return similitudes

def menu():
    similitudes = None
    documentos = None
    while True:
        print("\n---  Sistema de Detección de Similitud de Textos ---")
        print("1. Cargar documentos y mostrar similitudes")
        print("2. Ver tabla de similitudes")
        print("3. Ver grafo de similitud")
        print("4. Comparar dos documentos manualmente (Jaccard)")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ruta = Path.cwd() / "documentos"
            generar_txts(ruta, 100)
            documentos = cargar_documentos(ruta)
            tablas_bloom, ngramas_originales = construir_tabla_bloom(documentos, usar_bloom=True)
            similitudes = comparar_documentos(tablas_bloom, usar_bloom=True, ngramas_originales=ngramas_originales)
            mostrar_top_similares(similitudes, 10)

        elif opcion == "2":
            if not similitudes:
                print("Primero debes cargar los documentos (opción 1).")
            else:
                mostrar_tabla(similitudes)

        elif opcion == "3":
            if not similitudes:
                print("Primero debes cargar los documentos (opción 1).")
            else:
                visualizar_similitudes(similitudes[:10])

        elif opcion == "4":
            # Carpeta donde están los documentos
            ruta = Path.cwd() / "tests"  # Aseguramos que la carpeta "tests" esté al mismo nivel de "Main.py"

            # Mostrar los documentos disponibles
            print("\nSelecciona los documentos para comparar:")
            print("1. ensayo_Priego.txt")
            print("2. ensayo_Kantún.txt")
            print("3. ensayo_ácido_fólico.txt")
            print("2. ensayo_Priego_parcial.txt")
            
            # Entrada del usuario para seleccionar los archivos
            opcion_1 = input("Elige el primer documento (1, 2, 3 o 4): ")
            opcion_2 = input("Elige el segundo documento (1, 2, 3 o 4): ")

        # Mapear las opciones de entrada con los nombres de los archivos
            if opcion_1 == "1":
                archivo1 = "introduccion_ensayo_priego.txt"
            elif opcion_1 == "2":
                archivo1 = "introduccion_ensayo_kantun.txt"
            elif opcion_1 == "3":
                archivo1 = "ensayo_acido_folico.txt"
            elif opcion_1 == "4":
                archivo1 = "introduccion_ensayo_priego_parcial.txt"
            else:
                print("❌ Opción inválida para el primer documento.")
                archivo1 = None

            if opcion_2 == "1":
                archivo2 = "introduccion_ensayo_priego.txt"
            elif opcion_2 == "2":
                archivo2 = "introduccion_ensayo_kantun.txt"
            elif opcion_2 == "3":
                archivo2 = "ensayo_acido_folico.txt"
            elif opcion_2 == "4":
                archivo2 = "introduccion_ensayo_priego_parcial.txt"
            else:
                print("❌ Opción inválida para el segundo documento.")
                archivo2 = None


            # Verificar que ambas opciones sean válidas
            if archivo1 and archivo2:
                archivo1_path = ruta / archivo1
                archivo2_path = ruta / archivo2

                try:
                    # Leer el contenido de los documentos
                    with open(archivo1_path, "r", encoding="utf-8") as f1:
                        texto1 = f1.read()
                    with open(archivo2_path, "r", encoding="utf-8") as f2:
                        texto2 = f2.read()

                    # Preprocesar los textos (crear n-gramas)
                    ngramas1 = preprocesar_texto(texto1, n=2)
                    ngramas2 = preprocesar_texto(texto2, n=2)

                    # Convertir los n-gramas en sets
                    set1 = set(ngramas1)
                    set2 = set(ngramas2)

                    # Calcular la similitud de Jaccard
                    sim = similitud_jaccard(set1, set2)
                    print(f"\n✅ Similitud Jaccard entre {archivo1} y {archivo2}: {sim:.5f}")

                except FileNotFoundError:
                    print("❌ No se encontraron los archivos. Asegúrate de que los documentos existan en la carpeta 'tests'.")


        elif opcion == "5":
            print("¡Hasta luego! 👋")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
