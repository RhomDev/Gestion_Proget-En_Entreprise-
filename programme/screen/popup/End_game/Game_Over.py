import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Popup import Popup
from utils.Object import *
from utils.Read_Data import read_json, write_json, resource_path

from utils.Read_Data import read_json

class Game_Over(Popup):
    def __init__(self,screen):
        Popup.__init__(self,screen)
        self.screen = screen

    def update(self,clock):
        Popup.update(self)
        img_game_over = pygame.image.load(resource_path("src/img/game_img/TestGameOver.png"))
       
        self.screen.blit(img_game_over, (500,500))
        pygame.time.delay(2000)
             
        