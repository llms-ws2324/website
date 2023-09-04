import os
import json
import glob
from pathlib import Path


# CONVERT
# Convert files from .qmd to .ipynb
for i in glob.iglob('slides/*.qmd'):
    os.system(f"quarto convert {i}")


# MOVE FILES
source_folder = Path('slides/')
destination_folder = Path('code/')
# Alle .ipynb Dateien im Quellordner durchlaufen
for filepath in source_folder.glob('*.ipynb'):
    # Ziel-Pfad konstruieren
    destination = destination_folder / filepath.name
    # Datei verschieben
    filepath.rename(destination)


# JUPYTER NOTEBOOKS ANPASSEN

# Ordner mit den .ipynb Dateien
folder_path = Path('code/')

# Alle .ipynb Dateien im Ordner durchlaufen
for file_path in folder_path.glob('*.ipynb'):
    with file_path.open('r', encoding='utf-8') as file:
        notebook_content = json.load(file)

    # Ersetze ". . ." durch "" in allen Zellen
    for cell in notebook_content['cells']:
        if cell['cell_type'] == 'markdown':
            cell['source'] = [line.replace('. . .', '')
                              for line in cell['source']]

    # Finden und Entfernen der ersten Markdown-Zelle
    for index, cell in enumerate(notebook_content['cells']):
        if cell['cell_type'] == 'raw':
            del notebook_content['cells'][index]
            break

    # Finden und Entfernen der letzten Markdown-Zelle
    for index in reversed(range(len(notebook_content['cells']))):
        if notebook_content['cells'][index]['cell_type'] == 'markdown':
            del notebook_content['cells'][index]
            break

    # Den modifizierten Inhalt zurück in die Datei schreiben
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(notebook_content, file, ensure_ascii=False, indent=4)
