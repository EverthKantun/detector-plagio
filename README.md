# Sistema de Detección de Similitud de Textos

Este proyecto consiste en el desarrollo de un **Sistema de Detección de Similitud de Textos**, diseñado para comparar documentos `.txt` con el objetivo de identificar posibles coincidencias o similitudes. Su principal aplicación se orienta a contextos académicos, como la **detección de plagio**. El sistema está implementado en Python, utilizando estructuras de datos eficientes y algoritmos de comparación optimizados.

## Descripción General

El sistema realiza las siguientes operaciones principales:

- **Carga automática de archivos `.txt`** desde una carpeta específica.
- **Preprocesamiento de texto**, que incluye limpieza (eliminación de puntuación, conversión a minúsculas) y generación de **n-gramas** (secuencias de `n` palabras).
- **Transformación de n-gramas** en valores hash y almacenamiento en una **tabla hash personalizada**.
- Opcionalmente, almacenamiento en un **filtro de Bloom** para reducir tiempos de búsqueda.
- **Comparación de documentos** mediante la **Similitud de Jaccard**, evaluando el grado de coincidencia entre conjuntos de n-gramas.
- **Ordenamiento de resultados** usando el algoritmo **Merge Sort**, por su eficiencia y estabilidad.
- **Visualización** de los resultados en:
  - Tabla de pares de documentos con mayor similitud.
  - Grafo interactivo que muestra relaciones entre documentos mediante nodos y enlaces ponderados.

## ⚙️ Instrucciones de Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/detector-plagio.git
cd detector-plagio
```

### 2. Instalar las dependencias

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el programa

```bash
python main.py
```

## 🖥️ Interfaz del Menú

Desde la consola, el sistema ofrece un menú interactivo que permite:

1. **Cargar documentos y mostrar similitudes:** se procesan los documentos y se muestra una tabla con los pares más similares.
2. **Ver tabla de similitudes:** despliega todos los pares comparados junto con su porcentaje de similitud.
3. **Ver grafo de similitud:** representa gráficamente los documentos como nodos conectados según el nivel de similitud.
4. **Comparar dos documentos manualmente:** permite al usuario seleccionar dos archivos específicos y calcular su similitud con el índice de Jaccard.
5. **Salir del sistema**


## 📦 Requerimientos

Listado en `requirements.txt`:

```
pybloom-live
networkx
matplotlib
PyQt5
tabulate
```

Estas se instalan todas con:

```bash
pip install -r requirements.txt
```
