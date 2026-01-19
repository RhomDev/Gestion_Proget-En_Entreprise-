import sys,os
import pygame_gui
import pygame

from utils.Read_Data import write_json, read_json, resource_path
import utils.Object as obj

from utils.Constant import Screen

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_game_screen_init(screen, manager, data, lang):
    manager.get_root_container().clear()

    global dropdown_resolution, volume_slider, btn_return, input_box_tour_serveur,btn_appliquer, \
            checkbox_fullscreen, text_volume, text_nb_tour, text_nb_player, input_box_nb_player,text_langue,dropdown_langue, container
    list_lang = [key for key in lang.get().keys() if key.startswith("language::")]
    option_langue = [lang.get_text(key) for key in list_lang]

    lang_text = data.get("language", "fr-fr")
    text_langue = obj.TextView(screen, (mid_width - 60, mid_height - 330), 3, "option::text:langue", "Black", language=lg)
    dropdown_langue = pygame_gui.elements.UIDropDownMenu(
        options_list=option_langue,
        starting_option=lang.get_text(f"language::{lang_text}"),
        relative_rect=pygame.Rect((mid_width - 100, mid_height - 300), (400, 50)),
        manager=manager
    )
    container.append(dropdown_langue)

    text_nb_tour = obj.TextView(screen, (mid_width, mid_height - 145), 2, "option::text:tour", "Black",language=lg)
    input_box_tour_serveur = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((mid_width-100, mid_height-130), (200, 40)),
        initial_text=str(data.get("nb_tour",20)),
        manager=manager
    )
    container.append(input_box_tour_serveur)

    text_nb_player = obj.TextView(screen, (mid_width+200, mid_height - 145), 2, "option::text:player", "Black", language=lg)
    input_box_nb_player = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((mid_width - 100+200, mid_height - 130), (200, 40)),
        initial_text=str(data.get("nb_player", 2)),
        manager=manager
    )
    container.append(input_box_nb_player)

    text_volume = obj.TextView(screen,(mid_width-20, mid_height-215),3,"option::text:volume", "Black", language=lg)
    volume_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((mid_width-100, mid_height-200), (400, 30)),
        start_value=int(data.get("volume_son",50) * 100),
        value_range=(0, 100),
        manager=manager
    )
    container.append(volume_slider)

    btn_appliquer = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((mid_width + 100, mid_height + 400), (100, 50)),
        text="Appliquer",
        manager=manager
    )
    container.append(btn_appliquer)

    btn_return = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((mid_width-100, mid_height+400), (100, 50)),
        text="Retour",
        manager=manager
    )
    container.append(btn_return)
  #  checkbox_fullscreen = pygame_gui.elements.UICheckBox(
  #      relative_rect=pygame.Rect((mid_width-100, mid_height-250), (30, 30)),  # (x, y), (largeur, hauteur)
  #      text="Plein écran",
  #      manager=manager,
  #  )
  #  checkbox_fullscreen.checked = data.get("fullscreen",False)

def filtrer_entier(input_box):
    texte = input_box.get_text()
    texte_filtre = ''.join(c for c in texte if c.isdigit() or c == '-')
    if '-' in texte_filtre and not texte_filtre.startswith('-'):
        texte_filtre = texte_filtre.replace('-', '')
    if not texte_filtre or texte_filtre == '-':
        texte_filtre = '0'
    input_box.set_text(texte_filtre)
    return int(texte_filtre)

def get_resolution(resolution_data, default="1920x1080"):
    resolution_str = default
    if isinstance(resolution_data, (tuple, list)):
        if len(resolution_data) > 0:
            resolution_str = str(resolution_data[0]).strip("[]()'\" ")
    elif isinstance(resolution_data, str):
        resolution_str = resolution_data.strip("[]()'\" ")

    if "x" in resolution_str:
        parts = resolution_str.split('x')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return resolution_str
    return default

def get_language_info(label):
    for key, value in lg.get().items():
        if value == label:
            return key.split("::")[-1]
    return None

def option_screen(screen, manager, language, change_page, get_page, clock):
    global popup_quit, lg, mid_width, mid_height, container
    container = []
    option_active = True
    lg = language

    data_ = read_json(resource_path("config.json"))
    if data_ is None:
        data_ = {}

    mid_width = screen.get_width() / 2
    mid_height = screen.get_height() / 2

    create_game_screen_init(screen, manager, data_, language)

    while option_active:
        screen.fill((146, 147, 147))
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            manager.process_events(event)

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == volume_slider:
                    data_["volume_son"] = event.value / 100.0

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == input_box_tour_serveur:
                    data_["nb_tour"] = filtrer_entier(input_box_tour_serveur)
                if event.ui_element == input_box_nb_player:
                    data_["nb_player"] = filtrer_entier(input_box_tour_serveur)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btn_return:
                    change_page(Screen.MENU.value)
                    manager.get_root_container().clear()
                if event.ui_element == btn_appliquer:
                    pygame.mixer.music.set_volume(data_["volume_son"])
                    data_["language"] = get_language_info(str(dropdown_langue.selected_option[0]))
                    language.set_language(data_["language"])
                    write_json(resource_path("config.json"), data_)
                    create_game_screen_init(screen, manager, data_, language)

        text_langue.update()
        text_volume.update()
        text_nb_tour.update()
        text_nb_player.update()

        option_active = get_page() == Screen.OPTION.value

        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()