import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Popup import Popup
from utils.Object import *

from utils.Read_Data import read_json

class Wait_Popup(Popup):
    def __init__(self, screen, language, position):
        Popup.__init__(self, screen)
        self.rect_panel = None
        self.text_panel = None
        self.nb_player = None
        self.btn_cancel = None

        self.client_data = None

        self.language = language

        self.width_panel = 500
        self.height_panel = 200

        self.screen = screen

        self.render(position)

    def render(self,position):
        img_btn = pygame.image.load("src/img/util/btn_standard.png")
        img_panel = pygame.image.load("src/img/game_img/background_btn_option.jpg")

        self.rect_panel = RectangleView(self.screen,position, (self.width_panel, self.height_panel), img=img_panel)
        self.text_panel = TextView(self.screen, (position[0]+250,position[1]+20), 3, "logging:popup::text:wait",'Black', language=self.language)
        self.nb_player = TextView(self.screen,(position[0]+250,position[1]+40), 3, "00/00",'Black')
        self.btn_cancel = Button(self.screen, (position[0]+190,position[1]-20+int(self.height_panel/2)), img_btn, 3, self.language,"logging:popup::btn:cancel",'Black', 'White')


    def update(self):
        if self.get_active():
            Popup.update(self)

            self.rect_panel.update()
            self.btn_cancel.update()
            self.text_panel.update()
            data = self.client_data.get_state()

            if data is None:
                return  # on attend encore que le serveur réponde

            wait = data["wait_nb_player"]
            new_ = data["nb_player"]
            self.nb_player.change_text(f"{new_} / {wait}")
            self.nb_player.update()

    def set_client(self,client):
        self.client_data=client

    def event_handler(self,event, function_non):
        if self.get_active():
            self.btn_cancel.event(event, pygame.mouse.get_pos(),function_non)

    def animation_check_color(self):
        if self.get_active():
            self.btn_cancel.animation_check_color(pygame.mouse.get_pos())