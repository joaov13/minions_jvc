import random
from images import *
from main import pygame


# coord_x = [160, 340, 520, 700, 880]
# coord_y = [104, 228, 352, 476]
def generate_spawn_coordinates_for_dodge_mode():
    coord_x = [40, 160, 340, 700, 880, 1000]
    coord_1 = random.choice(coord_x)
    coord_2 = random.choice(coord_x)
    while coord_2 == coord_1:
        coord_2 = random.choice(coord_x)
    coord_3 = random.choice(coord_x)
    while coord_3 == coord_1 or coord_3 == coord_2:
        coord_3 = random.choice(coord_x)
    return coord_1, coord_2, coord_3


def generate_random_coordinates():
    """ Generates random x and y inside the screen and NOT in the center region """
    pos_x = (random.randint(6, 99))
    # does not spawn in the center region of the screen
    while 48 < pos_x < 62:
        pos_x = (random.randint(6, 99))

    pos_y = (random.randint(15, 65))
    # does not spawn in the center region of the screen
    while 27 < pos_y < 46:
        pos_y = (random.randint(15, 65))

    return pos_x * 10, pos_y * 10


def generate_just_coordinate_x():
    pos_x = (random.randint(10, 98))
    while 48 < pos_x < 62:
        pos_x = (random.randint(10, 98))
    return pos_x * 10


def generate_just_coordinate_y():
    pos_y = (random.randint(17, 60))
    while 27 < pos_y < 46:
        pos_y = (random.randint(17, 60))
    return pos_y * 10


def generate_list_of_coordinates():
    list_x = []
    for x in range(20):
        cord = generate_just_coordinate_x()
        if cord not in list_x:
            list_x.append(cord)
    list_y = []
    for x in range(20):
        cord = generate_just_coordinate_y()
        if cord not in list_y:
            list_y.append(cord)
    return list_x[0], list_x[1], list_x[2], list_x[3], list_x[4], list_x[5], list_y[0], list_y[1], list_y[2], list_y[3], \
        list_y[4], list_y[5]


def change_all_objects_coordinates(current_coordinates):
    current_coordinates.cord_x_2x = generate_just_coordinate_x()
    current_coordinates.cord_y_2x = generate_just_coordinate_y()
    current_coordinates.cord_x_potion = generate_just_coordinate_x()
    current_coordinates.cord_y_potion = generate_just_coordinate_y()
    current_coordinates.cord_x_clock = generate_just_coordinate_x()
    current_coordinates.cord_y_clock = generate_just_coordinate_y()
    current_coordinates.cord_x_symbol = current_coordinates.SPAWN_SYMBOL_X
    current_coordinates.cord_y_symbol = current_coordinates.SPAWN_SYMBOL_Y
    current_coordinates.cord_x_yellow_minion, current_coordinates.cord_x_purple_minion, \
        current_coordinates.cord_x_green_minion, current_coordinates.cord_x_red_minion, \
        current_coordinates.cord_x_unicorn, current_coordinates.cord_x_banana, \
        current_coordinates.cord_y_yellow_minion, current_coordinates.cord_y_purple_minion, \
        current_coordinates.cord_y_green_minion, current_coordinates.cord_y_red_minion, \
        current_coordinates.cord_y_unicorn, current_coordinates.cord_y_banana \
        = generate_list_of_coordinates()


def set_minions_coordinates_for_dodge_mode(info_game):
    info_game.current_coordinates.cord_x_green_minion, info_game.current_coordinates.cord_x_red_minion, \
        info_game.current_coordinates.cord_x_purple_minion = generate_spawn_coordinates_for_dodge_mode()
    info_game.current_coordinates.cord_y_green_minion = info_game.current_coordinates.cord_y_red_minion = \
        info_game.current_coordinates.cord_y_purple_minion = 98


def change_displacement_of_minions(info_game):
    info_game.current_coordinates.red_minion_displacement = random.choice(
        info_game.current_coordinates.list_displacement)
    info_game.current_coordinates.purple_minion_displacement = random.choice(
        info_game.current_coordinates.list_displacement)
    info_game.current_coordinates.green_minion_displacement = random.choice(
        info_game.current_coordinates.list_displacement)


def move_minions_in_dodge_mode(info_game):
    """RED"""
    if info_game.current_coordinates.where_move_red_minion == 'down':
        info_game.current_coordinates.cord_y_red_minion += info_game.current_coordinates.red_minion_displacement
        if info_game.current_coordinates.cord_y_red_minion >= 660:
            info_game.current_coordinates.where_move_red_minion = 'up'
    if info_game.current_coordinates.where_move_red_minion == 'up':
        info_game.current_coordinates.cord_y_red_minion -= info_game.current_coordinates.red_minion_displacement
        if info_game.current_coordinates.cord_y_red_minion <= 96:
            info_game.current_coordinates.where_move_red_minion = 'down'
    '''PURPLE'''
    if info_game.current_coordinates.where_move_purple_minion == 'down':
        info_game.current_coordinates.cord_y_purple_minion += info_game.current_coordinates.purple_minion_displacement
        if info_game.current_coordinates.cord_y_purple_minion >= 660:
            info_game.current_coordinates.where_move_purple_minion = 'up'
    if info_game.current_coordinates.where_move_purple_minion == 'up':
        info_game.current_coordinates.cord_y_purple_minion -= info_game.current_coordinates.purple_minion_displacement
        if info_game.current_coordinates.cord_y_purple_minion <= 96:
            info_game.current_coordinates.where_move_purple_minion = 'down'
    '''GREEN'''
    if info_game.current_coordinates.where_move_green_minion == 'down':
        info_game.current_coordinates.cord_y_green_minion += info_game.current_coordinates.green_minion_displacement
        if info_game.current_coordinates.cord_y_green_minion >= 660:
            info_game.current_coordinates.where_move_green_minion = 'up'
    if info_game.current_coordinates.where_move_green_minion == 'up':
        info_game.current_coordinates.cord_y_green_minion -= info_game.current_coordinates.green_minion_displacement
        if info_game.current_coordinates.cord_y_green_minion <= 96:
            info_game.current_coordinates.where_move_green_minion = 'down'


def set_bad_minions_on_corners(info_game):
    coordinates = [[0, 98], [1000, 98], [0, 640]]
    if info_game.current_settings.level_choice == 'easy':
        info_game.current_coordinates.cord_x_purple_minion = coordinates[1][0]
        info_game.current_coordinates.cord_y_purple_minion = coordinates[1][1]
    elif info_game.current_settings.level_choice == 'normal':
        info_game.current_coordinates.cord_x_purple_minion = coordinates[1][0]
        info_game.current_coordinates.cord_y_purple_minion = coordinates[1][1]
    elif info_game.current_settings.level_choice == 'hard':
        info_game.current_coordinates.cord_x_purple_minion = coordinates[1][0]
        info_game.current_coordinates.cord_y_purple_minion = coordinates[1][1]
        info_game.current_coordinates.cord_x_green_minion = coordinates[0][0]
        info_game.current_coordinates.cord_y_green_minion = coordinates[0][1]
        info_game.current_coordinates.cord_x_red_minion = coordinates[2][0]
        info_game.current_coordinates.cord_y_red_minion = coordinates[2][1]

class Settings:
    level_choice = 'normal'
    character_choice = 'agnes'
    mouse_hovering_character = ''
    time_choice = 30
    mouse_hovering_level = ''
    timer_classic = 0
    start_timer_classic = 0
    end_timer_classic = 0
    timer = 0
    score_to_print = ''
    score_to_print = ''
    game_mode_choice = 'classic'
    clock_additional_time = 0
    potion_effect = 0


class Game:
    def __init__(self, ):
        pygame.mixer.music.load('data/sounds/soundtrack.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.sound_of_clicking = pygame.mixer.Sound('data/sounds/click_sound.wav')
        self.sound_of_clicking.set_volume(0.7)
        self.sound_of_collision = pygame.mixer.Sound('data/sounds/sound.wav')
        self.sound_of_collision.set_volume(0.9)
        self.show_first_screen = True
        self.show_game_mode_screen = False
        self.show_settings_screen = False
        self.show_classic_game_screen = False
        self.show_after_game_screen = False
        self.show_score_screen = False
        self.show_about_screen = False
        self.show_dodge_game_screen = False
        self.show_modern_game_screen = False
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("MINIONS GAME")
        self.keys = pygame.key.get_pressed()
        self.collision_counter = self.score_counter = self.banana_counter = self.unicorn_counter = \
            self.bad_minions_counter = self.good_minion_counter = 0
        self.font_1 = pygame.font.SysFont('arial', 50, True, False)
        self.font_2 = pygame.font.SysFont('arial', 42, True, False)
        self.font_3 = pygame.font.SysFont('arial', 70, True, False)
        self.font_4 = pygame.font.SysFont('arial', 90, True, False)
        self.flag_for_append_score = True
        self.checking_highest_score = True
        self.score_list = []
        self.the_highest_score = 0
        self.current_settings = Settings()
        self.current_coordinates = ObjectsCoordinates()
        self.sound_of_game_on = True
        self.on_2x = False
        self.counter_2x = 0
        self.print_2x_on_screen = False
        self.appear_2x_on_game = True
        self.set_clock = True
        self.spawn_clock = False
        self.appear_potion = False
        self.set_potion = False


class ObjectsCoordinates:
    list_displacement = [1.5, 2, 3, 4, 5]
    red_minion_displacement = 1
    green_minion_displacement = 1
    purple_minion_displacement = 1
    where_move_red_minion = 'down'
    where_move_green_minion = 'down'
    where_move_purple_minion = 'down'
    displacement = 5
    SPAWN_SYMBOL_X = 540
    SPAWN_SYMBOL_Y = 360
    cord_x_symbol = SPAWN_SYMBOL_X
    cord_y_symbol = SPAWN_SYMBOL_Y

    cord_x_yellow_minion, cord_x_purple_minion, cord_x_green_minion, cord_x_red_minion, cord_x_unicorn, cord_x_banana, \
        cord_y_yellow_minion, cord_y_purple_minion, cord_y_green_minion, cord_y_red_minion, cord_y_unicorn, \
        cord_y_banana = generate_list_of_coordinates()
    cord_out_screen = (-300, -300)
    cord_x_2x = generate_just_coordinate_x()
    cord_y_2x = generate_just_coordinate_y()
    cord_x_potion = generate_just_coordinate_x()
    cord_y_potion = generate_just_coordinate_y()
    cord_x_clock = generate_just_coordinate_x()
    cord_y_clock = generate_just_coordinate_y()


def set_character(mouse, info_game):
    if (160 + 125 > mouse[0] > 160) and (220 + 75 > mouse[1] > 220):
        info_game.screen.blit(image_margo_white, (152, 212))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.character_choice = 'margo'
    elif (160 + 115 > mouse[0] > 160) and (320 + 95 > mouse[1] > 320):
        info_game.screen.blit(image_agnes_white, (173, 315))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.character_choice = 'agnes'
    elif (160 + 120 > mouse[0] > 160) and (420 + 100 > mouse[1] > 420):
        info_game.screen.blit(image_judith_white, (154, 429))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.character_choice = 'judith'
    if info_game.current_settings.character_choice == 'margo':
        info_game.screen.blit(image_choosing_arrow, (80, 235))
    elif info_game.current_settings.character_choice == 'agnes':
        info_game.screen.blit(image_choosing_arrow, (80, 353))
    elif info_game.current_settings.character_choice == 'judith':
        info_game.screen.blit(image_choosing_arrow, (80, 450))


def set_level(mouse, info_game):
    if (453 + 215 > mouse[0] > 453) and (214 + 62 > mouse[1] > 214):
        info_game.screen.blit(image_button_easy_white, (405, 200))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.level_choice = 'easy'
    elif (453 + 215 > mouse[0] > 453) and (297 + 62 > mouse[1] > 297):
        info_game.screen.blit(image_button_normal_white, (405, 283))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.level_choice = 'normal'
    elif (453 + 215 > mouse[0] > 453) and (381 + 62 > mouse[1] > 378):
        info_game.screen.blit(image_button_hard_white, (405, 366))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.level_choice = 'hard'
    if info_game.current_settings.level_choice == 'easy':
        info_game.screen.blit(image_choosing_arrow, (370, 230))
    elif info_game.current_settings.level_choice == 'normal':
        info_game.screen.blit(image_choosing_arrow, (370, 308))
    elif info_game.current_settings.level_choice == 'hard':
        info_game.screen.blit(image_choosing_arrow, (370, 392))


def set_time(mouse, info_game):
    if (783 + 215 > mouse[0] > 783) and (214 + 62 > mouse[1] > 214):
        info_game.screen.blit(image_button_30s, (735, 200))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.time_choice = 30
    elif (783 + 215 > mouse[0] > 783) and (297 + 62 > mouse[1] > 297):
        info_game.screen.blit(image_button_45s, (735, 283))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.time_choice = 45
    elif (783 + 215 > mouse[0] > 783) and (381 + 62 > mouse[1] > 381):
        info_game.screen.blit(image_button_60s, (735, 366))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            info_game.current_settings.time_choice = 60
    if info_game.current_settings.time_choice == 30:
        info_game.screen.blit(image_choosing_arrow, (700, 230))
    elif info_game.current_settings.time_choice == 45:
        info_game.screen.blit(image_choosing_arrow, (700, 308))
    elif info_game.current_settings.time_choice == 60:
        info_game.screen.blit(image_choosing_arrow, (700, 392))


def spawn_obj_character(info_game):
    if info_game.current_settings.character_choice == 'agnes':
        if info_game.current_settings.potion_effect == 1:
            obj_character = info_game.screen.blit(image_small_agnes_obj, ( info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
        else:
            obj_character = info_game.screen.blit(image_agnes_obj, (info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
    elif info_game.current_settings.character_choice == 'margo':
        if info_game.current_settings.potion_effect == 1:
            obj_character = info_game.screen.blit(image_small_margo_obj, (info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
        else:
            obj_character = info_game.screen.blit(image_margo_obj, (info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
    elif info_game.current_settings.character_choice == 'judith':
        if info_game.current_settings.potion_effect == 1:
            obj_character = info_game.screen.blit(image_small_judith_obj, (info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
        else:
            obj_character = info_game.screen.blit(image_judith_obj, (info_game.current_coordinates.cord_x_symbol, info_game.current_coordinates.cord_y_symbol))
    return obj_character


def spawn_2x(info_game):
    obj_2x = info_game.screen.blit(image_2x, info_game.current_coordinates.cord_out_screen)
    if info_game.current_settings.level_choice == 'easy' and info_game.appear_2x_on_game:
        if info_game.score_counter % 50 == 0 and info_game.score_counter > 0:
            obj_2x = info_game.screen.blit(image_2x, (info_game.current_coordinates.cord_x_2x, info_game.current_coordinates.cord_y_2x))
    elif info_game.current_settings.level_choice == 'normal' and info_game.appear_2x_on_game:
        if info_game.score_counter % 100 == 0 and info_game.score_counter > 0:
            obj_2x = info_game.screen.blit(image_2x, (info_game.current_coordinates.cord_x_2x, info_game.current_coordinates.cord_y_2x))
    elif info_game.current_settings.level_choice == 'hard' and info_game.appear_2x_on_game:
        if info_game.score_counter % 150 == 0 and info_game.score_counter > 0:
            obj_2x = info_game.screen.blit(image_2x, (info_game.current_coordinates.cord_x_2x, info_game.current_coordinates.cord_y_2x))
    else:
        obj_2x = info_game.screen.blit(image_2x, info_game.current_coordinates.cord_out_screen)
    return obj_2x


def setting_clock(info_game):
    if 50 < info_game.score_counter < 100:
        x = random.randrange(30)
        if x % 2:
            info_game.set_clock = False
            info_game.spawn_clock = True
            if info_game.current_settings.level_choice == 'easy':
                info_game.current_settings.clock_additional_time = 10
            elif info_game.current_settings.level_choice == 'normal':
                info_game.current_settings.clock_additional_time = 10
            elif info_game.current_settings.level_choice == 'hard':
                info_game.current_settings.clock_additional_time = 5


def setting_potion(info_game):
    '''1 = character, 2 = yellow_minion, 3 = bad_minions, 4 = speed character'''
    if info_game.set_potion:
        x = [1, 2, 3, 4]
        info_game.current_settings.potion_effect = random.choice(x)
        info_game.set_potion = False

    obj_potion = info_game.screen.blit(image_potion, info_game.current_coordinates.cord_out_screen)
    if info_game.appear_potion:
        obj_potion = info_game.screen.blit(image_potion, (info_game.current_coordinates.cord_x_potion, info_game.current_coordinates.cord_y_potion))
    return obj_potion


def print_things_after_game_screen(info_game):
    unicorn_to_print = f'{info_game.unicorn_counter}'
    bad_minions_to_print = f'{info_game.bad_minions_counter}'
    good_minion_to_print = f'{info_game.good_minion_counter}'
    banana_to_print = f'{info_game.banana_counter}'

    unicorn_format = info_game.font_1.render(unicorn_to_print, True, (0, 0, 0))
    bad_minions_format = info_game.font_1.render(bad_minions_to_print, True, (0, 0, 0))
    good_minion_format = info_game.font_1.render(good_minion_to_print, True, (0, 0, 0))
    banana_format = info_game.font_1.render(banana_to_print, True, (0, 0, 0))
    score_format = info_game.font_4.render(info_game.current_settings.score_to_print, True, (255, 255, 255))

    info_game.screen.blit(good_minion_format, (267, 250))
    info_game.screen.blit(unicorn_format, (420, 250))
    info_game.screen.blit(banana_format, (565, 250))
    info_game.screen.blit(bad_minions_format, (730, 250))
    info_game.screen.blit(score_format, (625, 345))


def set_to_zero_counters(info_game):
    info_game.current_settings.start_timer_classic = 0
    info_game.collision_counter = info_game.score_counter = info_game.banana_counter = info_game.unicorn_counter = \
        info_game.bad_minions_counter = info_game.good_minion_counter = 0


def change_volume(info_game, mouse):
    pressed = False
    if (386 + 312 > mouse[0] > 386) and (282 + 92 > mouse[1] > 282) and info_game.sound_of_game_on:
        info_game.screen.blit(image_button_new_sound_on_white, (384, 282))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pressed = True
    elif (386 + 312 > mouse[0] > 386) and (282 + 92 > mouse[1] > 282) and info_game.sound_of_game_on == False:
        info_game.screen.blit(image_button_new_sound_off_white, (384, 282))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pressed = True
    if (pressed == True) and info_game.sound_of_game_on:
        info_game.sound_of_clicking.play()
        info_game.sound_of_game_on = False
        pygame.mixer.music.set_volume(0)
        info_game.sound_of_collision.set_volume(0)
        info_game.sound_of_clicking.set_volume(0)
        pygame.time.delay(200)
    elif (pressed == True) and info_game.sound_of_game_on == False:
        info_game.sound_of_game_on = True
        pygame.mixer.music.set_volume(0.1)
        info_game.sound_of_collision.set_volume(0.9)
        info_game.sound_of_clicking.set_volume(0.7)
        info_game.sound_of_clicking.play()
        pygame.time.delay(200)


def write_scores_to_file(info_game):
    with open('score_data.txt', 'a') as score_to_write:
        for score in info_game.score_list:
            if score != 0:
                score_to_write.write(str(score) + '\n')


def reset_scores(info_game):
    info_game.the_highest_score = 0
    info_game.score_list = []
    with open('score_data.txt', 'w') as score_to_write:
        score_to_write.write('')


def checking_highest_score(info_game):
    read_scores = []
    highest_score_from_score_data = 0

    '''Find the highest value from score_list'''
    if not info_game.score_list:
        highest_score_from_list = 0
    else:
        highest_score_from_list = max(info_game.score_list)
    ''''Find the highest value from score_data.txt'''
    with open('score_data.txt', 'r') as score_to_read:
        for score in score_to_read:
            if score != '\n':
                read_scores.append(int(score))
    for scores in read_scores:
        if (highest_score_from_score_data == 0) or (scores > highest_score_from_score_data):
            highest_score_from_score_data = scores
    '''Set the highest value in the_highest_score'''
    if highest_score_from_score_data > highest_score_from_list:
        the_highest_score = highest_score_from_score_data
    elif highest_score_from_list > highest_score_from_score_data:
        the_highest_score = highest_score_from_list
    else:
        the_highest_score = 0
    return the_highest_score

def is_hovering_play_first_screen(mouse):
    return (384 + 312 > mouse[0] > 383) and (170 + 92 > mouse[1] > 170)


def is_hovering_quit_first_screen(mouse):
    return (386 + 312 > mouse[0] > 386) and (618 + 92 > mouse[1] > 618)


def is_hovering_score_first_screen(mouse):
    return (384 + 312 > mouse[0] > 383) and (394 + 92 > mouse[1] > 394)


def is_hovering_about_first_screen(mouse):
    return (386 + 312 > mouse[0] > 386) and (506 + 92 > mouse[1] > 506)


def is_hovering_play_in_game_mode(mouse):
    return (735 + 312 > mouse[0] > 735) and (619 + 92 > mouse[1] > 619)


def is_hovering_menu_in_game_mode(mouse):
    return (74 + 312 > mouse[0] > 74) and (619 + 92 > mouse[1] > 619)


def is_hovering_menu_in_score(mouse):
    return (383 + 312 > mouse[0] > 383) and (614 + 92 > mouse[1] > 614)


def is_hovering_menu_in_about(mouse):
    return (383 + 312 > mouse[0] > 383) and (614 + 92 > mouse[1] > 614)


def is_hovering_reset_in_score(mouse):
    return (383 + 312 > mouse[0] > 383) and (421 + 92 > mouse[1] > 421)


def is_hovering_play_in_settings_screen(mouse):
    return (735 + 312 > mouse[0] > 735) and (619 + 92 > mouse[1] > 619)


def is_hovering_menu_in_settings_screen(mouse):
    return (74 + 312 > mouse[0] > 74) and (619 + 92 > mouse[1] > 619)


def is_hovering_classic(mouse):
    return (131 + 312 > mouse[0] > 131) and (290 + 92 > mouse[1] > 290)


def is_hovering_dodge(mouse):
    return (131 + 312 > mouse[0] > 131) and (390 + 92 > mouse[1] > 390)


def is_hovering_modern(mouse):
    return (131 + 312 > mouse[0] > 131) and (490 + 92 > mouse[1] > 490)


def is_hovering_up_quit_in_game(mouse):
    return (911 + 145 > mouse[0] > 911) and (30 + 36 > mouse[1] > 30)


def is_hovering_menu_after_game(mouse):
    return (380 + 300 > mouse[0] > 380) and (553 + 75 > mouse[1] > 553)