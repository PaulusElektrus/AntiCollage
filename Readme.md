# AntiCollage
# Collage-Zerleger

Ein Python Command Line Tool, das eine Foto-Collage in mehrere Einzelbilder zerlegt.

## Installation

1. Stelle sicher, dass du Python installiert hast. Das Tool wurde mit Python 3 getestet.

2. Installiere die erforderlichen Abhängigkeiten mit pip:

   ```bash
   pip install pillow
   ```

## Verwendung

Führe das Skript `collage_zerleger.py` in der Kommandozeile aus, um die Collage zu zerlegen.

```bash
python collage_zerleger.py collage.png ausgabeverzeichnis 3 3
```

Ersetze `collage.png` durch den Pfad zur Foto-Collage und `ausgabeverzeichnis` durch den Pfad zum Verzeichnis, in dem die Einzelbilder gespeichert werden sollen. `3` und `3` sind die Anzahl der Reihen und Spalten, in die die Collage zerlegt werden soll.

## Argumente

- `collage_path`: Der Pfad zur Foto-Collage, die in Einzelbilder zerlegt werden soll.
- `output_dir`: Der Pfad zum Ausgabeverzeichnis, in dem die Einzelbilder gespeichert werden.
- `rows`: Anzahl der Reihen, in die die Collage zerlegt werden soll.
- `columns`: Anzahl der Spalten, in die die Collage zerlegt werden soll.

## Beispiel

Angenommen, du hast eine Collage mit dem Namen `collage.png` und möchtest sie in eine 3x3-Matrix von Einzelbildern zerlegen und diese im Verzeichnis `output_images` speichern, dann kannst du das Tool wie folgt ausführen:

```bash
python collage_zerleger.py collage.png output_images 3 3
```

Die Einzelbilder werden dann als `tile_0_0.png`, `tile_0_1.png`, ..., `tile_2_2.png` im Verzeichnis `output_images` gespeichert.
