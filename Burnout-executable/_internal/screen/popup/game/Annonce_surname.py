import sys,os
import pygame
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Popup import Popup
from utils.Object import *

class Annonce_surname_Popup(Popup):
    def __init__(self, screen, language, position):
        Popup.__init__(self, screen)
        self.img_back = None
        self.text_panel = None
        self.language = language

        self.width_panel = 300
        self.height_panel = 100

        self.fade_duration = 1000
        self.current_alpha = 0

        self.time_start = 0

        self.screen = screen

        self.render(position)

    def render(self,position):
        img_ = pygame.image.load("src/img/game_img/btn_tour.png")
        img_ = pygame.transform.scale(img_, (500, 100))

        self.img_back = ImageView(self.screen, position, 1,"", image_=img_)
        text = self.language.get_text("game:popup::text:annonce")
        self.text_panel = TextView(self.screen, position, 1,f"{text} : player", 'Black', police=23)

    def change_active(self, player):
        Popup.change_active(self)
        text = self.language.get_text("game:popup::text:annonce")
        self.text_panel.change_text(f"{text} : {player}")
        self.time_start = pygame.time.get_ticks()
        self.current_alpha = 0

    def update(self):
        if self.get_active():
            Popup.update(self)

            delay = pygame.time.get_ticks() - self.time_start

            if delay < self.fade_duration:
                self.current_alpha = int(255 * (delay / self.fade_duration))
            elif (2*self.fade_duration) < delay < (3*self.fade_duration):
                self.current_alpha = 255 - int(255 * (delay / (3*self.fade_duration)))
            elif delay >= (3*self.fade_duration):
                self.current_alpha = 0
                Popup.set_active(self,False)
            else:
                self.current_alpha = 255


            self.img_back.set_alpha(self.current_alpha)
            self.text_panel.set_alpha(self.current_alpha)

            self.img_back.update()
            self.text_panel.update()