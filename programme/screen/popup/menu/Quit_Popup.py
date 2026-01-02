<<<<<<< HEAD
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programme.utils.Popup import Popup
from programme.utils.Object import *
from programme.utils.ouvrier import *
=======
import pygame
from utils.Popup import Popup
from utils.Object import *
from player.ouvrier import *
>>>>>>> 9212f0b01ed2a1573c52b80ae04bc537e3cd42a3

class Quit_Popup(Popup):
    def __init__(self, screen, language, position):
        Popup.__init__(self, screen)
        self.rect_panel = None
        self.text_panel = None
        self.btn_yes = None
        self.btn_no = None
        self.language = language

        self.width_panel = 300
        self.height_panel = 100

        self.screen = screen

        self.render(position)

    def render(self,position):
<<<<<<< HEAD
        img_btn = pygame.image.load("../programme/src/img/util/btn_standard.png")
        img_panel = pygame.image.load("../programme/src/img/game_img/background_btn_option.jpg")
=======
        img_btn = pygame.image.load("src/img/util/btn_standard.png")
        img_panel = pygame.image.load("src/img/game_img/background_btn_option.jpg")
>>>>>>> 9212f0b01ed2a1573c52b80ae04bc537e3cd42a3

        self.rect_panel = Rectangle(self.screen,position, (self.width_panel, self.height_panel), img=img_panel)
        self.text_panel = TextView(self.screen, (position[0]+160,position[1]+15), 2, "Voulez vous vraiment quitter ?",'Black', language=self.language)

        self.btn_yes = Button(self.screen, (position[0]+40,position[1]-10+int(self.height_panel/2)), img_btn, 2, self.language,"Yes", 16,'Black', 'White')
        self.btn_no = Button(self.screen, (position[0]+190,position[1]-10+int(self.height_panel/2)), img_btn, 2, self.language,"No", 16,'Black', 'White')


    def update(self):
        if self.get_active():
            Popup.update(self)
            self.rect_panel.update()
            self.btn_yes.update()
            self.btn_no.update()
            self.text_panel.update()


    def event_handler(self,event, function_non, function_yes):
        if self.get_active():
            self.btn_yes.event(event, pygame.mouse.get_pos(),function_yes)
            self.btn_no.event(event, pygame.mouse.get_pos(),function_non)

    def animation_check_color(self):
        if self.get_active():
            self.btn_yes.animation_check_color(pygame.mouse.get_pos())
            self.btn_no.animation_check_color(pygame.mouse.get_pos())