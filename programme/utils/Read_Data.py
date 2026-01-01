import json

# la sortie est un tableau soit: data = read_json("file.json")
# data["nom_variable"]
def read_json(file):
    with open(file, "r+", encoding="utf-8") as file:
        return json.load(file)


# il faut que data soit un tableau
def write_json(file, data):
    with open(file, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
