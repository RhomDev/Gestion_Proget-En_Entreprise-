import socket
import threading
import time
import json
import random

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programme.utils.Read_Data import write_json


class Serveur(threading.Thread):
    def __init__(self, host='0.0.0.0', port=5555):
        super().__init__()
        self.host = host
        self.port = port
        self.clients = []
        self.shared_data = {}
        self.lock = threading.Lock()
        self.running = True
        self.file = "data_serveur.json"

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Serveur démarré sur {self.host}:{self.port}")

        # Accepter les connexions des clients
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Nouveau client connecté : {addr}")
                self.clients.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except OSError:
                break

        self.server_socket.close()

    def handle_client(self, client_socket):
        while self.running:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break

                received_data = json.loads(data)
                print(f"Reçu du client : {received_data}")
                data = self.update_json(received_data)

                self.update_shared_data(data)

                self.loading_game()

                time.sleep(0.1)

            except (ConnectionResetError, json.JSONDecodeError):
                break

        if client_socket in self.clients:
            self.clients.remove(client_socket)
        client_socket.close()

    def update_json(self, data):
        with open(self.file, "a+", encoding="utf-8") as file:
            donnees = json.load(file)
            donnees["joueurs"][data["id"]] = data
            json.dump(donnees, file, indent=4, ensure_ascii=False)
        return donnees

    def loading_game(self):
        active = 0
        data = self.get_shared_data()
        for i in range(data["nb_player"]):
            active += data["players"][i]["active"]
        if active == data["nb_player"]:
            action = data["players"][data["player_maitre"]]["action_realisee"]
            for i in range(data["nb_player"]):
                data["players"][i]["action_realisee"] = action

            id_player_aleatoire = random.randint(0, data["nb_player"] - 1)
            data["player_maitre"] = id_player_aleatoire
            data["tour_actuel"] += 1

            write_json(self.file_server, data)
            self.broadcast_data()

    def broadcast_data(self):
        for i in (len(self.clients)):
            try:
                with self.lock:
                    data_to_send = self.shared_data["players"][i]
                    self.clients[i].send(data_to_send)
            except (ConnectionResetError, BrokenPipeError):
                # Retirer le client de la liste s'il est déconnecté
                if self.clients[i] in self.clients:
                    self.clients.remove(self.clients[i])

    def stop(self):
        # Arrêter le serveur
        self.running = False
        self.server_socket.close()
        for client in self.clients:
            client.close()
        self.clients = []

    def get_shared_data(self):
        with self.lock:
            return self.shared_data

    def update_shared_data(self, data):
        with self.lock:
            self.shared_data = data


class Client(threading.Thread):
    def __init__(self, host='127.0.0.1', port=5555):
        super().__init__()
        self.host = host
        self.port = port
        self.running = True

        self.shared_data = None
        self.lock = threading.Lock()
        self.file = "data_client.json"

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connecté au serveur {self.host}:{self.port}")
        except Exception as e:
            print(f"Erreur de connexion au serveur {self.host}:{self.port} : {e}")
            raise

        self.receive_thread = threading.Thread(target=self.receive_data, daemon=True)
        self.receive_thread.start()

    def receive_data(self):
        while self.running:
            try:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break

                self.update_shared_data(data)
                self.update_json()

            except (ConnectionResetError, json.JSONDecodeError) as e:
                print(f"Erreur lors de la réception des données : {e}")
                break

    def send_data(self, data):
        try:
            self.client_socket.send(data.encode())
        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"Erreur lors de l'envoi des données : {e}")

    def stop(self):
        self.running = False
        self.client_socket.close()

    def get_shared_data(self):
        with self.lock:
            return self.shared_data

    def update_shared_data(self, data):
        with self.lock:
            self.shared_data = json.loads(data)

    def update_json(self):
        with open(self.file, "w+", encoding="utf-8") as file:
            json.dump(self.get_shared_data(), file, indent=4, ensure_ascii=False)
