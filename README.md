# PNG2PDF — Conversor de Imágenes a PDF en Python

Una herramienta de línea de comandos (CLI) ligera y eficiente escrita en Python para combinar y convertir una o múltiples imágenes (PNG, JPG, JPEG, etc.) en un único archivo PDF.

---

## 🚀 Características

- **Soporte multiformato:** Procesa imágenes PNG, JPG/JPEG y otros formatos compatibles con Pillow.
- **Conversión automática de color:** Convierte automáticamente canales alfa o paletas a modo `RGB` para evitar errores comunes de compatibilidad al generar PDFs.
- **Validación de rutas:** Comprueba la existencia de cada archivo antes de procesarlo para evitar salidas corruptas o incompletas.
- **Orden personalizable:** El PDF compilará las páginas exactamente en el orden en que se pasen las imágenes por consola.

---

## 📦 Requisitos Previos

- **Python 3.7+**
- Biblioteca **Pillow**

Para instalar la dependencia necesaria, ejecuta:

```bash
pip install Pillow
```

---

## 💻 Uso

La sintaxis básica para ejecutar el script es:

```bash
python png2pdf.py <imagen_1> [imagen_2 ...] -o <salida.pdf>
```

### Argumentos

| Parámetro | Tipo | Obligatorio | Descripción |
| :--- | :---: | :---: | :--- |
| `imagenes` | Posicional | **Sí** | Una o más rutas a imágenes separadas por espacios. |
| `-o`, `--output` | Opción | **Sí** | Nombre o ruta del archivo PDF de salida. |
| `-h`, `--help` | Bandera | No | Muestra el mensaje de ayuda y las opciones disponibles. |

---

## 🛠️ Ejemplos Prácticos

### 1. Convertir una sola imagen a PDF

```bash
python png2pdf.py documento.png -o documento.pdf
```

### 2. Combinar varias imágenes en un solo PDF

El orden de las imágenes en el comando determinará el orden de las páginas en el PDF resultante:

```bash
python png2pdf.py portada.png pagina1.jpg pagina2.png -o reporte_completo.pdf
```

### 3. Convertir todas las imágenes PNG de una carpeta (usando comodines)

En sistemas compatibles con expansión de terminal (*globbing* como Linux/macOS o PowerShell/Bash):

```bash
python png2pdf.py *.png -o resultado.pdf
```

---

## 📂 Estructura del Script

```python
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description="Convertir imágenes a PDF")
parser.add_argument(
    "imagenes",
    nargs="+",
    help="Una o más imágenes PNG/JPG"
)
parser.add_argument(
    "--output",
    "-o",
    required=True,
    help="Nombre del PDF de salida"
)

args = parser.parse_args()

imagenes = []

for archivo in args.imagenes:
    if not os.path.exists(archivo):
        print(f"Error: No existe {archivo}")
        exit(1)

    img = Image.open(archivo).convert("RGB")
    imagenes.append(img)

imagenes[0].save(
    args.output,
    save_all=True,
    append_images=imagenes[1:]
)

print(f"PDF creado: {args.output}")
```

---

## ⚠️ Notas Técnicas

- **Canal Alfa (Transparencias):** Al utilizar `.convert("RGB")`, los fondos transparentes de imágenes PNG se rellenarán automáticamente con color negro por defecto de Pillow. Si requieres fondo blanco para transparencias, se recomienda componer la imagen sobre un lienzo blanco antes de la conversión.
- **Tamaño de salida:** El PDF final conservará la resolución nativa en píxeles de cada imagen.
