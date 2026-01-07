import socket
import threading
import json
import utils.Read_Data as j

class Client(threading.Thread):
    def __init__(self, host="127.0.0.1", port=5555):
        super().__init__(daemon=True)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.running = True

        self.shared_data = j.read_json("network/data_player.json")
        self.lock = threading.Lock()


        self.save_data()

        threading.Thread(target=self.receive_loop, daemon=True).start()

    def receive_loop(self):
        buffer = ""
        while self.running:
            try:
                data = self.socket.recv(4096)
                if not data:
                    break

                buffer += data.decode()
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.shared_data = json.loads(line)
                    self.save_data()
                    print("Client reçu état")

            except:
                break

        self.running = False

    # 🔹 Action du maître
    def send_action(self, action):
        self.send({
            "type": "action",
            "action": action
        })

    # 🔹 Fin d’animation
    def send_animation_done(self):
        self.send({
            "type": "animation_done"
        })

    # 🔹 Fin de tour
    def send_end_turn(self):
        self.send({
            "type": "end_turn"
        })

    def send(self, data):
        if not self.running:
            return
        message = json.dumps(data) + "\n"
        try:
            self.socket.sendall(message.encode())
        except:
            self.running = False

    def get_state(self):
        with self.lock:
            return self.shared_data

    def save_data(self, data=None):
        with self.lock:
            if data is not None:
                self.shared_data = data
            j.write_json("network/data_client.json", self.shared_data)

    def stop(self):
        self.running = False
        self.socket.close()
