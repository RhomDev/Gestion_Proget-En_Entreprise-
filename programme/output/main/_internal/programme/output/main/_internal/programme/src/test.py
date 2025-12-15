import json

fichier_json = "data_serveur.json"
fichier_client_json = "data_client.json"

with open(fichier_client_json, "r", encoding="utf-8") as file:
    data = json.load(file)

with open(fichier_json, "r", encoding="utf-8") as file:
    donnees = json.load(file)

joueur_id = data["id"]
donnees["joueurs"][joueur_id] = data

with open(fichier_json, "w", encoding="utf-8") as file:
    json.dump(donnees, file, indent=4, ensure_ascii=False)
