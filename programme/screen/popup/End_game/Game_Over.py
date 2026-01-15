import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Popup import Popup
from utils.Object import *
from utils.Read_Data import resource_path


class Game_Over(Popup):
    def __init__(self,screen):
        self.screen = screen
        Popup.__init__(self,self.screen)

        self.img_game_over = pygame.image.load(resource_path("src/img/game_img/Game_Over.png"))

        

    def gameisover(self):#appelé depuis game_screen.py en fin de partie
        Popup.update(self)
        self.screen.blit(self.img_game_over, (750, 390))
        pygame.display.flip()
        pygame.mixer.music.load(resource_path("src/sound/game_over.mp3"))
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        
        

def Game_Over_screen(pageset):#appelé depuis main.py en boucle
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:# Si une touche est pressée on quitte l'écran game over
                pageset(0)
                pygame.mixer.music.stop()