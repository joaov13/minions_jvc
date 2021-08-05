import pygame
import time
from functions import *


def process_first_screen(info_game):
    info_game.show_first_screen = True
    while info_game.show_first_screen:
        info_game.screen.blit(image_first_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_first_screen = False
        '''PLAY'''
        if is_hovering_play_first_screen(mouse):
            info_game.screen.blit(image_button_play_white, (384, 170))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_first_screen = False
                info_game.show_game_mode_screen = True
                pygame.time.delay(200)
        '''SOUNDS'''
        if info_game.sound_of_game_on:
            info_game.screen.blit(image_button_new_sound_on_black, (384, 282))
        else:
            info_game.screen.blit(image_button_new_sound_off_black, (384, 282))
        change_volume(info_game, mouse)

        '''SCORE'''
        if is_hovering_score_first_screen(mouse):
            info_game.screen.blit(image_button_new_score_white, (384, 394))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_first_screen = False
                info_game.show_score_screen = True
                pygame.time.delay(200)

        '''ABOUT'''
        if is_hovering_about_first_screen(mouse):
            info_game.screen.blit(image_button_new_about_white, (386, 506))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_about_screen = True
                info_game.show_first_screen = False
                pygame.time.delay(200)

        '''QUIT'''
        if is_hovering_quit_first_screen(mouse):
            info_game.screen.blit(image_button_new_quit_white, (386, 618))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_first_screen = False
                pygame.time.delay(200)
        pygame.display.update()


def process_choose_game_mode(info_game):
    info_game.show_game_mode_screen = True
    while info_game.show_game_mode_screen:
        info_game.screen.blit(image_choose_game_mode_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_game_mode_screen = False
        '''PLAY'''
        if is_hovering_play_in_game_mode(mouse):
            info_game.screen.blit(image_button_play_white, (735, 619))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
                info_game.show_game_mode_screen = False
                info_game.show_settings_screen = True
        '''MENU'''
        if is_hovering_menu_in_game_mode(mouse):
            info_game.screen.blit(image_button_new_menu_white, (74, 619))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_game_mode_screen = False
                info_game.show_first_screen = True
                pygame.time.delay(200)
        if info_game.current_settings.game_mode_choice == 'classic':
            info_game.screen.blit(image_classic_info, (581, 270))
        elif info_game.current_settings.game_mode_choice == 'dodge':
            info_game.screen.blit(image_dodge_info, (581, 270))
        elif info_game.current_settings.game_mode_choice == 'modern':
            info_game.screen.blit(image_modern_info, (581, 270))

        '''CLASSIC'''
        if is_hovering_classic(mouse):
            info_game.screen.blit(image_button_classic_white, (131, 290))
            info_game.screen.blit(image_classic_info, (581, 270))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.current_settings.game_mode_choice = 'classic'
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
        '''DODGE'''
        if is_hovering_dodge(mouse):
            info_game.screen.blit(image_button_dodge_white, (131, 390))
            info_game.screen.blit(image_dodge_info, (581, 270))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.current_settings.game_mode_choice = 'dodge'
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
        '''BIG'''
        if is_hovering_modern(mouse):
            info_game.screen.blit(image_button_modern_white, (131, 490))
            info_game.screen.blit(image_modern_info, (581, 270))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.current_settings.game_mode_choice = 'modern'
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
        pygame.display.update()


def process_settings_screen(info_game):
    info_game.show_settings_screen = True
    while info_game.show_settings_screen:
        info_game.screen.blit(image_choose_settings_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_settings_screen = False

        if is_hovering_play_in_settings_screen(mouse):
            info_game.screen.blit(image_button_play_white, (735, 619))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
                info_game.show_settings_screen = False
                if info_game.current_settings.game_mode_choice == 'classic':
                    info_game.show_classic_game_screen = True
                    set_to_zero_counters(info_game)
                elif info_game.current_settings.game_mode_choice == 'dodge':
                    info_game.show_dodge_game_screen = True
                    set_to_zero_counters(info_game)

        if is_hovering_menu_in_settings_screen(mouse):
            info_game.screen.blit(image_button_new_menu_white, (74, 619))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
                info_game.show_settings_screen = False
                info_game.show_first_screen = True
        set_character(mouse, info_game)
        set_level(mouse, info_game)
        set_time(mouse, info_game)
        pygame.display.update()


def process_classic_game_screen(info_game):
    info_game.show_classic_game_screen = True
    info_game.current_settings.start_timer_classic = time.time()
    while info_game.show_classic_game_screen:
        print(info_game.the_highest_score)
        info_game.screen.blit(image_game_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        info_game.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_classic_game_screen = False

        if is_hovering_up_quit_in_game(mouse):
            info_game.screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_classic_game_screen = False
                info_game.show_after_game_screen = True
                process_screen_after_game(info_game)

        if info_game.keys[pygame.K_w] and info_game.current_coordinates.cord_y_symbol >= 120:
            info_game.current_coordinates.cord_y_symbol -= info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_s] and info_game.current_coordinates.cord_y_symbol <= 625:
            info_game.current_coordinates.cord_y_symbol += info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_d] and info_game.current_coordinates.cord_x_symbol <= 980:
            info_game.current_coordinates.cord_x_symbol += info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_a] and info_game.current_coordinates.cord_x_symbol >= 30:
            info_game.current_coordinates.cord_x_symbol -= info_game.current_coordinates.displacement

        '''SPAWN OBJECTS'''
        obj_yellow_minion = info_game.screen.blit(image_yellow_minion, (
            info_game.current_coordinates.cord_x_yellow_minion, info_game.current_coordinates.cord_y_yellow_minion))
        obj_character = spawn_obj_character(info_game)

        if info_game.current_settings.level_choice == 'easy':
            obj_unicorn = info_game.screen.blit(image_unicorn, (
                info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            obj_banana = info_game.screen.blit(image_banana,
                                               (info_game.current_coordinates.cord_x_banana,
                                                info_game.current_coordinates.cord_y_banana))
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))
            obj_green_minion = info_game.screen.blit(image_green_minion, info_game.current_coordinates.cord_out_screen)
            obj_red_minion = info_game.screen.blit(image_red_minion, info_game.current_coordinates.cord_out_screen)

        elif info_game.current_settings.level_choice == 'normal':
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))
            obj_green_minion = info_game.screen.blit(image_green_minion, info_game.current_coordinates.cord_out_screen)
            obj_red_minion = info_game.screen.blit(image_red_minion, info_game.current_coordinates.cord_out_screen)

            if info_game.collision_counter != 0 and (info_game.collision_counter % 3 == 0):
                obj_unicorn = info_game.screen.blit(image_unicorn, (
                    info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            else:
                obj_unicorn = info_game.screen.blit(image_unicorn, info_game.current_coordinates.cord_out_screen)
            if info_game.collision_counter != 0 and (info_game.collision_counter % 6 == 0):
                obj_banana = info_game.screen.blit(image_banana, (
                    info_game.current_coordinates.cord_x_banana, info_game.current_coordinates.cord_y_banana))
            else:
                obj_banana = info_game.screen.blit(image_banana, info_game.current_coordinates.cord_out_screen)

        elif info_game.current_settings.level_choice == 'hard':
            obj_green_minion = info_game.screen.blit(image_green_minion, (
                info_game.current_coordinates.cord_x_green_minion, info_game.current_coordinates.cord_y_green_minion))
            obj_red_minion = info_game.screen.blit(image_red_minion, (
                info_game.current_coordinates.cord_x_red_minion, info_game.current_coordinates.cord_y_red_minion))
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))

            if info_game.collision_counter != 0 and (info_game.collision_counter % 5 == 0):
                obj_unicorn = info_game.screen.blit(image_unicorn, (
                    info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            else:
                obj_unicorn = info_game.screen.blit(image_unicorn, info_game.current_coordinates.cord_out_screen)
            if info_game.collision_counter != 0 and (info_game.collision_counter % 10 == 0):
                obj_banana = info_game.screen.blit(image_banana, (
                    info_game.current_coordinates.cord_x_banana, info_game.current_coordinates.cord_y_banana))
            else:
                obj_banana = info_game.screen.blit(image_banana, info_game.current_coordinates.cord_out_screen)
        check_collision = True
        if check_collision:
            if obj_character.colliderect(obj_yellow_minion):
                info_game.collision_counter += 1
                info_game.good_minion_counter += 1
                info_game.score_counter += 5
                change_all_objects_coordinates(info_game.current_coordinates)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_unicorn):
                info_game.collision_counter += 1
                info_game.score_counter += 10
                info_game.unicorn_counter += 1
                change_all_objects_coordinates(info_game.current_coordinates)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_banana):
                info_game.collision_counter += 1
                info_game.score_counter += 20
                info_game.banana_counter += 1
                change_all_objects_coordinates(info_game.current_coordinates)
                info_game.sound_of_clicking.play()
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_purple_minion) or obj_character.colliderect(obj_green_minion) or \
                    obj_character.colliderect(obj_red_minion):
                info_game.collision_counter += 1
                info_game.score_counter -= 10
                info_game.bad_minions_counter += 1
                if info_game.score_counter < 0:
                    info_game.score_counter = 0
                change_all_objects_coordinates(info_game.current_coordinates)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)

        info_game.current_settings.end_timer_classic = time.time()
        info_game.current_settings.timer = (
                    info_game.current_settings.end_timer_classic - info_game.current_settings.start_timer_classic)
        timer_to_print = f'{(info_game.current_settings.time_choice - info_game.current_settings.timer):.0f}s'
        info_game.current_settings.score_to_print = f'{info_game.score_counter}'
        timer_format = info_game.font_3.render(timer_to_print, True, (0, 0, 0))
        score_format = info_game.font_3.render(info_game.current_settings.score_to_print, True, (0, 0, 0))
        info_game.screen.blit(timer_format, (680, 10))
        info_game.screen.blit(score_format, (260, 10))
        pygame.display.flip()
        if info_game.current_settings.timer > info_game.current_settings.time_choice - 1:
            info_game.show_classic_game_screen = False
            info_game.show_after_game_screen = True
            process_screen_after_game(info_game)


def process_dodge_game_screen(info_game):
    info_game.show_dodge_game_screen = True
    info_game.current_settings.start_timer_classic = time.time()
    set_minions_coordinates_for_dodge_mode(info_game)
    change_displacement_of_minions(info_game)
    while info_game.show_dodge_game_screen:
        info_game.screen.blit(image_game_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        info_game.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_dodge_game_screen = False

        if is_hovering_up_quit_in_game(mouse):
            info_game.screen.blit(image_button_quit_2_white, (911, 30))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_dodge_game_screen = False
                info_game.show_after_game_screen = True
                process_screen_after_game(info_game)

        if info_game.keys[pygame.K_w] and info_game.current_coordinates.cord_y_symbol >= 120:
            info_game.current_coordinates.cord_y_symbol -= info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_s] and info_game.current_coordinates.cord_y_symbol <= 625:
            info_game.current_coordinates.cord_y_symbol += info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_d] and info_game.current_coordinates.cord_x_symbol <= 980:
            info_game.current_coordinates.cord_x_symbol += info_game.current_coordinates.displacement
        if info_game.keys[pygame.K_a] and info_game.current_coordinates.cord_x_symbol >= 30:
            info_game.current_coordinates.cord_x_symbol -= info_game.current_coordinates.displacement
        '''SPAWN OBJECTS'''
        obj_yellow_minion = info_game.screen.blit(image_yellow_minion, (info_game.current_coordinates.cord_x_yellow_minion, info_game.current_coordinates.cord_y_yellow_minion))
        obj_character = spawn_obj_character(info_game)

        if info_game.current_settings.level_choice == 'easy':
            obj_unicorn = info_game.screen.blit(image_unicorn, (
                info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            obj_banana = info_game.screen.blit(image_banana,
                                               (info_game.current_coordinates.cord_x_banana,
                                                info_game.current_coordinates.cord_y_banana))
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))
            obj_green_minion = info_game.screen.blit(image_green_minion, info_game.current_coordinates.cord_out_screen)
            obj_red_minion = info_game.screen.blit(image_red_minion, info_game.current_coordinates.cord_out_screen)

        elif info_game.current_settings.level_choice == 'normal':
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))
            obj_green_minion = info_game.screen.blit(image_green_minion, info_game.current_coordinates.cord_out_screen)
            obj_red_minion = info_game.screen.blit(image_red_minion, info_game.current_coordinates.cord_out_screen)

            if info_game.collision_counter != 0 and (info_game.collision_counter % 3 == 0):
                obj_unicorn = info_game.screen.blit(image_unicorn, (
                    info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            else:
                obj_unicorn = info_game.screen.blit(image_unicorn, info_game.current_coordinates.cord_out_screen)
            if info_game.collision_counter != 0 and (info_game.collision_counter % 6 == 0):
                obj_banana = info_game.screen.blit(image_banana, (
                    info_game.current_coordinates.cord_x_banana, info_game.current_coordinates.cord_y_banana))
            else:
                obj_banana = info_game.screen.blit(image_banana, info_game.current_coordinates.cord_out_screen)

        elif info_game.current_settings.level_choice == 'hard':
            obj_green_minion = info_game.screen.blit(image_green_minion, (
                info_game.current_coordinates.cord_x_green_minion, info_game.current_coordinates.cord_y_green_minion))
            obj_red_minion = info_game.screen.blit(image_red_minion, (
                info_game.current_coordinates.cord_x_red_minion, info_game.current_coordinates.cord_y_red_minion))
            obj_purple_minion = info_game.screen.blit(image_purple_minion, (
                info_game.current_coordinates.cord_x_purple_minion, info_game.current_coordinates.cord_y_purple_minion))

            if info_game.collision_counter != 0 and (info_game.collision_counter % 5 == 0):
                obj_unicorn = info_game.screen.blit(image_unicorn, (
                    info_game.current_coordinates.cord_x_unicorn, info_game.current_coordinates.cord_y_unicorn))
            else:
                obj_unicorn = info_game.screen.blit(image_unicorn, info_game.current_coordinates.cord_out_screen)
            if info_game.collision_counter != 0 and (info_game.collision_counter % 10 == 0):
                obj_banana = info_game.screen.blit(image_banana, (
                    info_game.current_coordinates.cord_x_banana, info_game.current_coordinates.cord_y_banana))
            else:
                obj_banana = info_game.screen.blit(image_banana, info_game.current_coordinates.cord_out_screen)

        move_minions_in_dodge_mode(info_game)
        check_collision = True
        if check_collision:
            if obj_character.colliderect(obj_yellow_minion):
                info_game.collision_counter += 1
                info_game.good_minion_counter += 1
                info_game.score_counter += 5
                change_all_objects_coordinates(info_game.current_coordinates)
                set_minions_coordinates_for_dodge_mode(info_game)
                change_displacement_of_minions(info_game)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_unicorn):
                info_game.collision_counter += 1
                info_game.score_counter += 10
                info_game.unicorn_counter += 1
                change_all_objects_coordinates(info_game.current_coordinates)
                set_minions_coordinates_for_dodge_mode(info_game)
                change_displacement_of_minions(info_game)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_banana):
                info_game.collision_counter += 1
                info_game.score_counter += 20
                info_game.banana_counter += 1
                change_all_objects_coordinates(info_game.current_coordinates)
                set_minions_coordinates_for_dodge_mode(info_game)
                change_displacement_of_minions(info_game)
                info_game.sound_of_clicking.play()
                info_game.sound_of_collision.play()
                pygame.time.delay(50)
            if obj_character.colliderect(obj_purple_minion) or obj_character.colliderect(obj_green_minion) or \
                    obj_character.colliderect(obj_red_minion):
                info_game.collision_counter += 1
                info_game.score_counter -= 10
                info_game.bad_minions_counter += 1
                if info_game.score_counter < 0:
                    info_game.score_counter = 0
                change_all_objects_coordinates(info_game.current_coordinates)
                set_minions_coordinates_for_dodge_mode(info_game)
                change_displacement_of_minions(info_game)
                info_game.sound_of_collision.play()
                pygame.time.delay(50)

        info_game.current_settings.end_timer_classic = time.time()
        info_game.current_settings.timer = (
                info_game.current_settings.end_timer_classic - info_game.current_settings.start_timer_classic)
        timer_to_print = f'{(info_game.current_settings.time_choice - info_game.current_settings.timer):.0f}s'
        info_game.current_settings.score_to_print = f'{info_game.score_counter}'
        timer_format = info_game.font_3.render(timer_to_print, True, (0, 0, 0))
        score_format = info_game.font_3.render(info_game.current_settings.score_to_print, True, (0, 0, 0))
        info_game.screen.blit(timer_format, (680, 10))
        info_game.screen.blit(score_format, (260, 10))
        pygame.display.flip()
        if info_game.current_settings.timer > info_game.current_settings.time_choice - 1:
            info_game.show_classic_game_screen = False
            info_game.show_after_game_screen = True
            process_screen_after_game(info_game)


def process_screen_after_game(info_game):
    # info_game.show_after_game_screen = True
    info_game.flag_for_append_score = True
    info_game.screen.blit(image_after_game_screen, (0, 0))
    while info_game.show_after_game_screen:
        print_things_after_game_screen(info_game)
        mouse = pygame.mouse.get_pos()
        if info_game.flag_for_append_score:
            info_game.score_list.append(int(info_game.score_counter))
            info_game.flag_for_append_score = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_after_game_screen = False

        if is_hovering_menu_after_game(mouse):
            info_game.screen.blit(image_button_menu_white, (380, 553))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_settings_screen = True
                info_game.show_after_game_screen = False
                pygame.time.delay(100)
        pygame.display.flip()


def process_score_screen(info_game):
    info_game.show_score_screen = True
    info_game.the_highest_score = checking_highest_score(info_game)
    while info_game.show_score_screen:
        info_game.screen.blit(image_new_score_screen, (0, 0))
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_score_screen = False

        if is_hovering_menu_in_score(mouse):
            info_game.screen.blit(image_button_new_menu_white, (383, 614))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                pygame.time.delay(200)
                info_game.show_score_screen = False
                info_game.show_first_screen = True

        if is_hovering_reset_in_score(mouse):
            info_game.screen.blit(image_button_new_reset_white, (383, 421))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                reset_scores(info_game)

        highest_score_to_print = f'{info_game.the_highest_score}'
        highest_score_format = info_game.font_4.render(highest_score_to_print, True, (0, 0, 0))
        info_game.screen.blit(highest_score_format, (470, 295))
        pygame.display.flip()
        pygame.display.update()


def process_screen_about(info_game):
    info_game.show_about_screen = True
    while info_game.show_about_screen:
        info_game.screen.blit(image_new_about_screen, (0, 0))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info_game.show_about_screen = False

        if is_hovering_menu_in_about(mouse):
            info_game.screen.blit(image_button_new_menu_white, (383, 614))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                info_game.sound_of_clicking.play()
                info_game.show_first_screen = True
                info_game.show_about_screen = False
                pygame.time.delay(100)
        pygame.display.flip()


def main():
    FPS = 60
    clock = pygame.time.Clock()
    pygame.init()
    info_game = Game()
    game_on = True
    while game_on:
        clock.tick(FPS)
        if info_game.show_first_screen:
            process_first_screen(info_game)
        elif info_game.show_game_mode_screen:
            process_choose_game_mode(info_game)
        elif info_game.show_settings_screen:
            process_settings_screen(info_game)
        elif info_game.show_classic_game_screen:
            process_classic_game_screen(info_game)
        elif info_game.show_dodge_game_screen:
            process_dodge_game_screen(info_game)
        elif info_game.show_score_screen:
            process_score_screen(info_game)
        elif info_game.show_about_screen:
            process_screen_about(info_game)
        else:
            game_on = False
            write_scores_to_file(info_game)

    pygame.quit()


if __name__ == "__main__":
    main()
