import socket
import threading
import json
import time
import random

import utils.Read_Data as j


class Serveur(threading.Thread):
    def __init__(self, host='0.0.0.0', port=13546, file="network/data_serveur.json", nb_wait=0):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.file = file

        self.clients = []  # liste des sockets clients
        self.shared_data = {}  # données partagées (JSON)
        self.lock = threading.Lock()
        self.running = True

        # Charger le JSON existant
        self.load_json()
        with self.lock:
            self.shared_data = j.read_json("network/data.json")
            self.shared_data["wait_nb_player"] = nb_wait
            self.save_json()

    # Charger le JSON existant
    def load_json(self):
        with open(self.file, "r", encoding="utf-8") as f:
            self.shared_data = json.load(f)

    # Sauvegarder le JSON
    def save_json(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.shared_data, f, indent=4, ensure_ascii=False)

    # Lancement du serveur
    def run(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            print(f"Serveur démarré sur {self.host}:{self.port}")
        except OSError as e:
            print(f"Erreur serveur lors du bind : {e}")
            self.running = False
            return  # Arrêter le thread si le port est occupé

        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Nouveau client connecté : {addr}")

                new_id = len(self.clients)

                self.clients.append(client_socket)

                with self.lock:
                    self.shared_data["nb_player"]+=1
                    self.shared_data["players"][new_id]["wait_new"][0]=self.shared_data["wait_nb_player"]
                    self.shared_data["players"][new_id]["wait_new"][1] = new_id+1
                    self.save_json()
                self.synchronize_players(new_id)

                self.broadcast_all()

                # Thread pour gérer ce client
                threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, new_id),
                    daemon=True
                ).start()

            except OSError:
                break

    # Gestion d'un client
    def handle_client(self, client_socket, client_id):
        buffer = ""

        while self.running:
            try:
                data = client_socket.recv(4096)
                if not data:
                    break

                buffer += data.decode()

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    received_data = json.loads(line)

                    print(f"Reçu du client {client_id} :", received_data)

                    with self.lock:
                        self.shared_data["players"][client_id].update(received_data)
                        self.save_json()

                    self.synchronize_players(client_id)
                    self.change_player()
                    self.broadcast_all()

            except (ConnectionResetError, json.JSONDecodeError):
                break

        self.disconnect_client(client_id)

    def synchronize_players(self, original_id):
        with self.lock:
            original_player = self.shared_data["players"][original_id]

            for i, player in enumerate(self.shared_data["players"]):
                if i != original_id:
                    player_id = player["id"]
                    self.shared_data["players"][i] = original_player.copy()
                    self.shared_data["players"][i]["id"] = player_id
                    self.shared_data["players"][i]["statue"] = 2
            self.save_json()

    def change_player(self):
        nombre = random.randint(0, len(self.clients) - 1)
        print(f"le nouveau maitre client {nombre}")
        with self.lock:
            for i in range(len(self.clients)):
                self.shared_data["players"][i]["statue"] = 0
            self.shared_data["players"][nombre]["statue"] = 1
            self.shared_data["player_maitre"] = nombre
            # Mettre à jour le JSON serveur
            self.save_json()

    # Diffuser les données à tous les clients
    def broadcast_all(self):
        with self.lock:
            for idx, client_socket in enumerate(self.clients[:]):
                try:
                    message = json.dumps(self.shared_data["players"][idx]) + "\n"
                    client_socket.sendall(message.encode())
                except (BrokenPipeError, ConnectionResetError):
                    self.disconnect_client(idx)


    def broadcast_local(self,id):
        with self.lock:
                try:
                    message = json.dumps(self.shared_data["players"][id]).encode()
                    self.clients[id].sendall(message)
                except (BrokenPipeError, ConnectionResetError):
                    print(f"Client {id} déconnecté")
                    self.clients.remove(id)

    # Arrêter le serveur
    def stop(self):
        self.running = False
        self.server_socket.close()
        for client in self.clients:
            client.close()
        self.clients.clear()

    # Accès sécurisé aux données partagées
    def get_shared_data(self):
        with self.lock:
            return self.shared_data
