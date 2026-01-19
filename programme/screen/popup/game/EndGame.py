import random
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Popup import Popup
from utils.Object import *
from utils.Read_Data import resource_path,read_json

from utils.Constant import Screen


class Game_Over(Popup):
    def __init__(self, screen, language, position):
        _config = read_json(resource_path("config.json"))
        self.screen = screen
        self.language = language
        Popup.__init__(self, self.screen)

        pygame.mixer.music.load(resource_path("src/sound/game_over.mp3"))
        pygame.mixer.music.set_volume(_config["volume_son"])

        self.imgView_over = None
        self.text_over = None

        self.img_game_over =resource_path("src/img/game_img/Game_Over.png")

        self.fade_duration = 3000
        self.current_alpha = 0

        self.time_start = 0
        self.win = False
        self.render(position)

    def render(self,position):
        self.imgView_over = ImageView(self.screen, position, 1, self.img_game_over)
        text = random.choice(self.language.get_text("game:popup::text:over"))
        self.text_over = TextView(self.screen, (position[0],position[1]+200), 3, text,'Red', police=18)


    def change_active(self):
        Popup.change_active(self)
        self.time_start = pygame.time.get_ticks()
        self.current_alpha = 0
        pygame.mixer.music.play()

    def update(self):
        if self.get_active():
            Popup.update(self)
            delay = pygame.time.get_ticks() - self.time_start

            if delay < self.fade_duration:
                self.current_alpha = int(255 * (delay / self.fade_duration))
            else:
                self.current_alpha = 255
            self.rect_surface.set_alpha(self.current_alpha)
            self.imgView_over.set_alpha(self.current_alpha)
            self.text_over.set_alpha(self.current_alpha)

            self.imgView_over.update()
            self.text_over.update()

    def out_game(self, client, serveur, change_page):
        if self.get_active():
            if client() is not None:
                client().stop()
            if serveur() is not None:
                serveur().stop()
            change_page(Screen.MENU.value)
            pygame.mixer.music.stop()


class Game_Win(Popup):
    def __init__(self, screen, language, position):
        _config = read_json(resource_path("config.json"))
        self.screen = screen
        self.language = language
        Popup.__init__(self, self.screen)


        pygame.mixer.music.load(resource_path("src/sound/game_over.mp3"))
        pygame.mixer.music.set_volume(_config["volume_son"])

        self.imgView_win = None
        self.text_win = None

        img_game_win_1 = resource_path("src/img/game_img/win/Win_1.png")
        img_game_win_2 = resource_path("src/img/game_img/win/Win_2.png")
        self.img_win = random.choice([img_game_win_1, img_game_win_2])

        self.img_game_mega_win =resource_path("src/img/game_img/win/mega_win.jpg")

        self.fade_duration = 3000
        self.current_alpha = 0

        self.time_start = 0
        self.win = False
        self.render(position)

    def render(self,position):
        self.imgView_win = ImageView(self.screen, position, 2, self.img_win)
        self.text_win = TextView(self.screen, (position[0],position[1]+250), 3, "game:popup::text:win",'White', language=self.language, police=18)

    def change_win(self):
        self.win = True

    def change_active(self):
        Popup.change_active(self)
        self.time_start = pygame.time.get_ticks()
        self.current_alpha = 0
        pygame.mixer.music.play()

    def update(self):
        if self.get_active():
            Popup.update(self)
            delay = pygame.time.get_ticks() - self.time_start

            if delay < self.fade_duration:
                self.current_alpha = int(255 * (delay / self.fade_duration))
            else:
                self.current_alpha = 255

            self.rect_surface.set_alpha(self.current_alpha)
            self.imgView_win.set_alpha(self.current_alpha)
            self.text_win.set_alpha(self.current_alpha)

            if self.win:
                self.imgView_win.change_image(self.img_game_mega_win)
                self.text_win.change_text("game:popup::text:win_mega")
            self.imgView_win.update()
            self.text_win.update()

    def out_game(self, client, serveur, change_page):
        if self.get_active():
            if client() is not None:
                client().stop()
            if serveur() is not None:
                serveur().stop()
            change_page(Screen.MENU.value)
            pygame.mixer.music.stop()


