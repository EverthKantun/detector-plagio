# 📂 Carpeta del Código Fuente (`src`)

Contiene todos los módulos y scripts que componen la lógica del sistema de detección de similitud de textos.

## Módulos principales
- `preprocesamiento.py`: Limpieza del texto, eliminación de puntuación, conversión a minúsculas y generación de n-gramas.
- `hashing.py`: Generación y almacenamiento de valores hash en tablas hash personalizadas.
- `bloom_filter.py`: Implementación de filtros de Bloom para comprobaciones eficientes de pertenencia.
- `comparacion.py`: Comparación de documentos usando Similitud de Jaccard y con filtros Bloom.
- `visualizacion_grafo.py`: Visualización de la similitud entre documentos mediante un grafo usando NetworkX y matplotlib.
- `ordenamiento.py`: Implementación del algoritmo Merge Sort para ordenar los pares de documentos por su nivel de similitud.
- `resultados_similitudes.py`: Generación de una tabla con el top 10 de los pares de documentos más similares y exportación a CSV.
- `carga_documentos.py`: Carga automática de todos los archivos `.txt` desde la carpeta `documentos`.
- `generador_documentos.py`: Crea documentos `.txt` con texto aleatorio para alimentar el sistema con datos de prueba.

> ⚙️ Este directorio es esencial para el funcionamiento interno del sistema.

También se incluye el archivo `comparación_sin_optimización.ipynb` donde no se incluye bloom filters.
