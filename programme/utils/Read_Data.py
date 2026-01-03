import json
import os


# la sortie est un tableau soit: data = read_json("file.json")
# data["nom_variable"]
def read_json(file):
    if not os.path.exists(file):
        return None

    with open(file, "r", encoding="utf-8") as file:
        content = file.read().strip()
        if content == "":
            return None  # fichier vide → pas d'erreur
        return json.loads(content)


# il faut que data soit un tableau
def write_json(file, data):
    with open(file, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
