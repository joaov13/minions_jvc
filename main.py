import pygame
import random
import time


def reset_pos_balls():
    x_yellow, y_yellow = generate_random_coordinates()
    x_purple, y_purple = generate_random_coordinates()
    x_green, y_green = generate_random_coordinates()
    x_red, y_red = generate_random_coordinates()
    x_symbol = SPAWN_SYMBOL_X
    y_symbol = SPAWN_SYMBOL_Y
    return x_yellow, y_yellow, x_purple, y_purple, x_green, y_green, x_red, y_red, x_symbol, y_symbol


def generate_random_coordinates():
    return random.choice(POS_X), random.choice(POS_Y)


def change_pos(ball_image):
    y_for_ball = (random.choice(POS_Y))
    x_for_ball = (random.choice(POS_X))
    draw_ball = screen.blit(ball_image, (x_for_ball, y_for_ball))
    return draw_ball, y_for_ball, x_for_ball


def is_hovering_quit(mouse):
    return (620 + 300 > mouse[0] > 620) and (375 + 75 > mouse[1] > 375)


def is_hovering_quit_game(mouse):
    return (911 + 145 > mouse[0] > 912) and (30 + 36 > mouse[1] > 30)


def is_hovering_quit_after_game(mouse):
    return (380 + 300 > mouse[0] > 380) and (638 + 75 > mouse[1] > 638)


def is_hovering_menu_after_game(mouse):
    return (380 + 300 > mouse[0] > 380) and (553 + 75 > mouse[1] > 553)


def is_hovering_start(mouse):
    return (160 + 300 > mouse[0] > 160) and (250 + 75 > mouse[1] > 250)


def is_hovering_level(mouse):
    return (620 + 300 > mouse[0] > 620) and (250 + 75 > mouse[1] > 250)


def is_hovering_sounds(mouse):
    return (160 + 300 > mouse[0] > 160) and (375 + 75 > mouse[1] > 375)


pygame.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('data/sounds/soundtrack.mp3')
pygame.mixer.music.play(-1)
sound_of_collision = pygame.mixer.Sound('data/sounds/sound.wav')
sound_of_collision.set_volume(0.9)
sound_of_clicking = pygame.mixer.Sound('data/sounds/click_sound.wav')
sound_of_clicking.set_volume(0.7)
font_1 = pygame.font.SysFont('arial', 50, True, False)
font_2 = pygame.font.SysFont('arial', 42, True, False)
font_3 = pygame.font.SysFont('arial', 70, True, False)
font_4 = pygame.font.SysFont('arial', 90, True, False)
pygame.display.set_caption("Minions game")
screen = pygame.display.set_mode((1080, 720))
# COLOCAR TODAS AS IMAGENS ABAIXO EM FUNÇÃO USANDO DICIONÁRIO
image_menu_screen = pygame.image.load('data/screen_images/menu_screen.png')
image_game_screen = pygame.image.load('data/screen_images/game_screen.png')
image_after_game_screen = pygame.image.load('data/screen_images/screen_after_game.png')
image_yellow_minion = pygame.image.load('data/balls/yellow.png')
image_unicorn = pygame.image.load('data/balls/unicorn.png')
image_banana = pygame.image.load('data/balls/banana.png')
image_purple_minion = pygame.image.load('data/balls/purple.png')
image_green_minion = pygame.image.load('data/balls/green.png')
image_red_minion = pygame.image.load('data/balls/red.png')
image_symbol = pygame.image.load('data/balls/black.png')
image_button_start_white = pygame.image.load('data/buttons/start_white.png')
image_button_start_black = pygame.image.load('data/buttons/start_black.png')
image_button_quit_white = pygame.image.load('data/buttons/quit_white.png')
image_button_quit_black = pygame.image.load('data/buttons/quit_black.png')
image_button_quit_2_white = pygame.image.load('data/buttons/quit2_white.png')
image_button_level_easy_white = pygame.image.load('data/buttons/level_easy_white.png')
image_button_level_easy_black = pygame.image.load('data/buttons/level_easy_black.png')
image_button_level_normal_white = pygame.image.load('data/buttons/level_normal_white.png')
image_button_level_normal_black = pygame.image.load('data/buttons/level_normal_black.png')
image_button_level_hard_white = pygame.image.load('data/buttons/level_hard_white.png')
image_button_level_hard_black = pygame.image.load('data/buttons/level_hard_black.png')
image_button_sounds_on_white = pygame.image.load('data/buttons/sounds_on_white.png')
image_button_sounds_on_black = pygame.image.load('data/buttons/sounds_on_black.png')
image_button_sounds_off_white = pygame.image.load('data/buttons/sounds_off_white.png')
image_button_sounds_off_black = pygame.image.load('data/buttons/sounds_off_black.png')
image_button_menu_white = pygame.image.load('data/buttons/menu_white.png')
# ###
volume_adjust = 3
sound_of_game_on = True
SPAWN_SYMBOL_X = 540
SPAWN_SYMBOL_Y = 360
cord_x_symbol = SPAWN_SYMBOL_X
cord_y_symbol = SPAWN_SYMBOL_Y
displacement = 35
level = 1
POS_X = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
         280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 620,
         630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840,
         850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
POS_Y = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 460, 470, 480, 490, 500, 510, 520, 530, 540,
         550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650]
cord_out_screen = (-200, -200)
cord_x_yellow_minion, cord_y_yellow_minion = generate_random_coordinates()
cord_x_purple_minion, cord_y_purple_minion = generate_random_coordinates()
cord_x_green_minion, cord_y_green_minion = generate_random_coordinates()
cord_x_red_minion, cord_y_red_minion = generate_random_coordinates()
cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = -200
break_unicorn_to_appear = 2
break_banana_to_appear = 4
collision_counter = 0
entire_game_on = True

while entire_game_on:
    screen_menu_on = True
    screen_game_on = True
    screen_after_game_on = True
    while screen_menu_on:
        pygame.time.delay(50)
        screen.blit(image_menu_screen, (0, 0))
        screen.blit(image_button_start_black, (160, 250))
        screen.blit(image_button_quit_black, (620, 375))
        score_counter = banana_counter = unicorn_counter = bad_minions_counter = good_minion_counter = 0
        help_easy_level = True
        if level == 1:
            screen.blit(image_button_level_normal_black, (620, 250))
        elif level == 0:
            screen.blit(image_button_level_easy_black, (620, 250))
        elif level == 2:
            screen.blit(image_button_level_hard_black, (620, 250))

        screen.blit(image_button_sounds_on_black, (160, 375))
        if sound_of_game_on:
            screen.blit(image_button_sounds_on_black, (160, 375))
        else:
            screen.blit(image_button_sounds_off_black, (160, 375))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False
            keys = pygame.key.get_pressed()

        mouse = pygame.mouse.get_pos()

        if is_hovering_start(mouse):
            screen.blit(image_button_start_white, (160, 250))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = False
                score_counter = timer = 0
                start = 0
                start = time.time()

        if is_hovering_level(mouse):
            if level == 1:
                screen.blit(image_button_level_normal_white, (620, 250))
            elif level == 0:
                screen.blit(image_button_level_easy_white, (620, 250))
            elif level == 2:
                screen.blit(image_button_level_hard_white, (620, 250))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                if level == 1:
                    level = 2
                    pygame.time.delay(150)
                elif level == 2:
                    level = 0
                    pygame.time.delay(150)
                elif level == 0:
                    level = 1
                    pygame.time.delay(150)

        if is_hovering_sounds(mouse):
            if sound_of_game_on:
                screen.blit(image_button_sounds_on_white, (160, 375))
            else:
                screen.blit(image_button_sounds_off_white, (160, 375))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                if volume_adjust % 2 == 0:
                    pygame.mixer.music.set_volume(0.2)
                    sound_of_collision.set_volume(0.9)
                    sound_of_clicking.set_volume(0.7)
                    volume_adjust += 1
                    pygame.time.delay(150)
                    sound_of_game_on = True
                    sound_of_clicking.play()
                else:
                    sound_of_clicking.play()
                    sound_of_game_on = False
                    pygame.mixer.music.set_volume(0)
                    sound_of_collision.set_volume(0)
                    sound_of_clicking.set_volume(0)
                    volume_adjust += 1
                    pygame.time.delay(150)

        if is_hovering_quit(mouse):
            screen.blit(image_button_quit_white, (620, 375))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False

        pygame.display.update()
    while screen_game_on:
        screen.blit(image_game_screen, (0, 0))
        pygame.time.delay(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False
            keys = pygame.key.get_pressed()

        if is_hovering_quit_game(mouse):
            screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_game_on = False
        mouse = pygame.mouse.get_pos()
        if keys[pygame.K_UP] and cord_y_symbol >= 120:
            cord_y_symbol -= displacement
        if keys[pygame.K_DOWN] and cord_y_symbol <= 625:
            cord_y_symbol += displacement
        if keys[pygame.K_RIGHT] and cord_x_symbol <= 980:
            cord_x_symbol += displacement
        if keys[pygame.K_LEFT] and cord_x_symbol >= 30:
            cord_x_symbol -= displacement

        if level == 0:
            break_banana_to_appear = 10
            break_unicorn_to_appear = 10
            obj_green_minion = screen.blit(image_green_minion, cord_out_screen)
            obj_red_minion = screen.blit(image_red_minion, cord_out_screen)
            obj_purple_minion = screen.blit(image_purple_minion, cord_out_screen)

            if help_easy_level:
                obj_unicorn, cord_y_unicorn, cord_x_unicorn = change_pos(image_unicorn)
                obj_banana, cord_y_banana, cord_x_banana = change_pos(image_banana)
                help_easy_level = False

        elif level == 1:
            obj_green_minion = screen.blit(image_green_minion, cord_out_screen)
            obj_red_minion = screen.blit(image_red_minion, cord_out_screen)
            obj_purple_minion = screen.blit(image_purple_minion, (cord_x_purple_minion, cord_y_purple_minion))
            obj_unicorn = screen.blit(image_unicorn, (cord_x_unicorn, cord_y_unicorn))
            obj_banana = screen.blit(image_banana, (cord_x_banana, cord_y_banana))
        elif level == 2:
            obj_green_minion = screen.blit(image_green_minion, (cord_x_green_minion, cord_y_green_minion))
            obj_red_minion = screen.blit(image_red_minion, (cord_x_red_minion, cord_y_red_minion))
            obj_purple_minion = screen.blit(image_purple_minion, (cord_x_purple_minion, cord_y_purple_minion))
            # PROBLEMA COM SPAWN obj_banana e obj_unicorn NO LEVE HARD
            # obj_unicorn = screen.blit(image_unicorn, cord_out_screen)
            # obj_banana = screen.blit(image_banana, cord_out_screen)
            break_banana_to_appear = 8
            break_unicorn_to_appear = 4

        obj_yellow_minion = screen.blit(image_yellow_minion, (cord_x_yellow_minion, cord_y_yellow_minion))
        obj_symbol = screen.blit(image_symbol, (cord_x_symbol, cord_y_symbol))

        test_collision_spawn = True
        if test_collision_spawn:
            if obj_purple_minion.colliderect(obj_yellow_minion):
                obj_purple_minion, cord_y_purple_minion, cord_x_purple_minion = change_pos(image_purple_minion)

            if obj_green_minion.colliderect(obj_yellow_minion) or obj_green_minion.colliderect(obj_red_minion):
                obj_green_minion, cord_y_green_minion, cord_x_green_minion = change_pos(image_green_minion)

            if obj_red_minion.colliderect(obj_yellow_minion):
                obj_red_minion, cord_y_red_minion, cord_x_red_minion = change_pos(image_red_minion)

            if obj_purple_minion.colliderect(obj_unicorn) or obj_purple_minion.colliderect(obj_banana) or \
                    obj_purple_minion.colliderect(obj_red_minion) or obj_purple_minion.colliderect(obj_green_minion):
                obj_purple_minion, cord_y_purple_minion, cord_x_purple_minion = change_pos(image_purple_minion)

            if obj_unicorn.colliderect(obj_banana) or obj_unicorn.colliderect(obj_yellow_minion) or \
                    obj_unicorn.colliderect(obj_red_minion) or obj_unicorn.colliderect(obj_green_minion):
                obj_unicorn, cord_y_unicorn, cord_x_unicorn = change_pos(image_unicorn)

            if obj_banana.colliderect(obj_yellow_minion) or obj_banana.colliderect(
                    obj_green_minion) or obj_banana.colliderect(obj_red_minion):
                obj_banana, cord_y_banana, cord_x_banana = change_pos(image_banana)

        test_collision_red = True
        if test_collision_red:
            if obj_symbol.colliderect(obj_yellow_minion):
                collision_counter += 1
                good_minion_counter += 1
                score_counter += 5
                cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, \
                    cord_x_green_minion, cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, \
                    cord_y_symbol = reset_pos_balls()
                sound_of_collision.play()
                if break_unicorn_to_appear and break_banana_to_appear == 10:
                    cord_x_unicorn, cord_y_unicorn = generate_random_coordinates()
                    cord_x_banana, cord_y_banana = generate_random_coordinates()
                else:
                    if collision_counter % break_unicorn_to_appear == 0:
                        cord_x_unicorn, cord_y_unicorn = generate_random_coordinates()
                        if collision_counter % break_banana_to_appear == 0:
                            cord_x_banana, cord_y_banana = generate_random_coordinates()
                    else:
                        cord_x_unicorn = cord_y_unicorn = cord_y_banana = cord_x_banana = -200

            if obj_symbol.colliderect(obj_unicorn):
                collision_counter += 1
                score_counter += 10
                unicorn_counter += 1
                cord_x_unicorn = cord_y_unicorn = cord_x_banana = cord_y_banana = -200
                cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, \
                    cord_x_green_minion, cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, \
                    cord_y_symbol = reset_pos_balls()
                sound_of_collision.play()
                if break_unicorn_to_appear and break_banana_to_appear == 10:
                    cord_x_unicorn, cord_y_unicorn = generate_random_coordinates()
                    cord_x_banana, cord_y_banana = generate_random_coordinates()

            if obj_symbol.colliderect(obj_banana):
                collision_counter += 1
                score_counter += 20
                banana_counter += 1
                cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = -200
                cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, \
                    cord_x_green_minion, cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, \
                    cord_y_symbol = reset_pos_balls()

                if break_unicorn_to_appear and break_banana_to_appear == 10:
                    cord_x_unicorn, cord_y_unicorn = generate_random_coordinates()
                    cord_x_banana, cord_y_banana = generate_random_coordinates()

                sound_of_clicking.play()
                sound_of_collision.play()

            if obj_symbol.colliderect(obj_purple_minion):
                score_counter -= 10
                bad_minions_counter += 1
                if score_counter < 0:
                    score_counter = 0
                cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, \
                    cord_x_green_minion, cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, \
                    cord_y_symbol = reset_pos_balls()
                cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = -200
                sound_of_collision.play()

            if obj_symbol.colliderect(obj_green_minion):
                bad_minions_counter += 1
                score_counter -= 10
                if score_counter < 0:
                    score_counter = 0
                cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, \
                    cord_x_green_minion, cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, \
                    cord_x_symbol, cord_y_symbol = reset_pos_balls()
                cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = -200
                sound_of_collision.play()

            if obj_symbol.colliderect(obj_red_minion):
                bad_minions_counter += 1
                score_counter -= 10
                if score_counter < 0:
                    score_counter = 0
                    cord_x_yellow_minion, cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                        cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = reset_pos_balls()
                cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = -200  # reseta bolas verdes e azuis
                sound_of_collision.play()

        end = time.time()
        timer = (end - start)
        timer_to_print = f'{timer:.0f}s'
        score_to_print = f'{score_counter}'
        timer_format = font_3.render(timer_to_print, True, (0, 0, 0))
        score_format = font_3.render(score_to_print, True, (0, 0, 0))
        screen.blit(timer_format, (680, 10))
        screen.blit(score_format, (260, 10))
        pygame.display.flip()
        if timer > 30:
            screen_game_on = False

    while screen_after_game_on:
        screen.blit(image_after_game_screen, (0, 0))
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False
            keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        if is_hovering_menu_after_game(mouse):
            screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = True
                screen_game_on = screen_after_game_on = False

        if is_hovering_quit_after_game(mouse):
            screen.blit(image_button_quit_white, (380, 638))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False

        unicorn_to_print = f'{unicorn_counter}'
        bad_minions_to_print = f'{bad_minions_counter}'
        good_minion_to_print = f'{good_minion_counter}'
        banana_to_print = f'{banana_counter}'

        unicorn_format = font_1.render(unicorn_to_print, True, (0, 0, 0))
        bad_minions_format = font_1.render(bad_minions_to_print, True, (0, 0, 0))
        good_minion_format = font_1.render(good_minion_to_print, True, (0, 0, 0))
        banana_format = font_1.render(banana_to_print, True, (0, 0, 0))
        score_format = font_4.render(score_to_print, True, (255, 255, 255))

        screen.blit(good_minion_format, (267, 250))
        screen.blit(unicorn_format, (420, 250))
        screen.blit(banana_format, (565, 250))
        screen.blit(bad_minions_format, (730, 250))
        screen.blit(score_format, (625, 345))
        pygame.display.flip()

pygame.quit()

