import time
from variables import *

# just to remove sounds
remove_sounds = True

from functions import is_hovering_quit, is_hovering_quit_game, \
    is_hovering_menu_down, is_hovering_start, is_hovering_level, is_hovering_sounds, \
    is_hovering_about, is_hovering_reset, is_hovering_score, reading_scores_from_score_data, \
    is_hovering_time, generate_list_of_coordinates


pygame.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('data/sounds/soundtrack.mp3')
pygame.mixer.music.play(-1)


class Objects_coordinates:
    cord_x_yellow_minion, cord_x_purple_minion, cord_x_green_minion, cord_x_red_minion, cord_x_unicorn, cord_x_banana,\
        cord_y_yellow_minion, cord_y_purple_minion, cord_y_green_minion, cord_y_red_minion, cord_y_unicorn, \
        cord_y_banana = generate_list_of_coordinates()
    cord_out_screen = (-200, -200)


class Game:
    sound_of_collision = pygame.mixer.Sound('data/sounds/sound.wav')
    sound_of_collision.set_volume(0.9)
    sound_of_clicking = pygame.mixer.Sound('data/sounds/click_sound.wav')
    sound_of_clicking.set_volume(0.7)
    volume_adjust = 3
    collision_counter = 0
    sound_of_game_on = True
    font_1 = pygame.font.SysFont('arial', 50, True, False)
    font_2 = pygame.font.SysFont('arial', 42, True, False)
    font_3 = pygame.font.SysFont('arial', 70, True, False)
    font_4 = pygame.font.SysFont('arial', 90, True, False)
    pygame.display.set_caption("Minions game")
    screen = pygame.display.set_mode((1080, 720))
    should_show_tutorial = 1
    entire_game_on = True
    screen_menu_on = True
    screen_tutorial_on = True
    screen_game_on = False
    screen_after_game_on = False
    screen_score_on = False
    screen_about_on = False
    checking_highest_score = True
    flag_for_append_score = True
    score_counter = banana_counter = unicorn_counter = bad_minions_counter = good_minion_counter = 0
    timer = 0
    start = 0
    end = 0
    timer_tutorial = 0
    start_time_tutorial = 0
    end_time_tutorial = 0
    level = 'normal'
    score_to_print = ''
    time_choice = 30
    displacement = 30
    SPAWN_SYMBOL_X = 540
    SPAWN_SYMBOL_Y = 360
    cord_x_symbol = SPAWN_SYMBOL_X
    cord_y_symbol = SPAWN_SYMBOL_Y
    keys = pygame.key.get_pressed()
    score_list = [0]
    the_highest_score = 0
    start_time_tutorial = 0


def process_screen_menu(current_game):
    pygame.time.delay(50)
    current_game.screen.blit(image_menu_screen, (0, 0))
    current_game.screen.blit(image_button_sounds_on_black, (204, 331))
    mouse = pygame.mouse.get_pos()

    if current_game.level == 'normal':
        current_game.screen.blit(image_button_level_normal_black, (539, 212))
    elif current_game.level == 'easy':
        current_game.screen.blit(image_button_level_easy_black, (539, 212))
    elif current_game.level == 'hard':
        current_game.screen.blit(image_button_level_hard_black, (539, 212))

    if current_game.sound_of_game_on:
        current_game.screen.blit(image_button_sounds_on_black, (204, 331))
    else:
        current_game.screen.blit(image_button_sounds_off_black, (204, 331))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_game.screen_menu_on = current_game.entire_game_on = False
    '''START'''
    if is_hovering_start(mouse):
        current_game.screen.blit(image_button_start_white, (204, 212))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.sound_of_clicking.play()
            current_game.screen_menu_on = False
            current_game.score_counter = current_game.timer = 0
            if current_game.should_show_tutorial > 0:
                current_game.start = 0
                current_game.start = time.time()
                current_game.screen_tutorial_on = False
                process_screen_game(current_game)
            else:
                current_game.screen_tutorial_on = True
                current_game.start_time_tutorial = time.time()
                process_screen_tutorial(current_game)
            pygame.time.delay(100)

    '''LEVEL'''
    if is_hovering_level(mouse):
        if current_game.level == 'normal':
            current_game.screen.blit(image_button_level_normal_white, (539, 212))
        elif current_game.level == 'easy':
            current_game.screen.blit(image_button_level_easy_white, (539, 212))
        elif current_game.level == 'hard':
            current_game.screen.blit(image_button_level_hard_white, (539, 212))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.sound_of_clicking.play()
            if current_game.level == 'normal':
                current_game.level = 'hard'
                pygame.time.delay(50)
            elif current_game.level == 'hard':
                current_game.level = 'easy'
                pygame.time.delay(50)
            elif current_game.level == 'easy':
                current_game.level = 'normal'
                pygame.time.delay(50)
    '''SOUNDS'''
    if is_hovering_sounds(mouse):
        if current_game.sound_of_game_on:
            current_game.screen.blit(image_button_sounds_on_white, (204, 331))
        else:
            current_game.screen.blit(image_button_sounds_off_white, (204, 331))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if current_game.volume_adjust % 2 == 0:
                pygame.mixer.music.set_volume(0.1)
                current_game.sound_of_collision.set_volume(0.9)
                current_game.sound_of_clicking.set_volume(0.7)
                current_game.volume_adjust += 1
                pygame.time.delay(200)
                current_game.sound_of_game_on = True
                current_game.sound_of_clicking.play()
            else:
                current_game.sound_of_game_on = False
                pygame.mixer.music.set_volume(0)
                current_game.sound_of_collision.set_volume(0)
                current_game.sound_of_clicking.set_volume(0)
                current_game.volume_adjust += 1
                pygame.time.delay(200)
    '''QUIT'''
    if is_hovering_quit(mouse):
        current_game.screen.blit(image_button_quit_white, (379, 569))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.sound_of_clicking.play()
            pygame.time.delay(100)
            current_game.screen_tutorial_on = current_game.screen_menu_on = current_game.screen_game_on = current_game.screen_after_game_on = current_game.entire_game_on = False
    '''TIME'''
    if is_hovering_time(mouse):
        current_game.screen.blit(image_button_time_white, (539, 331))
        time_choice_to_print = f'{current_game.time_choice}s'
        time_choice_format = current_game.font_3.render(time_choice_to_print, True, (255, 255, 255))
        current_game.screen.blit(time_choice_format, (641, 330))

        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.sound_of_clicking.play()
            pygame.time.delay(200)
            if current_game.time_choice == 60:
                current_game.time_choice = 30
            elif current_game.time_choice == 30:
                current_game.time_choice = 60
    '''SCORE'''
    if is_hovering_score(mouse):
        current_game.screen.blit(image_button_score_white, (539, 450))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.screen_score_on = True
            current_game.sound_of_clicking.play()
            process_screen_score(current_game)
            pygame.time.delay(80)
    '''ABOUT'''
    if is_hovering_about(mouse):
        current_game.screen.blit(image_button_about_white, (204, 450))
        if pygame.mouse.get_pressed() == (1, 0, 0):
            current_game.sound_of_clicking.play()
            pygame.time.delay(40)
            current_game.screen_about_on = True
            process_screen_about(current_game)
    pygame.display.update()
    current_game.checking_highest_score = True
    if remove_sounds:
        pygame.mixer.music.set_volume(0)
        current_game.sound_of_collision.set_volume(0)
        current_game.sound_of_clicking.set_volume(0)


def process_screen_tutorial(current_game):
    while current_game.screen_tutorial_on:
        current_game.screen.blit(image_tutorial_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game.screen_menu_on = current_game.entire_game_on = current_game.screen_tutorial_on = False

        if is_hovering_quit_game(mouse):
            current_game.screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                current_game.screen_tutorial_on = False
                current_game.should_show_tutorial += 1
                current_game.start = 0
                current_game.start = time.time()
                pygame.time.delay(50)
                process_screen_game(current_game)

        current_game.end_time_tutorial = time.time()
        current_game.timer_tutorial = (current_game.end_time_tutorial - current_game.start_time_tutorial)
        timer_tutorial_to_print = f'{(10 - current_game.timer_tutorial):.0f}s'
        timer_tutorial_format = current_game.font_4.render(timer_tutorial_to_print, True, (255, 0, 0))
        current_game.screen.blit(timer_tutorial_format, (675, 600))

        if current_game.timer_tutorial >= 9.5:
            current_game.screen_tutorial_on = False
            current_game.should_show_tutorial += 1
            current_game.start = 0
            current_game.start = time.time()
            process_screen_game(current_game)
        pygame.display.flip()


def process_screen_game(current_game):
    current_game.screen_game_on = True
    while current_game.screen_game_on:
        current_game.screen.blit(image_game_screen, (0, 0))
        pygame.time.delay(40)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game.screen_menu_on = current_game.screen_game_on = current_game.entire_game_on = False
            current_game.keys = pygame.key.get_pressed()

        if is_hovering_quit_game(mouse):
            current_game.screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                current_game.screen_game_on = False
                current_game.screen_after_game_on = True

        if current_game.keys[pygame.K_UP] and current_game.cord_y_symbol >= 120:
            current_game.cord_y_symbol -= current_game.displacement
        if current_game.keys[pygame.K_DOWN] and current_game.cord_y_symbol <= 625:
            current_game.cord_y_symbol += current_game.displacement
        if current_game.keys[pygame.K_RIGHT] and current_game.cord_x_symbol <= 980:
            current_game.cord_x_symbol += current_game.displacement
        if current_game.keys[pygame.K_LEFT] and current_game.cord_x_symbol >= 30:
            current_game.cord_x_symbol -= current_game.displacement

        '''SPAWN OBJECTS'''
        obj_yellow_minion = current_game.screen.blit(image_yellow_minion, (objects_cords.cord_x_yellow_minion, objects_cords.cord_y_yellow_minion))
        obj_symbol = current_game.screen.blit(image_symbol, (current_game.cord_x_symbol, current_game.cord_y_symbol))

        if current_game.level == 'easy':
            obj_unicorn = current_game.screen.blit(image_unicorn,(objects_cords.cord_x_unicorn, objects_cords.cord_y_unicorn))
            obj_banana = current_game.screen.blit(image_banana, (objects_cords.cord_x_banana, objects_cords.cord_y_banana))
            obj_purple_minion = current_game.screen.blit(image_purple_minion, (objects_cords.cord_x_purple_minion, objects_cords.cord_y_purple_minion))
            obj_green_minion = current_game.screen.blit(image_green_minion, objects_cords.cord_out_screen)
            obj_red_minion = current_game.screen.blit(image_red_minion, objects_cords.cord_out_screen)

        elif current_game.level == 'normal':
            obj_purple_minion = current_game.screen.blit(image_purple_minion, (objects_cords.cord_x_purple_minion, objects_cords.cord_y_purple_minion))
            obj_green_minion = current_game.screen.blit(image_green_minion, objects_cords.cord_out_screen)
            obj_red_minion = current_game.screen.blit(image_red_minion, objects_cords.cord_out_screen)

            if current_game.collision_counter != 0 and (current_game.collision_counter % 3 == 0):
                obj_unicorn = current_game.screen.blit(image_unicorn, (objects_cords.cord_x_unicorn, objects_cords.cord_y_unicorn))
            else:
                obj_unicorn = current_game.screen.blit(image_unicorn, objects_cords.cord_out_screen)
            if current_game.collision_counter != 0 and (current_game.collision_counter % 6 == 0):
                obj_banana = current_game.screen.blit(image_banana, (objects_cords.cord_x_banana, objects_cords.cord_y_banana))
            else:
                obj_banana = current_game.screen.blit(image_banana, objects_cords.cord_out_screen)

        elif current_game.level == 'hard':
            obj_green_minion = current_game.screen.blit(image_green_minion, (objects_cords.cord_x_green_minion, objects_cords.cord_y_green_minion))
            obj_red_minion = current_game.screen.blit(image_red_minion, (objects_cords.cord_x_red_minion, objects_cords.cord_y_red_minion))
            obj_purple_minion = current_game.screen.blit(image_purple_minion, (objects_cords.cord_x_purple_minion, objects_cords.cord_y_purple_minion))

            if current_game.collision_counter != 0 and (current_game.collision_counter % 5 == 0):
                obj_unicorn = current_game.screen.blit(image_unicorn, (objects_cords.cord_x_unicorn, objects_cords.cord_y_unicorn))
            else:
                obj_unicorn = current_game.screen.blit(image_unicorn, objects_cords.cord_out_screen)
            if current_game.collision_counter != 0 and (current_game.collision_counter % 10 == 0):
                obj_banana = current_game.screen.blit(image_banana, (objects_cords.cord_x_banana, objects_cords.cord_y_banana))
            else:
                obj_banana = current_game.screen.blit(image_banana, objects_cords.cord_out_screen)

        test_collision_red = True
        if test_collision_red:
            if obj_symbol.colliderect(obj_yellow_minion):
                current_game.collision_counter += 1
                current_game.good_minion_counter += 1
                current_game.score_counter += 5
                current_game.cord_x_symbol = current_game.SPAWN_SYMBOL_X
                current_game.cord_y_symbol = current_game.SPAWN_SYMBOL_Y
                objects_cords.cord_x_yellow_minion, objects_cords.cord_x_purple_minion, objects_cords.cord_x_green_minion, \
                    objects_cords.cord_x_red_minion, objects_cords.cord_x_unicorn, objects_cords.cord_x_banana, \
                    objects_cords.cord_y_yellow_minion, objects_cords.cord_y_purple_minion, objects_cords.cord_y_green_minion,\
                    objects_cords.cord_y_red_minion, objects_cords.cord_y_unicorn, objects_cords.cord_y_banana \
                    = generate_list_of_coordinates()
                current_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_unicorn):
                current_game.collision_counter += 1
                current_game.score_counter += 10
                current_game.unicorn_counter += 1
                current_game.cord_x_symbol = current_game.SPAWN_SYMBOL_X
                current_game.cord_y_symbol = current_game.SPAWN_SYMBOL_Y
                objects_cords.cord_x_yellow_minion, objects_cords.cord_x_purple_minion, objects_cords.cord_x_green_minion, \
                objects_cords.cord_x_red_minion, objects_cords.cord_x_unicorn, objects_cords.cord_x_banana, \
                objects_cords.cord_y_yellow_minion, objects_cords.cord_y_purple_minion, objects_cords.cord_y_green_minion, \
                objects_cords.cord_y_red_minion, objects_cords.cord_y_unicorn, objects_cords.cord_y_banana \
                    = generate_list_of_coordinates()
                current_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_banana):
                current_game.collision_counter += 1
                current_game.score_counter += 20
                current_game.banana_counter += 1
                current_game.cord_x_symbol = current_game.SPAWN_SYMBOL_X
                current_game.cord_y_symbol = current_game.SPAWN_SYMBOL_Y
                objects_cords.cord_x_yellow_minion, objects_cords.cord_x_purple_minion, objects_cords.cord_x_green_minion, \
                objects_cords.cord_x_red_minion, objects_cords.cord_x_unicorn, objects_cords.cord_x_banana, \
                objects_cords.cord_y_yellow_minion, objects_cords.cord_y_purple_minion, objects_cords.cord_y_green_minion, \
                objects_cords.cord_y_red_minion, objects_cords.cord_y_unicorn, objects_cords.cord_y_banana \
                    = generate_list_of_coordinates()
                current_game.sound_of_clicking.play()
                current_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_purple_minion) or obj_symbol.colliderect(obj_green_minion) or obj_symbol.colliderect(obj_red_minion):
                current_game.collision_counter += 1
                current_game.score_counter -= 10
                current_game.bad_minions_counter += 1
                if current_game.score_counter < 0:
                    current_game.score_counter = 0
                current_game.cord_x_symbol = current_game.SPAWN_SYMBOL_X
                current_game.cord_y_symbol = current_game.SPAWN_SYMBOL_Y
                objects_cords.cord_x_yellow_minion, objects_cords.cord_x_purple_minion, objects_cords.cord_x_green_minion, \
                objects_cords.cord_x_red_minion, objects_cords.cord_x_unicorn, objects_cords.cord_x_banana, \
                objects_cords.cord_y_yellow_minion, objects_cords.cord_y_purple_minion, objects_cords.cord_y_green_minion, \
                objects_cords.cord_y_red_minion, objects_cords.cord_y_unicorn, objects_cords.cord_y_banana \
                    = generate_list_of_coordinates()
                current_game.sound_of_collision.play()
                pygame.time.delay(50)

        current_game.end = time.time()
        timer = (current_game.end - current_game.start)
        timer_to_print = f'{(current_game.time_choice - timer):.0f}s'
        current_game.score_to_print = f'{current_game.score_counter}'
        timer_format = current_game.font_3.render(timer_to_print, True, (0, 0, 0))
        score_format = current_game.font_3.render(current_game.score_to_print, True, (0, 0, 0))
        current_game.screen.blit(timer_format, (680, 10))
        current_game.screen.blit(score_format, (260, 10))
        pygame.display.flip()
        current_game.flag_for_append_score = True
        if timer > current_game.time_choice:
            current_game.screen_game_on = False
            current_game.screen_after_game_on = True
    if current_game.screen_after_game_on:
        process_screen_after_game(current_game)


def process_screen_after_game(current_game):
    current_game.screen_after_game_on = True
    while current_game.screen_after_game_on:
        current_game.screen.blit(image_after_game_screen, (0, 0))
        pygame.time.delay(50)
        if current_game.flag_for_append_score:
            current_game.score_list.append(int(current_game.score_counter))
            current_game.flag_for_append_score = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game.screen_menu_on = current_game.screen_after_game_on = current_game.entire_game_on = False
        mouse = pygame.mouse.get_pos()

        if is_hovering_menu_down(mouse):
            current_game.screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                current_game.screen_menu_on = True
                current_game.screen_after_game_on = False
                pygame.time.delay(100)
                pygame.display.flip()

        print_things_after_game_screen()
        pygame.display.flip()
        current_game.checking_highest_score = True


def process_screen_score(current_game):
    while current_game.screen_score_on:
        current_game.screen.blit(image_score_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()

        if current_game.checking_highest_score:
            highest_score_from_list = max(current_game.score_list)
            highest_score_from_score_data = reading_scores_from_score_data()
            if highest_score_from_score_data > highest_score_from_list:
                current_game.the_highest_score = highest_score_from_score_data
                current_game.checking_highest_score = False
            else:
                current_game.the_highest_score = highest_score_from_list
                current_game.checking_highest_score = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game.screen_score_on = current_game.entire_game_on =  False

        if is_hovering_menu_down(mouse):
            current_game.screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                current_game.screen_score_on = False
                pygame.time.delay(50)

        if is_hovering_reset(mouse):
            current_game.screen.blit(image_button_reset_white, (380, 468))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                pygame.time.delay(50)
                current_game.the_highest_score = 0
                with open('score_data.txt', 'w') as score_to_write:
                    for score in current_game.score_list:
                        score_to_write.write(str(score) + '\n')

        highest_score_to_print = f'{current_game.the_highest_score}'
        highest_score_format = current_game.font_4.render(highest_score_to_print, True, (255, 255, 255))
        current_game.screen.blit(highest_score_format, (470, 310))
        pygame.display.flip()


def process_screen_about(current_game):
    while current_game.screen_about_on:
        current_game.screen.blit(image_about_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_game.screen_about_on = current_game.screen_menu_on = current_game.screen_after_game_on = False
        if is_hovering_menu_down(mouse):
            current_game.screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                current_game.sound_of_clicking.play()
                current_game.screen_menu_on = True
                current_game.screen_game_on = current_game.screen_after_game_on = current_game.screen_score_on = current_game.screen_about_on = False
                pygame.time.delay(50)
        pygame.display.flip()


def write_score_in_score_data_txt():
    with open('score_data.txt', 'a') as score_to_write:
        for score in current_game.score_list:
            if score != 0:
                score_to_write.write(str(score) + '\n')


def print_things_after_game_screen():
    unicorn_to_print = f'{current_game.unicorn_counter}'
    bad_minions_to_print = f'{current_game.bad_minions_counter}'
    good_minion_to_print = f'{current_game.good_minion_counter}'
    banana_to_print = f'{current_game.banana_counter}'

    unicorn_format = current_game.font_1.render(unicorn_to_print, True, (0, 0, 0))
    bad_minions_format = current_game.font_1.render(bad_minions_to_print, True, (0, 0, 0))
    good_minion_format = current_game.font_1.render(good_minion_to_print, True, (0, 0, 0))
    banana_format = current_game.font_1.render(banana_to_print, True, (0, 0, 0))
    score_format = current_game.font_4.render(current_game.score_to_print, True, (255, 255, 255))

    current_game.screen.blit(good_minion_format, (267, 250))
    current_game.screen.blit(unicorn_format, (420, 250))
    current_game.screen.blit(banana_format, (565, 250))
    current_game.screen.blit(bad_minions_format, (730, 250))
    current_game.screen.blit(score_format, (625, 345))


current_game = Game()
objects_cords = Objects_coordinates()
while current_game.entire_game_on:
    process_screen_menu(current_game)
write_score_in_score_data_txt()
pygame.quit()
