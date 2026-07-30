# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Educational tutorial repo (in Spanish) teaching OpenCV computer vision fundamentals with Python, progressing from basic image I/O to a face-recognition project. There is no build system, package manifest, or test suite — each file is a standalone, runnable example.

## Setup

**Requires Python 3.10-3.13.** `deepface` depends on `tensorflow`, which has no wheels for Python 3.14+ yet — creating the venv with 3.14 makes `pip install -r requirements.txt` fail with `ResolutionImpossible`. On Windows, use `py -3.13 -m venv ENTORNO` to pin the interpreter.

Dependencies are listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This covers `opencv-python`, `numpy`, `deepface`, `pyttsx3`, and `pytesseract`. `deepface`/`pyttsx3` are only needed by the face-recognition project (`proyectos/proyecto.py`, `notebooks/8_deteccion_personas.ipynb`). `pytesseract` (module 11) additionally requires the **Tesseract-OCR system binary** — it is not installable via pip alone; see the README's OCR install section for per-OS instructions.

Module 10 (`notebooks/10_deteccion_objetos_dnn.ipynb`) needs YOLOv4-tiny weights in `modelos/`, fetched by running `python scripts/descargar_modelos.py` from the repo root first — the `.cfg`/`.weights`/`.names` files are not committed (binary size; `modelos/` is gitignored).

## Running examples

- `.py` files are run directly, e.g. `python scripts/verificar_entorno.py` (checks `cv2`/`numpy` versions and webcam availability).
- `.ipynb` files are meant to be run cell-by-cell in Jupyter/VS Code, not executed headlessly — several cells call `cv2.imshow` + `cv2.waitKey(0)`, which blocks and requires a display and manual key press to close each window.
- Files that use `cv2.VideoCapture(0)` (`notebooks/5_captura_video.ipynb`, `notebooks/6_deteccion_movimiento.ipynb`, `notebooks/7_seguimiento_objetos.ipynb`, `notebooks/10_deteccion_objetos_dnn.ipynb`, `proyectos/proyecto.py`, `notebooks/8_deteccion_personas.ipynb`) require a connected webcam and will open a live window; exit the loop with the `q` key.

## Structure

The repo root holds `notebooks/`, `practicas/`, `proyectos/`, `scripts/`, `imgs/`, `db/`, `modelos/`, and `requirements.txt`:

- `notebooks/` — the numbered curriculum notebooks (paths are relative to this folder). They read sample images via `../imgs/...` and the face database via `../db`.
- `practicas/` — one guided exercise notebook per module (`N_practica.ipynb`), with `# TODO` markers instead of solved code — the lesson notebooks link to these in a closing "🧪 Práctica" cell.
- `proyectos/` — standalone capstone project(s), currently `proyectos/proyecto.py`.
- `scripts/` — `verificar_entorno.py` (environment/dependency/webcam check) and `descargar_modelos.py` (fetches YOLOv4-tiny weights into `modelos/`).
- `modelos/` — DNN model weights, populated by `scripts/descargar_modelos.py`; gitignored.

The numbered notebooks form a progressive curriculum — later ones assume familiarity with concepts from earlier ones:

1. `notebooks/1_funciones_basicas.ipynb` — reading/showing images, grayscale, resizing, rotation
2. `notebooks/2_procesaciento_imagenes.ipynb` — filter families applied via a shared `show_filters(dict)` helper: color-space, blur, edge-detection (Sobel/Scharr/Canny/Laplacian), morphological, and histogram-equalization filters
3. `notebooks/3_deteccion_caracteristicas.ipynb` — feature detection/description with ORB and SIFT
4. `notebooks/4_transformaciones_geometricas.ipynb` — perspective transforms via point-pair matrices
5. `notebooks/5_captura_video.ipynb` — webcam capture loop basics
6. `notebooks/6_deteccion_movimiento.ipynb` — motion detection via `cv2.createBackgroundSubtractorMOG2`
7. `notebooks/7_seguimiento_objetos.ipynb` — object tracking via `cv2.legacy.TrackerCSRT_create` (MOSSE alternative left commented out)
8. `notebooks/8_deteccion_personas.ipynb` — capstone: face recognition against a local face database
9. `notebooks/9_segmentacion_contornos.ipynb` — contour detection/shape analysis, `cv2.watershed`, `cv2.grabCut`
10. `notebooks/10_deteccion_objetos_dnn.ipynb` — object detection via `cv2.dnn` with YOLOv4-tiny (static image + live webcam)
11. `notebooks/11_ocr_texto.ipynb` — OCR via `pytesseract`, including preprocessing (threshold) and the effect of rotation/noise on accuracy

`proyectos/proyecto.py` is the standalone version of the capstone project (identical logic to `notebooks/8_deteccion_personas.ipynb`):
- Uses `DeepFace.find` against `../db` to identify faces from the webcam feed, matching the `VGG-Face` model.
- `db/<person_name>/*.jpg|jpeg|webp|avif` — one subfolder per known identity; the folder name is used as the display label (parsed out of the matched file path in `reconocimiento()`).
- `db/ds_model_vggface_detector_opencv_aligned_normalization_base_expand_0.pkl` is DeepFace's cached face-embedding index for `db/` — delete it if the `db/` contents change and stale matches occur, so DeepFace regenerates it.
- On identifying a face, `pyttsx3` speaks a greeting ("hola <nombre>") once per change in identity (tracked via `mensajeAnterior`) to avoid repeating the greeting every frame.

`imgs/` holds the static sample images (`img1.jpg`, `img2.jpg`) used by notebooks 1–4, referenced from `notebooks/` as `../imgs/...`.

## Working with notebooks

When editing `.ipynb` files, preserve the existing pattern of markdown cells introducing each filter/technique group followed by a code cell demonstrating it — this repo is read by learners, so the explanatory structure matters as much as the code.
