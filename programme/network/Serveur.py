import socket
import threading
import json
import random
import utils.Read_Data as j

class Serveur(threading.Thread):
    def __init__(self, host="0.0.0.0", port=5555, file="network/data_serveur.json", nb_wait=0):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.file = file
        j.write_json(file, j.read_json("network/data.json"))

        self.clients = []
        self.lock = threading.Lock()
        self.running = True
        self.init_started = False
        self.shared_data = j.read_json(file)

        self.save_json()
        self.shared_data["wait_nb_player"] = nb_wait

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Serveur lancé sur {self.host}:{self.port}")

        while self.running:
            client_socket, addr = self.server_socket.accept()
            with self.lock:
                client_id = len(self.clients)
                self.clients.append(client_socket)
                self.shared_data["nb_player"] = len(self.clients)
                self.shared_data["players"].append(j.read_json("network/data_player.json"))
                self.synchro_init_serveur()
                self.save_json()
                self.broadcast_state()

            print(f"Client {client_id} connecté")

            threading.Thread(
                target=self.handle_client,
                args=(client_socket, client_id),
                daemon=True
            ).start()

    def handle_client(self, client_socket, client_id):
        buffer = ""
        while self.running:
            try:
                with self.lock:
                    if (self.shared_data["wait_nb_player"] == self.shared_data["nb_player"]) and not self.init_started:
                        self.init_started = True
                        self.select_new_master()
                        self.save_json()
                        self.broadcast_state()

                data = client_socket.recv(4096)
                if not data:
                    break

                buffer += data.decode()
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    msg = json.loads(line)
                    print("Client ", client_id, " -> Serveur:", msg)
                    self.handle_message(client_id, msg)

            except (ConnectionResetError, json.JSONDecodeError):
                break

        self.disconnect_client(client_id)

    def handle_message(self, client_id, msg):
        with self.lock:
            player = self.shared_data["players"][client_id]

            # 🔹 Action du maître
            if msg["type"] == "action" and player["statue"] == 1:
                for i in range(self.shared_data["nb_player"]):
                    self.shared_data["players"][i]["action_realisee"] = msg["action"]

            # 🔹 Tache du maître
            elif msg["type"] == "task":
                for i in range(self.shared_data["nb_player"]):
                    self.shared_data["players"][i]["tache_realisee"] = msg["action"]

            # 🔹 Fin d’animation
            elif msg["type"] == "animation_done":
                if player["action_realisee"] != "":
                    player["action_realisee"] = ""
                if player["tache_realisee"]:
                    player["tache_realisee"] = []

            # 🔹 Fin de tour
            elif msg["type"] == "end_turn" and player["statue"] == 1:
                player["statue"] = 0
                for i in range(self.shared_data["nb_player"]):
                    self.shared_data["players"][i]["tour"] +=1
                self.select_new_master()

            # 🔹 Fin de tour
            elif msg["type"] == "loading_mission":
                player["mission"] = msg["action"]
                player["mission_faite"] = msg["action_second"]

            elif msg["type"] == "credit_bonus":
                player["credit_bonus"] = msg["action"]
           
            elif msg["type"] == "piece_ferme":
                player["piece_ferme"] = msg["action"]

            self.save_json()
            self.broadcast_state()

    def select_new_master(self):
        nombre = random.randint(0, self.shared_data["nb_player"] - 1)
        for i in range(self.shared_data["nb_player"]):
            self.shared_data["players"][i]["statue"] = 0
        self.shared_data["players"][nombre]["statue"] = 1
        self.shared_data["player_maitre"] = nombre

    def broadcast_state(self):

        for idx, client_socket in enumerate(self.clients[:]):
            try:
                message = json.dumps(self.shared_data["players"][idx]) + "\n"
                #print("Serveur -> Client", idx," : ", message)
                client_socket.sendall(message.encode())
            except (BrokenPipeError, ConnectionResetError):
                self.clients.remove(client_socket)

    def save_json(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.shared_data, f, indent=4)

    def disconnect_client(self, client_id):
        with self.lock:
            if client_id < len(self.clients):
                try:
                    self.clients[client_id].close()
                except:
                    pass
                del self.clients[client_id]
            self.shared_data["nb_player"] = len(self.clients)
            print(f"Client {client_id} déconnecté")

    def synchro_init_serveur(self):
        for i in range(len(self.clients)):
            player= self.shared_data["players"][i]
            player["id"] = i
            player["nb_player"] = self.shared_data["nb_player"]
            player["wait_nb_player"] = self.shared_data["wait_nb_player"]