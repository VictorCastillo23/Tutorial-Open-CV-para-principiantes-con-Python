# Tutorial OpenCV para principiantes con Python

Repositorio educativo para aprender **visión por computadora** utilizando **Python** y la librería **OpenCV**, enfocado en personas que están comenzando desde cero.

---

## Descripción

Este proyecto contiene ejemplos prácticos y sencillos para introducirte en el uso de OpenCV con Python, una de las bibliotecas más utilizadas en **procesamiento de imágenes y visión artificial**. 

A lo largo del repositorio aprenderás conceptos básicos como:

* Lectura y visualización de imágenes
* Manipulación de píxeles
* Uso de filtros
* Procesamiento de video
* Aplicaciones básicas de visión por computadora

---

## ¿Qué es OpenCV?

**OpenCV (Open Source Computer Vision Library)** es una biblioteca de código abierto con cientos de algoritmos optimizados para trabajar con imágenes y video en tiempo real.

Se usa en áreas como:

* Reconocimiento facial
* Detección de objetos
* Robótica
* Inteligencia artificial

---

## Tecnologías utilizadas

*  Python 3
*  OpenCV (`cv2`)
*  NumPy

---

## Instalación

> ⚠️ **Usá Python 3.10 a 3.13.** `deepface` depende de `tensorflow`, que todavía no publica wheels para Python 3.14 (ni versiones más nuevas) — si tu `python` por defecto apunta a 3.14, `pip install -r requirements.txt` va a fallar con un error de resolución de dependencias imposible de resolver. En Windows, usá el [Python Launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows) para elegir la versión: `py -0p` lista las versiones instaladas, y `py -3.13 -m venv ENTORNO` crea el entorno con esa versión puntual.

1. Clona el repositorio:

```bash
git clone https://github.com/VictorCastillo23/Tutorial-Open-CV-para-principiantes-con-Python.git
cd Tutorial-Open-CV-para-principiantes-con-Python
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv ENTORNO        # Linux / Mac / Windows con Python 3.10-3.13 por defecto
py -3.13 -m venv ENTORNO      # Windows, si necesitás elegir la versión explícitamente
source ENTORNO/bin/activate   # Linux / Mac
.\ENTORNO\Scripts\Activate.ps1  # Windows (PowerShell)
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## Requisito extra para el módulo de OCR (Tesseract-OCR)

El módulo 11 (OCR con `pytesseract`) necesita, además de `pip install -r requirements.txt`, tener instalado el **binario de Tesseract-OCR a nivel de sistema** (pytesseract es solo un wrapper de Python, no incluye el motor de OCR).

*  **Windows**: descargá el instalador oficial de [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) y agregá la carpeta de instalación al `PATH`. Si preferís no tocar el `PATH`, podés apuntar directo al ejecutable en el código:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

*  **Linux (Debian/Ubuntu)**:

```bash
sudo apt install tesseract-ocr
```

*  **Mac**:

```bash
brew install tesseract
```

---

Cada archivo está diseñado para enseñar un concepto específico de forma progresiva.

---

##  Estructura del proyecto

```
├── notebooks/       # Los 11 módulos del tutorial en Jupyter Notebook
├── practicas/       # Ejercicios guiados por módulo, con TODOs para completar
├── proyectos/       # Proyecto capstone standalone (reconocimiento facial)
├── scripts/         # verificar_entorno.py y descargar_modelos.py
├── modelos/         # Pesos de modelos DNN descargados (no versionados, ver módulo 10)
├── imgs/            # Imágenes de muestra usadas por los notebooks
├── db/              # Base de rostros usada por el proyecto de reconocimiento facial
└── requirements.txt # Dependencias del proyecto
```

---

##  Contenido del tutorial

1. Funciones básicas: lectura, escalado y rotación de imágenes
2. Procesamiento de imágenes: filtros de color, desenfoque, bordes, morfología y ecualización
3. Detección de características: keypoints y descriptores con ORB y SIFT
4. Transformaciones geométricas: perspectiva
5. Captura de video por webcam
6. Detección de movimiento con sustracción de fondo
7. Seguimiento de objetos (tracking)
8. Detección de personas / reconocimiento facial (capstone, con `proyectos/proyecto.py`)
9. Segmentación y contornos avanzados (Watershed, GrabCut)
10. Detección de objetos con Deep Learning (`cv2.dnn` + YOLOv4-tiny)
11. OCR y reconocimiento de texto (`pytesseract`)

Cada módulo tiene su ejercicio guiado correspondiente en `practicas/`.

---

##  Objetivo del proyecto

Este repositorio busca:

* Facilitar el aprendizaje práctico
* Servir como base para proyectos más avanzados
* Introducir conceptos clave de visión por computadora

---

##  Contribuciones

Las contribuciones son bienvenidas 🙌

Puedes:

* Mejorar ejemplos
* Agregar nuevos ejercicios
* Corregir errores
* Optimizar código

---

##  Autor

**Víctor Castillo**
🔗 [https://github.com/VictorCastillo23](https://github.com/VictorCastillo23)

---
