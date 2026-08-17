from pathlib import Path
import shutil

current_folder = Path(__file__).parent

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
    if file.is_file() and file != Path(__file__):
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

        print(file.name, "->", category)