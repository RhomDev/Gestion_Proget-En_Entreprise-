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

        self.history_task = ""


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

    def send_task(self, task):
        if self.history_task !=task:
            self.send({
                "type": "task",
                "action": task
            })
            self.history_task=task


        # 🔹 Fin d’animation
    def send_animation_done(self, mise=None):
        self.send({
            "type": "animation_done",
            "action": mise
        })

    # 🔹 Fin de tour
    def send_end_turn(self):
        self.send({
            "type": "end_turn"
        })

    def send_loading_mission(self,mission,mission_faite):
        self.send({
            "type": "loading_mission",
            "action": mission,
            "action_second" : mission_faite
        })
    def send_credit(self,credit):
            self.send({
            "type": "credit_bonus",
            "action": credit,
        })
    def send_piece(self,piece_ferme):
            self.send({
            "type": "piece_ferme",
            "action": piece_ferme,
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
