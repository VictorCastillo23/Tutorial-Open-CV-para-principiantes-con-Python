"""Descarga los archivos del modelo YOLOv4-tiny necesarios para el módulo 10.

Descarga a la carpeta `modelos/` (en la raíz del repo) los 3 archivos que
necesita `cv2.dnn` para correr detección de objetos con YOLOv4-tiny:
- yolov4-tiny.cfg      (arquitectura de la red, formato Darknet)
- yolov4-tiny.weights  (pesos entrenados sobre el dataset COCO)
- coco.names           (las 80 clases del dataset COCO, una por línea)

Uso (desde la raíz del repo):
    python scripts/descargar_modelos.py

No agrega dependencias nuevas: usa únicamente `urllib.request` de la
librería estándar de Python.
"""

import os
import urllib.error
import urllib.request

# URL oficial: verificar si cambia (repo AlexeyAB/darknet, rama master)
URL_CFG = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg"

# URL oficial: verificar si cambia (repo AlexeyAB/darknet, rama master)
URL_NAMES = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names"

# URL oficial: verificar si cambia (release "darknet_yolo_v4_pre" del repo AlexeyAB/darknet)
URL_WEIGHTS = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"

CARPETA_MODELOS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "modelos")

ARCHIVOS = {
    "yolov4-tiny.cfg": URL_CFG,
    "coco.names": URL_NAMES,
    "yolov4-tiny.weights": URL_WEIGHTS,
}


def descargar(url, destino):
    """Descarga el archivo en `url` y lo guarda en la ruta `destino`.

    Devuelve True si la descarga fue exitosa, False si falló. No propaga
    la excepción cruda: imprime un mensaje de error claro en español.
    """
    try:
        print(f"Descargando {os.path.basename(destino)} desde {url} ...")
        urllib.request.urlretrieve(url, destino)
        print(f"  Listo: {destino}")
        return True
    except urllib.error.URLError as error:
        print(f"  Error: no se pudo descargar {url} ({error}).")
        print("  Verificá tu conexión a internet o si la URL sigue vigente.")
        return False
    except OSError as error:
        print(f"  Error al guardar el archivo en {destino} ({error}).")
        return False


def main():
    os.makedirs(CARPETA_MODELOS, exist_ok=True)
    print(f"Carpeta de destino: {CARPETA_MODELOS}\n")

    resultados = []
    for nombre_archivo, url in ARCHIVOS.items():
        destino = os.path.join(CARPETA_MODELOS, nombre_archivo)
        if os.path.exists(destino):
            print(f"{nombre_archivo} ya existe, se omite la descarga.")
            resultados.append(True)
            continue
        resultados.append(descargar(url, destino))

    print()
    if all(resultados):
        print("Todos los archivos del modelo YOLOv4-tiny se descargaron correctamente.")
    else:
        print("Advertencia: alguno de los archivos no se pudo descargar. Revisá los mensajes de error.")


if __name__ == "__main__":
    main()
