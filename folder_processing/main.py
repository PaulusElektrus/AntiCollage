import os
from PIL import Image

def split_collage_to_images(collage_path, output_dir, rows, columns):
    try:
        # Öffne die Collage mit Pillow
        collage = Image.open(collage_path)

        # Erhalte die Abmessungen des Collage-Bildes
        collage_width, collage_height = collage.size

        # Berechne die Breite und Höhe jedes Einzelbildes
        tile_width = collage_width // columns
        tile_height = collage_height // rows

        # Stelle sicher, dass das Ausgabeverzeichnis für die Collage existiert oder erstelle es
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

def process_collage_folder(input_folder, output_folder, rows, columns):
    # Liste alle Dateien im Eingabeverzeichnis auf
    collage_files = os.listdir(input_folder)

    # Verarbeite jede Collage im Ordner
    for collage_file in collage_files:
        # Überprüfe, ob die Datei eine Bilddatei ist (z.B. PNG oder JPG)
        if collage_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Konstruiere den vollständigen Pfad zur Collage-Datei
            collage_path = os.path.join(input_folder, collage_file)

            # Erstelle ein separates Ausgabeverzeichnis für die Collage
            collage_output_dir = os.path.join(output_folder, os.path.splitext(collage_file)[0])
            
            # Zerlege die Collage und speichere die Einzelbilder im Ausgabeverzeichnis
            split_collage_to_images(collage_path, collage_output_dir, rows, columns)

def main():
    input_folder = "pfad_zum_eingabeverzeichnis"
    output_folder = "pfad_zum_ausgabeverzeichnis"
    rows = 3  # Anzahl der Reihen
    columns = 3  # Anzahl der Spalten

    # Verarbeite den Ordner mit Collagen
    process_collage_folder(input_folder, output_folder, rows, columns)

if __name__ == "__main__":
    main()
