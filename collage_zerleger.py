import argparse
from PIL import Image
import os

def split_collage_to_images(collage_path, output_dir, rows, columns):
    try:
        # Öffne die Collage mit Pillow
        collage = Image.open(collage_path)

        # Erhalte die Abmessungen des Collage-Bildes
        collage_width, collage_height = collage.size

        # Berechne die Breite und Höhe jedes Einzelbildes
        tile_width = collage_width // columns
        tile_height = collage_height // rows

        # Stelle sicher, dass das Ausgabeverzeichnis existiert oder erstelle es
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Zerlege die Collage in Einzelbilder
        for row in range(rows):
            for column in range(columns):
                # Bestimme den Bereich des aktuellen Einzelbildes
                left = column * tile_width
                top = row * tile_height
                right = left + tile_width
                bottom = top + tile_height

                # Schneide das Einzelbild aus der Collage
                tile = collage.crop((left, top, right, bottom))

                # Speichere das Einzelbild als separate Datei
                output_path = os.path.join(output_dir, f"tile_{row}_{column}.png")
                tile.save(output_path)

        print(f"Collage wurde in {rows}x{columns} Einzelbilder zerlegt und gespeichert.")
    
    except Exception as e:
        print(f"Fehler beim Zerlegen der Collage: {e}")

def main():
    parser = argparse.ArgumentParser(description="Zerlege eine Foto-Collage in Einzelbilder.")
    parser.add_argument("collage_path", type=str, help="Pfad zur Foto-Collage.")
    parser.add_argument("output_dir", type=str, help="Pfad zum Ausgabeverzeichnis für die Einzelbilder.")
    parser.add_argument("rows", type=int, help="Anzahl der Reihen.")
    parser.add_argument("columns", type=int, help="Anzahl der Spalten.")
    args = parser.parse_args()

    split_collage_to_images(args.collage_path, args.output_dir, args.rows, args.columns)

if __name__ == "__main__":
    main()
