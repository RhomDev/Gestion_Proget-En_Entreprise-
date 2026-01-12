import pygame

# actionneur
class Button:
    def __init__(
            self,
            screen,
            position,
            image,
            scale,
            language=None,text="",
            color_input="Black",
            color_input1="White",
            position_text=(0, 0),
            police_taille=1,
            taille=(0, 0),
            argument=None,
            function=None,

    ):
        self.text_rect = None
        self.rect = None
        self.argument = argument
        self.main_font = pygame.font.SysFont("Arial", police_taille * 8 * scale)
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
        self.taille = taille
        self.language = language
        self.piece_ferme = False

        self.hovered = False
        self.function = function
        # Charger et redimensionner l'image
        dim = (int(image.get_width() * scale), int(image.get_height() * scale))
        self.change_dim(dim, police_taille * 8 * scale)
        if self.taille != (0, 0):
            self.change_dim(self.taille, police_taille)


    def update(self):
        self.screen.blit(self.image, self.rect)
        if self._input_text != "":
            self.screen.blit(self.text, self.text_rect)
        if self.hovered and self.function is not None:
            self.function()

    def change_dim(self,dim, police_taille):
        image = self.image
        self.image = pygame.transform.scale(image, dim)
        self.rect = pygame.Rect(self.position, dim)
        if self._input_text != "":
            _text = (self._input_text if self.language is None else self.language.get_text(self._input_text))
            self.text = self.main_font.render(_text, True, self._input_color)
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

    def get_text(self):
        return self._input_text

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
        _text = (self._input_text if self.language is None else self.language.get_text(self._input_text))
        self.text = self.main_font.render(_text, True, self._input_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def change_color(self, color):
        _text = (self._input_text if self.language is None else self.language.get_text(self._input_text))
        self.text = self.main_font.render(_text, True, color)

    def set_input_color1(self,color):
        self._input_color1=color
    def set_input_color(self,color):
        self._input_color=color

    def animation_check_color(self, position):
        if self._input_text != "":
            if self.rect.collidepoint(position):
                self.change_color(self._input_color1)
            else:
                self.change_color(self._input_color)
    def filtre(self, tint_color):
        surf = self.image.copy().convert_alpha()
        tint = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
        tint.fill((*tint_color, 0))

    def event(self, event, position, function):
        if self.rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN and self.actif:
                function()
                print("BUTTON " , self.get_text())
            self.hovered = True
        else:
            self.hovered = False

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

        self.hint = TextView(screen,(position[0]+50,position[1]+(dimension[1]/2)),1,text_hint,'gray',police=int(font_size/2), language=lang)

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
            if self.text == "":
                self.hint.update()


# visuelle
class TextView:
    def __init__(self, screen,position,scale,text,color_input,language=None,
        color_input1=(255, 255, 255),police=8,function=None,box_size=(300, 100)
    ):
        self.screen = screen
        self.main_font = pygame.font.SysFont("Arial", police * scale)

        self.function = function
        self.hovered = False

        self._input_text = text
        self.language = language
        self._input_color = color_input
        self._input_color1 = color_input1

        self.position_text = position

        self.box_rect = pygame.Rect(0, 0, *box_size)
        self.box_rect.center = position

        self.lines = []
        self._wrap_text()

    def _wrap_text(self):
        self.lines = []
        text = self._input_text if self.language is None else self.language.get_text(self._input_text)
        words = text.split(" ")

        current_line = ""
        for word in words:
            test_line = current_line + (" " if current_line else "") + word
            width, _ = self.main_font.size(test_line)

            if width <= self.box_rect.width:
                current_line = test_line
            else:
                self.lines.append(current_line)
                current_line = word

        if current_line:
            self.lines.append(current_line)

    def update(self):
        color = self._input_color1 if self.hovered else self._input_color

        total_height = len(self.lines) * self.main_font.get_height()
        y = self.box_rect.centery - total_height // 2

        for line in self.lines:
            surf = self.main_font.render(line, True, color)
            rect = surf.get_rect(centerx=self.box_rect.centerx, y=y)
            self.screen.blit(surf, rect)
            y += self.main_font.get_height()

        if self.hovered and self.function is not None:
            self.function()

    def change_text(self, text):
        self._input_text = text
        self._wrap_text()

    def change_dim(self, dim, police_taille=None):
        self.box_rect.size = dim
        if police_taille is not None:
            self.main_font = pygame.font.SysFont("Arial", police_taille)
        self._wrap_text()

    def change_position(self, position):
        self.position_text = position
        self.box_rect.center = position

    def change_color(self, color):
        self._input_color = color

    def animation_check_color(self, position):
        self.hovered = self.box_rect.collidepoint(position)

    def draw_debug(self, color=(255, 0, 0)):
        pygame.draw.rect(self.screen, color, self.box_rect, 1)

class ImageView:
    def __init__(self, screen, position, scale, image_path):
        self.screen = screen
        self.position = position
        self.scale = scale

        # Chargement image
        self._image_path = image_path
        self._original_image = pygame.image.load(image_path).convert_alpha()

        self.image = self._scale_image(self._original_image)
        self.rect = self.image.get_rect(center=position)

    def _scale_image(self, image):
        width = image.get_width() * self.scale
        height = image.get_height() * self.scale
        return pygame.transform.scale(image, (width, height))

    def update(self):
        self.screen.blit(self.image, self.rect)

    def change_image(self, image_path):
        self._image_path = image_path
        self._original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self._scale_image(self._original_image)
        self.rect = self.image.get_rect(center=self.position)

    def change_scale(self, scale):
        self.scale = scale
        self.image = self._scale_image(self._original_image)
        self.rect = self.image.get_rect(center=self.position)
class RectangleView:
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
    def __init__(s,list_bouton,position_bas,size,up=None,down=None,police_taille=20,nombre_bouton_affiche=3):
        s.size = size
        s.nombre_bouton_affiche=nombre_bouton_affiche
        s.liste=list_bouton
        if nombre_bouton_affiche < len(s.liste):
            s.n=nombre_bouton_affiche
        else:
            s.n=len(s.liste)
        print("nombre de bouton affiche :",s.n)
        s.index=0
        s.position = [ position_bas[0] , position_bas[1] - size[1]]
        s.affiche= s.liste[s.index:s.index+s.n]
        s.police_taille = police_taille
        s.dim = [size[0],size[1]/(s.n+2)]
        s.up=up
        s.down=down


        s.init_flèche()
        for i in range(len(s.liste)):
            s.deroule(1)
        for i in range(len(s.liste)):
            s.deroule(-1)

    def update(s):
        #print(pygame.mouse.get_pos())
        if s.up is not None:
            s.up.update()
        if s.down is not None:
            s.down.update()
        for i in range(s.n):
            s.affiche[i].update()

    def deroule(s,k):
        if s.index + k + s.n < len(s.liste)+1 and s.index+k >= 0:
            print("index : ",s.index ,"k:", k,"index + s.n:",s.index + s.n,"taille liste", len(s.affiche))
            if len(s.affiche) !=0:
                if k>0:
                    s.affiche[0].actif = False
                if k<0:
                    s.affiche[-1].actif = False
            
            s.index=s.index + k
        s.affiche= s.liste[s.index:s.index+s.n]
        for i in range(s.n):
            boutonpos=[ s.position[0] , s.position[1] + (i+1) * s.dim[1]]
            s.affiche[i].actif = True
            s.affiche[i].change_dim(s.dim,s.police_taille)
            s.affiche[i].change_position(boutonpos)


    def init_flèche(s):
        if s.up is not None:
            fleche_up=[ s.position[0] , s.position[1]]
            s.up.change_position(fleche_up)
            s.up.change_dim(s.dim,s.police_taille)
        if s.down is not None:    
            fleche_down=[ s.position[0] , s.position[1]+s.dim[1]*(s.n+1)]
            s.down.change_position(fleche_down)
            s.down.change_dim(s.dim,s.police_taille)
    
    def change_liste(s,list_bouton):
        s.liste=list_bouton
        s.index=0
        s.affiche= s.liste[s.index:s.index+s.n]
        if s.nombre_bouton_affiche < len(s.liste):
            s.n=s.nombre_bouton_affiche
        else:
            s.n=len(s.liste)
        
        for i in range(len(s.liste)):
            s.deroule(1)
        for i in range(len(s.liste)):
            s.deroule(-1)
        s.init_flèche()

class barre_de_vie:
    def __init__(s,screen,position,dim,scale=1,scale_img=1,color1=(255,20,255),image=None):
        s.position=position
        s.screen=screen
        s.dim=dim
        s.screen=screen
        s.color1=color1
        s.scale=scale
        s.value = 0
        s.scale_img=scale_img
        s.image = pygame.transform.scale(image, (int(dim[0] * scale_img), int(dim[1] * scale_img)))

        s.rect_bar = pygame.Rect([position[0],position[1]-107], (int(dim[0] * scale), int(dim[1] * scale)))
        s.rec_vie = pygame.Rect(position, (int(dim[0] * scale) , int(dim[1] * scale )))

    def update(s):
        s.screen.blit(s.image, s.rect_bar)
        pygame.draw.rect(s.screen, s.color1, s.rec_vie)

    def change_dim(s,dim):
        s.rect = pygame.Rect(s.position, (int(dim[0] * s.scale), int(dim[1] * s.scale)))
        return s.rect
    def set_value(s, vie):
        s.value = vie
        s.rec_vie = s.change_dim( (s.dim[0] * s.value , int(s.dim[1]/8)) )
        print("value burnout :", s.rec_vie)


