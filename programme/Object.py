import pygame

# Suppression des variables globales inutiles
class Button:
    def __init__(self, position, image, scale, text="", color_input=(255,255,255), color_input1=(255,255,255), position_text=(0,0)):
        self.main_font = pygame.font.SysFont("Arial", 8*scale)
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.position_text = position_text

        # Charger et redimensionner l'image
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = pygame.Rect(position, (int(image.get_width() * scale), int(image.get_height() * scale)))

        # Rendu du texte
        if text != "":
            self.text = self.main_font.render(self._input_text, True, self._input_color)
            self.text_rect = self.text.get_rect(center=self.rect.center)
        else:
            self.text = text

    def update(self, screen):
        screen.blit(self.image, self.rect)
        if self.text != "":
            screen.blit(self.text, self.text_rect)

    def change_text(self, text):
        self._input_text = text
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def change_color(self, color):
        self._input_color = color
        self.text = self.main_font.render(self._input_text, True, self._input_color)

    def animation_check_color(self,position):
        if self.text != "":
            if self.rect.collidepoint(position):
                self.text = self.main_font.render(self._input_text, True, self._input_color1)
            else:
                self.text = self.main_font.render(self._input_text, True, self._input_color)

    def event(self,event, position, function):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(position):
                function()

class TextView:
    def __init__(self, screen, main_font, position, scale, text, color_input, color_input1=(255,255,255), position_text=(0,0)):
        self.screen = screen
        self.main_font = main_font
        self.rect = pygame.Rect(position, (0, 0))  # Rect vide, car TextView n'a pas d'image
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.position_text = position_text
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=position_text)
        self.inter_actif = False

    def update(self):
        self.screen.blit(self.text, self.text_rect)

    def change_text(self, text):
        self._input_text = text
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.position_text)

    def change_color(self, color):
        self._input_color = color
        self.text = self.main_font.render(self._input_text, True, self._input_color)

    def set_inter_actif(self, inter_actif):
        self.inter_actif = inter_actif

    def animation_check_color(self, position):
        if self.inter_actif:
            if self.rect.collidepoint(position):
                self.text = self.main_font.render(self._input_text, True, self._input_color)
            else:
                self.text = self.main_font.render(self._input_text, True, self._input_color1)
