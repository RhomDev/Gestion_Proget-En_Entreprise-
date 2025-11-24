import pygame

screen, main_font = None, None

def get_info(screen1, main_font1):
    screen = screen1
    main_font = main_font1

class Button:
    def __init__(self, position, image, scale, text="", color_input=(255,255,255), color_input1=(255,255,255), position_text=(0,0)):
        width  = image.get_width()
        height = image.get_height()
        self.rect.topleft = position
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.position_text = position_text
        self.text = main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.position_text)

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def change_text(self, text):
        self._input_text = text

    def change_color(self, color):
        self._input_color = color

    def animation_check_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self._input_text, True, self._input_color)
        else:
            self.text = main_font.render(self._input_text, True, self._input_color1)

class TextView:
    def __init__(self, position, scale, text, color_input, color_input1=(255,255,255),  position_text= (0,0)):
        self.rect.topleft = position
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.text = main_font.render(self._input_text, True, self._input_color)
        self.position_text = position_text
        self.text_rect = self.text.get_rect(center=self.position_text)
        self.inter_actif= False

    def update(self):
        screen.blit(self.text, self.rect)

    def change_text(self, text):
        self._input_text = text

    def change_color(self, color):
        self._input_color = color

    def set_inter_actif(self, inter_actif):
        self.inter_actif = inter_actif

    def animation_check_color(self, position):
        if self.inter_actif:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = main_font.render(self._input_text, True, self._input_color)
            else:
                self.text = main_font.render(self._input_text, True, self._input_color1)