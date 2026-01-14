import json
import os
import time

import sys

# la sortie est un tableau soit: data = read_json("file.json")
# data["nom_variable"]
def read_json(path, retry=10, delay=0.1):
    for i in range(retry):
        if not os.path.exists(path):
            time.sleep(delay)
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    print(f"Tentative {i}: Fichier vide")
        except json.JSONDecodeError as e:
            print(f"Tentative {i}: Erreur de lecture JSON ({e})")
        
        time.sleep(delay)
    
    print(f"ERREUR FATALE: Impossible de lire {path} après {retry} essais.")
    return None

# il faut que data soit un tableau
def write_json(file, data):
    with open(file, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def resource_path(relative_path):
    """ Retourne le chemin absolu vers la ressource """
    try:
        base_path = sys._MEIPASS  # PyInstaller
    except AttributeError:
        # Remonter au dossier parent (programme/) depuis utils/
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.normpath(os.path.join(base_path, relative_path))


