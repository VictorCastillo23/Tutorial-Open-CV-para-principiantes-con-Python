"""Verifica que el entorno esté listo para seguir el tutorial.

Comprueba que las dependencias principales (OpenCV y NumPy) estén
instaladas y que haya una webcam accesible para los notebooks que
usan captura de video.
"""

import sys


def verificar_dependencias():
    """Verifica que cv2 y numpy se puedan importar e imprime sus versiones."""
    try:
        import cv2
        import numpy as np
    except ImportError as error:
        print(f"Error: no se pudo importar una dependencia requerida ({error}).")
        print("Instalá las dependencias con: pip install -r requirements.txt")
        return None, None

    print(f"OpenCV instalado correctamente. Versión: {cv2.__version__}")
    print(f"NumPy instalado correctamente. Versión: {np.__version__}")
    return cv2, np


def verificar_webcam(cv2):
    """Verifica si hay una webcam accesible en el índice 0."""
    captura = cv2.VideoCapture(0)
    try:
        if captura.isOpened():
            print("Webcam detectada correctamente en el índice 0.")
        else:
            print("Advertencia: no se detectó ninguna webcam en el índice 0.")
            print("Los notebooks de captura de video no funcionarán sin una cámara conectada.")
    finally:
        captura.release()


def main():
    cv2, np = verificar_dependencias()
    if cv2 is None:
        sys.exit(1)

    verificar_webcam(cv2)


if __name__ == "__main__":
    main()
