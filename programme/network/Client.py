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

        # Thread pour recevoir les données du serveur
        self.receive_thread = threading.Thread(target=self.receive_data, daemon=True)
        self.receive_thread.start()

    # Réception des données du serveur
    def receive_data(self):
        while self.running:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break
                with self.lock:
                    self.shared_data = json.loads(data.decode())
                    self.update_json_file()
            except (ConnectionResetError, json.JSONDecodeError):
                break

    # Envoyer les données au serveur
    def send_data(self):
        if not self.running:
            return

        data = j.read_json(self.file)
        if data is None:
            return

        try:
            data["tour"] += 1

            message = json.dumps(data) + "\n"
            self.client_socket.sendall(message.encode())

        except (BrokenPipeError, ConnectionResetError, OSError):
            print("Erreur lors de l'envoi des données")
            self.running = False

    # Sauvegarde côté client
    def update_json_file(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.shared_data, f, indent=4, ensure_ascii=False)

    # Arrêt du client
    def stop(self):
        self.running = False
        self.client_socket.close()
