import socket
import threading
import json
import utils.Read_Data as j


class Client(threading.Thread):
    def __init__(self, host='127.0.0.1', port=13545, file="network/data_client.json"):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.file = file

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        self.shared_data = None
        self.lock = threading.Lock()
        self.running = True

        self.receive = False

        # Thread pour recevoir les données du serveur
        self.receive_thread = threading.Thread(target=self.receive_data, daemon=True)
        self.receive_thread.start()

    # Réception des données du serveur:
    def receive_data(self):
        while self.running:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break
                with self.lock:
                    self.shared_data = json.loads(data.decode())
                    self.update_json_file()
                print("client : data reçu")

            except (ConnectionResetError, json.JSONDecodeError):
                print("client : erreur json")
                break

    # Envoyer les données au serveur
    def send_data(self):
        if not self.running:
            return
        data = self.shared_data
        if data is None:
            return
        try:
            data["tour"] += 1

            message = json.dumps(data) + "\n"
            self.client_socket.sendall(message.encode())
            print("client : envoi des données")

        except (BrokenPipeError, ConnectionResetError, OSError):
            print("Erreur lors de l'envoi des données")
            self.running = False

    # Sauvegarde côté client
    def update_json_file(self, data=None):
        with open(self.file, "w", encoding="utf-8") as f:
            if data is not None:
                self.shared_data = data
            json.dump(self.shared_data, f, indent=4, ensure_ascii=False)

    def get_received(self):
        return self.receive

    def get_shared_data(self):
        with self.lock:
            return self.shared_data

    # Arrêt du client
    def stop(self):
        self.running = False
        self.client_socket.close()
