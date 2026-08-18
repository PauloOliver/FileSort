from pathlib import Path
import shutil
import json
import sys

current_folder = Path(__file__).parent

history_file = current_folder / ".filesort_history.json"
history = []

undo = "--undo" in sys.argv

if undo:
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as file:
            history = json.load(file)
    else:
        print("Nenhum histórico encontrado.")
        sys.exit()

    for item in reversed(history):
        original = Path(item["original"])
        destination = Path(item["destination"])

        if destination.exists():
            shutil.move(destination, original)
            print(destination.name, "->", original.parent)

    history_file.unlink()

    print("Organização desfeita.")
    sys.exit()

categories = {
    # Imagens
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".webp": "Imagens",
    ".svg": "Imagens",
    ".ico": "Imagens",
    ".tiff": "Imagens",
    ".tif": "Imagens",
    ".raw": "Imagens",
    ".heic": "Imagens",

    # Vídeos
    ".mp4": "Vídeos",
    ".mkv": "Vídeos",
    ".avi": "Vídeos",
    ".mov": "Vídeos",
    ".wmv": "Vídeos",
    ".flv": "Vídeos",
    ".webm": "Vídeos",
    ".m4v": "Vídeos",
    ".mpeg": "Vídeos",
    ".mpg": "Vídeos",
    ".3gp": "Vídeos",

    # Músicas
    ".mp3": "Músicas",
    ".wav": "Músicas",
    ".flac": "Músicas",
    ".aac": "Músicas",
    ".ogg": "Músicas",
    ".m4a": "Músicas",
    ".wma": "Músicas",
    ".opus": "Músicas",

    # Documentos
    ".pdf": "Documentos",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".odt": "Documentos",
    ".rtf": "Documentos",
    ".txt": "Documentos",
    ".md": "Documentos",
    ".tex": "Documentos",

    # Planilhas
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".xlsm": "Planilhas",
    ".csv": "Planilhas",
    ".ods": "Planilhas",

    # Compactados
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
    ".tar": "Compactados",
    ".gz": "Compactados",
    ".bz2": "Compactados",
    ".xz": "Compactados",

    # Programas
    ".exe": "Programas",
    ".msi": "Programas",
    ".bat": "Programas",
    ".cmd": "Programas",
    ".com": "Programas",
    ".scr": "Programas",
}

for file in current_folder.iterdir():
    if file.is_file() and file != Path(__file__) and file != history_file:
        extension = file.suffix.lower()

        if extension in categories:
            category = categories[extension]
        else:
            category = "Outros"

        category_folder = current_folder / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name

        if destination.exists():
            print(f"Arquivo já existe: {file.name}")
        else:
            shutil.move(file, destination)

            history.append({
                "original": str(file),
                "destination": str(destination)
            })

            print(file.name, "->", category)

with open(history_file, "w", encoding="utf-8") as file:
    json.dump(history, file, indent=4)