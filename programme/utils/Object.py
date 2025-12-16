import pygame


class Button:
    def __init__(self,screen,position,image,scale,
                 language=None,text="", police=8,color_input=(255, 255, 255),color_input1=(255, 255, 255),
                 position_text=(0, 0),):

        self.screen = screen
        self.position = position
        self.main_font = pygame.font.SysFont("Arial", 1*police)
        self._input_text = text
        self.language = language

        self.color = color_input
        self._input_color = color_input
        self._input_color1 = color_input1

        self.position_text = position_text

        # Charger et redimensionner l'image
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = pygame.Rect(position, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self._input_text = text

    def update(self):
        self.screen.blit(self.image, self.rect)
        if self._input_text != "":
            text_input = (self._input_text if self.language is None else self.language.get_text(self._input_text))
            text = self.main_font.render(text_input, True, self.color)
            text_rect = text.get_rect(center=self.rect.center)

            self.screen.blit(text, text_rect)

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
        self.rect = self.image.get_rect(
            topleft=position
        )  # Utilise topleft pour positionner le coin supérieur gauche
        if self.text != "":
            self.text_rect = self.text.get_rect(center=self.rect.center)

    def change_text(self, text):
        self._input_text = text

    def change_color(self, color):
        self.color = color

    def change_color_input(self, color):
        self._input_color = color
    def change_color_input1(self, color):
        self._input_color1 = color

    def animation_check_color(self, position):
        if self._input_text != "":
            if self.rect.collidepoint(position):
                self.color = self._input_color1
            else:
                self.color = self._input_color

    def event(self, event, position, function):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(position):
                function()


class TextView:
    def __init__(self, screen, position, scale,
                 text, color_input,police=8,language=None,
                 color_input1=(255, 255, 255)
    ):
        self.screen = screen
        self.main_font = pygame.font.SysFont("Arial", police)
        self.position = position
        self.language=language
        self.rect = pygame.Rect(
            position, (0, 0)
        )  # Rect vide, car TextView n'a pas d'image
        self._input_text = text
        self.color = color_input
        self._input_color = color_input
        self._input_color1 = color_input1


    def update(self):
        text_input = (self._input_text if self.language is None else self.language.get_text(self._input_text))
        text = self.main_font.render(text_input, True, self.color)
        text_rect = text.get_rect(center=self.position)
        self.screen.blit(text, text_rect)

    def change_text(self, text):
        self._input_text = text

    def change_color(self, color):
        self._input_color = color

    def animation_check_color(self, position):
        if self.rect.collidepoint(position):
            self.color = self._input_color1
        else:
            self.color = self._input_color


class Rectangle:
    def __init__(
        self,
        screen,
        position,
        dim=(0, 0),
        scale=1,
        color=None,
        img=None,
    ):
        self.position = position
        self.screen = screen

        self.image = img
        self.color = color

        if img != None:
            if dim != (0, 0):
                self.image = pygame.transform.scale(
                    img, (int(dim[0] * scale), int(dim[1] * scale))
                )
                self.rect = pygame.Rect(
                    position, (int(dim[0] * scale), int(dim[1] * scale))
                )
            else:
                self.image = pygame.transform.scale(
                    img, (int(img.get_width() * scale), int(img.get_height() * scale))
                )
                self.rect = pygame.Rect(
                    position,
                    (int(img.get_width() * scale), int(img.get_height() * scale)),
                )
        else:
            self.rect = pygame.Rect(
                position, (int(dim[0] * scale), int(dim[1] * scale))
            )

    def update(self):
        if self.image != None:
            self.screen.blit(self.image, self.rect)
        elif self.color != None:
            pygame.draw.rect(self.screen, self.color, self.rect)
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
            if dim != (0, 0):
                self.image = pygame.transform.scale(
                    self.image, (int(dim[0]), int(dim[1]))
                )
                self.rect = pygame.Rect(self.position, (int(dim[0]), int(dim[1])))
            else:
                self.image = pygame.transform.scale(
                    self.image,
                    (int(self.image.get_width()), int(self.image.get_height())),
                )
                self.rect = pygame.Rect(
                    self.position,
                    (int(self.image.get_width()), int(self.image.get_height())),
                )
        else:
            self.rect = pygame.Rect(self.position, (int(dim[0]), int(dim[1])))

    def modif(self, dim, position, scale=1, color=None, img=None):
        if img != None:
            if dim != (0, 0):
                self.image = pygame.transform.scale(
                    img, (int(dim[0] * scale), int(dim[1] * scale))
                )
                self.rect = pygame.Rect(
                    position, (int(dim[0] * scale), int(dim[1] * scale))
                )
            else:
                self.image = pygame.transform.scale(
                    img, (int(img.get_width() * scale), int(img.get_height() * scale))
                )
                self.rect = pygame.Rect(
                    position,
                    (int(img.get_width() * scale), int(img.get_height() * scale)),
                )
        else:
            self.rect = pygame.Rect(
                position, (int(dim[0] * scale), int(dim[1] * scale))
            )

class InputBox:
    def __init__(self,screen,lang , position, dimension, font_size=32, text_hint=""):
        self.rect = pygame.Rect(position, dimension)
        self.screen = screen
        self.color = pygame.Color('lightskyblue3')
        self.text = ''
        self.font = pygame.font.Font(None, font_size)
        self.active = False
        self.text_color = pygame.Color('black')
        self.active_color = pygame.Color('gray')
        self.inactive_color = pygame.Color('black')

        self.hint = TextView(screen,position,1,text_hint,'gray',police=font_size, language=lang)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.active_color if self.active else self.inactive_color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Faire quelque chose avec le texte
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def get_text(self):
        return self.text

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.text_color)
        self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        if self.active:
            cursor = pygame.Rect(self.rect.x + 5 + text_surface.get_width(), self.rect.y + 5, 2, self.rect.height - 10)
            pygame.draw.rect(self.screen, self.text_color, cursor)
        else:
            self.hint.update()