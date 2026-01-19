import socket
import threading
import json

import pygame

import utils.Read_Data as j

class Client(threading.Thread):
    def __init__(self, host="127.0.0.1", port=5555, player_name="", time_out=10.0):
        super().__init__(daemon=True)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(time_out)  # Timeout de 10 secondes pour la connexion
        try:
            self.socket.connect((host, port))
            self.socket.settimeout(None)  # Retire le timeout après la connexion
            self.running = True

            self.shared_data = j.read_json("network/data_player.json")
            self.lock = threading.Lock()

            self.save_data()
            self.send_init("name", player_name)
            threading.Thread(target=self.receive_loop, daemon=True).start()

        except socket.timeout:
            print("Timeout : Impossible de se connecter au serveur dans les 10 secondes.")
            self.socket.close()
            raise
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            self.socket.close()
            raise

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

            except Exception as e:
                print(f"reception : {e}")
                break

        self.running = False

    # Chargement des datas initial
    def send_init(self, key, value):
        self.send({
            "type": "init",
            "key": key,
            "value": value,
            "time": pygame.time.get_ticks()
        })

    # 🔹 Action du maître
    def send_action(self, action):
        print("action")
        self.send({
            "type": "action",
            "action": action,
            "time": pygame.time.get_ticks()
        })

    def send_task(self, task):
        self.send({
            "type": "task",
            "action": task,
            "time": pygame.time.get_ticks()
        })


        # 🔹 Fin d’animation
    def send_animation_done(self, mise=None):
        print("animation_done")
        self.send({
            "type": "animation_done",
            "action": mise,
            "time": pygame.time.get_ticks()
        })

    # 🔹 Fin de tour
    def send_end_turn(self):
        print("end_turn")
        self.send({
            "type": "end_turn",
            "time":pygame.time.get_ticks()
        })

    def send_win(self):
        self.send({
            "type": "player_win",
            "time":pygame.time.get_ticks()
        })

    def send_loading_mission(self,mission,mission_faite):
        print("loading_mission")
        self.send({
            "type": "loading_mission",
            "action": mission,
            "action_second" : mission_faite
        })

    def send(self, data):
        if not self.running:
            print("send_error")
            return
        message = json.dumps(data) + "\n"
        try:
            print("send : ", message)
            self.socket.send(message.encode())
            self.socket.sendall(message.encode())
        except Exception as e:
            print(f"Erreur de connexion : {e}")
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
