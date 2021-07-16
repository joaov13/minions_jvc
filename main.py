import time
import random
from variables import*


from functions import is_hovering_quit, is_hovering_quit_game, is_hovering_quit_down, \
    is_hovering_menu_down, is_hovering_start, is_hovering_level, is_hovering_sounds, \
    is_hovering_about, is_hovering_reset, is_hovering_score, reset_pos_balls, reading_scores_from_score_data, \
    is_hovering_time


def change_pos(ball_image):
    y_for_ball, x_for_ball = generate_random_coordinates()
    draw_ball = screen.blit(ball_image, (x_for_ball, y_for_ball))
    return draw_ball, y_for_ball, x_for_ball


pygame.init()
pygame.mixer.music.set_volume(0)
pygame.mixer.music.load('data/sounds/soundtrack.mp3')
pygame.mixer.music.play(-1)
sound_of_collision = pygame.mixer.Sound('data/sounds/sound.wav')
sound_of_collision.set_volume(0.9)
sound_of_clicking = pygame.mixer.Sound('data/sounds/click_sound.wav')
sound_of_clicking.set_volume(0.7)
volume_adjust = 3
sound_of_game_on = True
font_1 = pygame.font.SysFont('arial', 50, True, False)
font_2 = pygame.font.SysFont('arial', 42, True, False)
font_3 = pygame.font.SysFont('arial', 70, True, False)
font_4 = pygame.font.SysFont('arial', 90, True, False)
pygame.display.set_caption("Minions game")
screen = pygame.display.set_mode((1080, 720))
entire_game_on = True
show_tutorial = True
while entire_game_on:
    screen_menu_on = True
    screen_tutorial_on = True
    screen_game_on = True
    screen_after_game_on = True
    screen_score_on = False
    screen_about_on = False

    while screen_menu_on:
        pygame.time.delay(50)
        screen.blit(image_menu_screen, (0, 0))
        score_counter = banana_counter = unicorn_counter = bad_minions_counter = good_minion_counter = 0
        screen.blit(image_button_sounds_on_black, (204, 331))
        mouse = pygame.mouse.get_pos()
        print(mouse)

        if level == 'normal':
            screen.blit(image_button_level_normal_black, (539, 212))
        elif level == 'easy':
            screen.blit(image_button_level_easy_black, (539, 212))
        elif level == 'hard':
            screen.blit(image_button_level_hard_black, (539, 212))

        if sound_of_game_on:
            screen.blit(image_button_sounds_on_black, (204, 331))
        else:
            screen.blit(image_button_sounds_off_black, (204, 331))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False
            keys = pygame.key.get_pressed()

        if is_hovering_start(mouse):
            screen.blit(image_button_start_white, (204, 212))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = False
                score_counter = timer = 0
                if not show_tutorial:
                    start = 0
                    start = time.time()
                else:
                    start_time_tutorial = time.time()
                pygame.time.delay(100)
        if is_hovering_level(mouse):
            if level == 'normal':
                screen.blit(image_button_level_normal_white, (539, 212))
            elif level == 'easy':
                screen.blit(image_button_level_easy_white, (539, 212))
            elif level == 'hard':
                screen.blit(image_button_level_hard_white, (539, 212))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                if level == 'normal':
                    level = 'hard'
                    pygame.time.delay(150)
                elif level == 'hard':
                    level = 'easy'
                    pygame.time.delay(150)
                elif level == 'easy':
                    level = 'normal'
                    pygame.time.delay(150)

        if is_hovering_sounds(mouse):
            if sound_of_game_on:
                screen.blit(image_button_sounds_on_white, (204, 331))
            else:
                screen.blit(image_button_sounds_off_white, (204, 331))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if volume_adjust % 2 == 0:
                    pygame.mixer.music.set_volume(0.1)
                    sound_of_collision.set_volume(0.9)
                    sound_of_clicking.set_volume(0.7)
                    volume_adjust += 1
                    pygame.time.delay(200)
                    sound_of_game_on = True
                    sound_of_clicking.play()
                else:
                    sound_of_game_on = False
                    pygame.mixer.music.set_volume(0)
                    sound_of_collision.set_volume(0)
                    sound_of_clicking.set_volume(0)
                    volume_adjust += 1
                    pygame.time.delay(200)

        if is_hovering_quit(mouse):
            screen.blit(image_button_quit_white, (379, 569))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False

        if is_hovering_time(mouse):
            screen.blit(image_button_time_white, (539, 331))
            time_choice_to_print = f'{time_choice}s'
            time_choice_format = font_3.render(time_choice_to_print, True, (255, 255, 255))
            screen.blit(time_choice_format, (641, 330))

            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                pygame.time.delay(200)
                if time_choice == 60:
                    time_choice = 30
                elif time_choice == 30:
                    time_choice = 60

        if is_hovering_score(mouse):
            screen.blit(image_button_score_white, (539, 450))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = False
                screen_score_on = True
                pygame.time.delay(40)

        if is_hovering_about(mouse):
            screen.blit(image_button_about_white, (204, 450))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = screen_score_on = False
                screen_about_on = True
                pygame.time.delay(40)

        pygame.display.update()
        checking_highest_score = True

    while screen_tutorial_on:
        screen.blit(image_tutorial_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = \
                    screen_score_on = screen_about_on = screen_tutorial_on = False
            keys = pygame.key.get_pressed()

        if is_hovering_quit_game(mouse):
            screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_tutorial_on = False
                show_tutorial = False
                start = 0
                start = time.time()
                pygame.time.delay(50)
        end_time_tutorial = time.time()
        timer_tutorial = (end_time_tutorial - start_time_tutorial)
        timer_tutorial_to_print = f'{(10 - timer_tutorial):.0f}s'
        timer_tutorial_format = font_4.render(timer_tutorial_to_print, True, (255, 0, 0))
        screen.blit(timer_tutorial_format, (675, 600))
        if timer_tutorial >= 9.5:
            screen_tutorial_on = False
            show_tutorial = False
            start = 0
            start = time.time()
        print(mouse)
        pygame.display.flip()

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

        if level == 'easy':
            obj_unicorn = screen.blit(image_unicorn, (cord_x_unicorn, cord_y_unicorn))
            obj_banana = screen.blit(image_banana, (cord_x_banana, cord_y_banana))
            obj_purple_minion = screen.blit(image_purple_minion, (cord_x_purple_minion, cord_y_purple_minion))
            obj_green_minion = screen.blit(image_green_minion, cord_out_screen)
            obj_red_minion = screen.blit(image_red_minion, cord_out_screen)

        elif level == 'normal':
            obj_purple_minion = screen.blit(image_purple_minion, (cord_x_purple_minion, cord_y_purple_minion))
            if collision_counter != 0 and (collision_counter % 3 == 0):
                obj_unicorn = screen.blit(image_unicorn, (cord_x_unicorn, cord_y_unicorn))
            else:
                obj_unicorn = screen.blit(image_unicorn, cord_out_screen)
            if collision_counter != 0 and (collision_counter % 6 == 0):
                obj_banana = screen.blit(image_banana, (cord_x_banana, cord_y_banana))
            else:
                obj_banana = screen.blit(image_banana, cord_out_screen)
            obj_green_minion = screen.blit(image_green_minion, cord_out_screen)
            obj_red_minion = screen.blit(image_red_minion, cord_out_screen)

        elif level == 'hard':
            obj_green_minion = screen.blit(image_green_minion, (cord_x_green_minion, cord_y_green_minion))
            obj_red_minion = screen.blit(image_red_minion, (cord_x_red_minion, cord_y_red_minion))
            obj_purple_minion = screen.blit(image_purple_minion, (cord_x_purple_minion, cord_y_purple_minion))

            if collision_counter != 0 and (collision_counter % 5 == 0):
                obj_unicorn = screen.blit(image_unicorn, (cord_x_unicorn, cord_y_unicorn))
            else:
                obj_unicorn = screen.blit(image_unicorn, cord_out_screen)
            if collision_counter != 0 and (collision_counter % 10== 0):
                obj_banana = screen.blit(image_banana, (cord_x_banana, cord_y_banana))
            else:
                obj_banana = screen.blit(image_banana, cord_out_screen)
        obj_yellow_minion = screen.blit(image_yellow_minion, (cord_x_yellow_minion, cord_y_yellow_minion))
        obj_symbol = screen.blit(image_symbol, (cord_x_symbol, cord_y_symbol))

        test_collision_spawn = True
        if test_collision_spawn:
            if obj_purple_minion.colliderect(obj_yellow_minion):
                obj_purple_minion, cord_x_purple_minion, cord_y_purple_minion = change_pos(image_purple_minion)

            if obj_green_minion.colliderect(obj_yellow_minion) or obj_green_minion.colliderect(obj_red_minion):
                obj_green_minion, cord_x_green_minion, cord_y_green_minion = change_pos(image_green_minion)

            if obj_red_minion.colliderect(obj_yellow_minion):
                obj_red_minion, cord_x_red_minion, cord_y_red_minion = change_pos(image_red_minion)

            if obj_purple_minion.colliderect(obj_unicorn) or obj_purple_minion.colliderect(obj_banana) or \
                    obj_purple_minion.colliderect(obj_red_minion) or obj_purple_minion.colliderect(obj_green_minion):
                obj_purple_minion, cord_x_purple_minion, cord_y_purple_minion = change_pos(image_purple_minion)

            if obj_unicorn.colliderect(obj_banana) or obj_unicorn.colliderect(obj_yellow_minion) or \
                    obj_unicorn.colliderect(obj_red_minion) or obj_unicorn.colliderect(obj_green_minion):
                obj_unicorn, cord_x_unicorn, cord_y_unicorn = change_pos(image_unicorn)

            if obj_banana.colliderect(obj_yellow_minion) or obj_banana.colliderect(
                    obj_green_minion) or obj_banana.colliderect(obj_red_minion):
                obj_banana, cord_x_banana, cord_y_banana = change_pos(image_banana)

        test_collision_red = True
        if test_collision_red:
            if obj_symbol.colliderect(obj_yellow_minion):
                collision_counter += 1
                good_minion_counter += 1
                score_counter += 5
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion,\
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()
                sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_unicorn):
                collision_counter += 1
                score_counter += 10
                unicorn_counter += 1
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()
                sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_banana):
                collision_counter += 1
                score_counter += 20
                banana_counter += 1
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()
                sound_of_clicking.play()
                sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_purple_minion):
                score_counter -= 10
                bad_minions_counter += 1
                if score_counter < 0:
                    score_counter = 0
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()
                sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_green_minion):
                bad_minions_counter += 1
                score_counter -= 10
                if score_counter < 0:
                    score_counter = 0
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()

                sound_of_collision.play()
                pygame.time.delay(50)
            if obj_symbol.colliderect(obj_red_minion):
                collision_counter += 1
                score_counter -= 10
                if score_counter < 0:
                    score_counter = 0
                cord_x_unicorn, cord_y_unicorn, cord_x_banana, cord_y_banana, cord_x_yellow_minion, \
                    cord_y_yellow_minion, cord_x_purple_minion, cord_y_purple_minion, cord_x_green_minion, \
                    cord_y_green_minion, cord_x_red_minion, cord_y_red_minion, cord_x_symbol, cord_y_symbol = \
                    reset_pos_balls()
                sound_of_collision.play()
                pygame.time.delay(50)
        print(mouse)
        end = time.time()
        timer = (end - start)
        timer_to_print = f'{(time_choice - timer):.0f}s'
        score_to_print = f'{score_counter}'
        timer_format = font_3.render(timer_to_print, True, (0, 0, 0))
        score_format = font_3.render(score_to_print, True, (0, 0, 0))
        screen.blit(timer_format, (680, 10))
        screen.blit(score_format, (260, 10))
        pygame.display.flip()
        flag_for_append_score = True
        if timer > time_choice:
            screen_game_on = False

    while screen_after_game_on:
        screen.blit(image_after_game_screen, (0, 0))
        pygame.time.delay(50)
        if flag_for_append_score:
            score_list.append(int(score_counter))
            flag_for_append_score = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = False
            keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        if is_hovering_menu_down(mouse):
            screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                pygame.time.delay(100)
                screen_menu_on = True
                screen_game_on = screen_after_game_on = screen_score_on = screen_about_on = False

        if is_hovering_quit_down(mouse):
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
        checking_highest_score = True

    while screen_score_on:
        screen.blit(image_score_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()

        if checking_highest_score:
            highest_score_from_list = max(score_list)
            highest_score_from_score_data = reading_scores_from_score_data()
            if highest_score_from_score_data > highest_score_from_list:
                the_highest_score = highest_score_from_score_data
                checking_highest_score = False
            else:
                the_highest_score = highest_score_from_list
                checking_highest_score = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = screen_score_on = False
            keys = pygame.key.get_pressed()

        if is_hovering_menu_down(mouse):
            screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = True
                screen_game_on = screen_after_game_on = screen_score_on = screen_about_on = False

        if is_hovering_quit_down(mouse):
            screen.blit(image_button_quit_white, (380, 638))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = screen_score_on = False

        if is_hovering_reset(mouse):
            screen.blit(image_button_reset_white, (380, 468))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                pygame.time.delay(50)
                the_highest_score = 0
                with open('score_data.txt', 'w') as score_to_write:
                    for score in score_list:
                        score_to_write.write(str(score) + '\n')

        highest_score_to_print = f'{the_highest_score}'
        highest_score_format = font_4.render(highest_score_to_print, True, (255, 255, 255))
        screen.blit(highest_score_format, (470, 310))
        print(mouse)
        pygame.display.flip()

    while screen_about_on:
        screen.blit(image_about_screen, (0, 0))
        pygame.time.delay(50)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = \
                    screen_score_on = screen_about_on = False
            keys = pygame.key.get_pressed()

        if is_hovering_menu_down(mouse):
            screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_menu_on = True
                screen_game_on = screen_after_game_on = screen_score_on = screen_about_on = False
                pygame.time.delay(50)
        if is_hovering_quit_down(mouse):
            screen.blit(image_button_quit_white, (380, 638))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                sound_of_clicking.play()
                screen_about_on, screen_menu_on, screen_game_on, screen_after_game_on, entire_game_on, screen_score_on = False
                pygame.time.delay(50)
        pygame.display.flip()

with open('score_data.txt', 'a') as score_to_write:
    for score in score_list:
        if score != 0:
            score_to_write.write(str(score) + '\n')
pygame.quit()

# while screen_about_on:
#     screen.blit(IMAGEM, (0, 0))
#     pygame.time.delay(50)
#     mouse = pygame.mouse.get_pos()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             screen_menu_on = screen_game_on = screen_after_game_on = entire_game_on = \
#                 screen_score_on = screen_about_on = False
#         keys = pygame.key.get_pressed()
#     pygame.display.flip()
