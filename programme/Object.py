import pygame


class Button:
    def __init__(
        self,
        screen,
        position,
        image,
        scale,
        text="",
        color_input="Black",
        color_input1="White",
        position_text=(0, 0),
        police_taille=1
    ):
        self.main_font = pygame.font.SysFont("Arial", police_taille*8 * scale)
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.position_text = position_text
        self.screen = screen
        self.position = position
        self.image = image
        self.scale = scale
        self.text = text
        self.actif = True

        # Charger et redimensionner l'image
        dim=(int(image.get_width() * scale), int(image.get_height() * scale))
        self.change_dim(dim, police_taille * 8 * scale)


    def update(self):
        self.screen.blit(self.image, self.rect)
        if self.text != "":
            self.screen.blit(self.text, self.text_rect)


    def change_dim(self,dim, police_taille):
        image = self.image
        self.image = pygame.transform.scale(image, dim)
        self.rect = pygame.Rect(self.position, dim)
        if self._input_text != "":
            self.text = self.main_font.render(self._input_text, True, self._input_color)
            self.main_font = pygame.font.SysFont("Arial", police_taille )
            self.text_rect = self.text.get_rect(center=self.rect.center)

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
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def change_color(self, color):
        self._input_color = color
        self.text = self.main_font.render(self._input_text, True, self._input_color)

    def animation_check_color(self, position):
        if self.text != "":
            if self.rect.collidepoint(position):
                self.text = self.main_font.render(
                    self._input_text, True, self._input_color1
                )
            else:
                self.text = self.main_font.render(
                    self._input_text, True, self._input_color
                )

    def event(self, event, position, function):
        if event.type == pygame.MOUSEBUTTONDOWN and self.actif:
            if self.rect.collidepoint(position):
                function()


class TextView:
    def __init__(
        self, screen, position, scale, text, color_input, color_input1=(255, 255, 255)
    ):
        self.screen = screen
        self.main_font = pygame.font.SysFont("Arial", 8 * scale)
        self.rect = pygame.Rect(
            position, (0, 0)
        )  # Rect vide, car TextView n'a pas d'image
        self._input_text = text
        self._input_color = color_input
        self._input_color1 = color_input1
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=position)

    def update(self):
        self.screen.blit(self.text, self.text_rect)

    def change_text(self, text):
        self._input_text = text
        self.text = self.main_font.render(self._input_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.position_text)

    def change_color(self, color):
        self._input_color = color
        self.text = self.main_font.render(self._input_text, True, self._input_color)

    def animation_check_color(self, position):
        if self.rect.collidepoint(position):
            self.text = self.main_font.render(
                self._input_text, True, self._input_color1
            )
        else:
            self.text = self.main_font.render(self._input_text, True, self._input_color)


class Rectangle:
    def __init__(self,screen,position, dim=(0, 0),scale=1, color=None, img=None):
        self.position = position
        self.screen = screen

        self.image = img
        self.color = color
        self.centers = [int(position[0]+dim[0]/2) ,int(position[1]+dim[1]/2)  ]

        if img != None:
            if dim != (0, 0):
                self.image = pygame.transform.scale(img, (int(dim[0] * scale), int(dim[1] * scale)))
                self.rect = pygame.Rect(position, (int(dim[0] * scale), int(dim[1] * scale)))
            else:
                self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                self.rect = pygame.Rect(
                    position,(int(img.get_width() * scale), int(img.get_height() * scale)),)
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


class Menu_Deroulent:
    def __init__(s,list_bouton,position_bas,size,up,down,police_taille=20,nombre_bouton_affiche=3):
        s.size = size

        s.liste=list_bouton
        s.n=nombre_bouton_affiche
        s.index=0
        s.position = [ position_bas[0] , position_bas[1] - size[1]* ( 1 + 1/s.n)]
        s.affiche= s.liste[s.index:s.index+s.n]
        s.police_taille = police_taille
        s.dim = [size[0],size[1]/s.n]
        s.up=up
        s.down=down


        s.init_flèche()
        s.deroule(0)
        s.deroule(1)
        s.deroule(-1)
        s.deroule(-1)

    def update(s):
        #print(pygame.mouse.get_pos())
        s.up.update()
        s.down.update()
        for i in range(s.n):
            s.affiche[i].update()

    def deroule(s,k):
        #print(s.index , k)
        if s.index + k + s.n < len(s.liste)+1 and s.index+k >= 0:
            if k>0:
                s.affiche[s.index].actif = False
            if k<0:
                s.affiche[s.index + s.n-2].actif = False
            s.index=s.index + k
        s.affiche= s.liste[s.index:s.index+s.n]
        for i in range(s.n):
            boutonpos=[ s.position[0] , s.position[1]+i*s.dim[1]]
            s.affiche[i].actif = True
            s.affiche[i].change_dim(s.dim,s.police_taille)
            s.affiche[i].change_position(boutonpos)


    def init_flèche(s):
        fleche_up=[ s.position[0] , s.position[1]-s.dim[1]]
        fleche_down=[ s.position[0] , s.position[1]+s.dim[1]*s.n]
        s.up.change_position(fleche_up)
        s.down.change_position(fleche_down)
        s.up.change_dim(s.dim,s.police_taille)
        s.down.change_dim(s.dim,s.police_taille)
