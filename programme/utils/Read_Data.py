import json
import os
import time

import sys

# la sortie est un tableau soit: data = read_json("file.json")
# data["nom_variable"]
def read_json(path, retry=10, delay=0.1):
    for _ in range(retry):
        if not os.path.exists(path):
            time.sleep(delay)
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
        except json.JSONDecodeError:
            pass  # fichier en cours d'écriture
        time.sleep(delay)
        print(_)
    return None


# il faut que data soit un tableau
def write_json(file, data):
    with open(file, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def resource_path(relative_path):
    """Retourne le chemin correct vers un fichier, même dans un exe PyInstaller"""
    try:
        # _MEIPASS est le dossier temporaire créé par PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Quand on est en mode développement
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)