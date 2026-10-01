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