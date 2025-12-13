import pygame

class Button:
    def __init__(self, screen, position, image, scale, text="", color_input=(255,255,255), color_input1=(255,255,255), position_text=(0,0)):
        self.main_font = pygame.font.SysFont("Arial", 8*scale)
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.position_text = position_text
        self.screen =screen
        self.position=position

        # Charger et redimensionner l'image
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = pygame.Rect(position, (int(image.get_width() * scale), int(image.get_height() * scale)))

        # Rendu du texte
        if text != "":
            self.text = self.main_font.render(self._input_text, True, self._input_color)
            self.text_rect = self.text.get_rect(center=self.rect.center)
        else:
            self.text = text

    def update(self):
        self.screen.blit(self.image, self.rect)
        if self.text != "":
            self.screen.blit(self.text, self.text_rect)

    def get_rect(self):
        return self.rect

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def get_image(self):
        return self.image

    def get_screen(self):
        return self.screen

    def change_image(self, image):
        self.image = image

    def change_position(self, position):
        self.position = position
        self.rect = self.image.get_rect(topleft=position)  # Utilise topleft pour positionner le coin supérieur gauche
        if self.text != "":
            self.text_rect = self.text.get_rect(center=self.rect.center)

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

class Rectangle:
    def __init__(self, screen, position, dim=(0,0), scale=1, color=None, img=None, ):
        self.position = position
        self.screen = screen

        self.image = img
        self.color = color

        if img != None:
            if dim != (0,0):
                self.image = pygame.transform.scale(img,
                                                    (int(dim[0] * scale), int(dim[1] * scale)))
                self.rect = pygame.Rect(position, (int(dim[0] * scale), int(dim[1] * scale)))
            else:
                self.image = pygame.transform.scale(img,
                                                    (int(img.get_width() * scale), int(img.get_height() * scale)))
                self.rect = pygame.Rect(position, (int(img.get_width() * scale), int(img.get_height() * scale)))
        else:
            self.rect = pygame.Rect(position, (int(dim[0] * scale), int(dim[1] * scale)))

    def update(self):
        if self.image != None:
            self.screen.blit(self.image, self.rect)
        elif self.color != None:
            pygame.draw.rect(self.screen , self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.rect)

    def get_rect(self):
        return self.rect

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def get_image(self):
        return self.image

    def get_screen(self):
        return self.screen

    def change_position(self, position):
        self.position = position
        if self.image is not None:
            self.rect = self.image.get_rect(topleft=position)
        else:
            self.rect = pygame.Rect(position, self.rect.size)

    def change_color(self, color):
        self.color = color

    def change_image(self, image):
        self.image = image

    def change_dim(self, dim):
        if self.image != None:
            if dim != (0,0):
                self.image = pygame.transform.scale(self.image,
                                                    (int(dim[0]), int(dim[1])))
                self.rect = pygame.Rect(self.position, (int(dim[0]), int(dim[1])))
            else:
                self.image = pygame.transform.scale(self.image,
                                                    (int(self.image.get_width()), int(self.image.get_height())))
                self.rect = pygame.Rect(self.position, (int(self.image.get_width()), int(self.image.get_height())))
        else:
            self.rect = pygame.Rect(self.position, (int(dim[0]), int(dim[1])))

    def modif(self, dim, position, scale=1, color=None, img=None):
        if img != None:
            if dim != (0, 0):
                self.image = pygame.transform.scale(img,
                                                    (int(dim[0] * scale), int(dim[1] * scale)))
                self.rect = pygame.Rect(position, (int(dim[0] * scale), int(dim[1] * scale)))
            else:
                self.image = pygame.transform.scale(img,
                                                    (int(img.get_width() * scale), int(img.get_height() * scale)))
                self.rect = pygame.Rect(position, (int(img.get_width() * scale), int(img.get_height() * scale)))
        else:
            self.rect = pygame.Rect(position, (int(dim[0] * scale), int(dim[1] * scale)))

