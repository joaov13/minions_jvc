import pygame

from functions import generate_random_coordinates

image_menu_screen = pygame.image.load('data/screen_images/menu_screen.png')
image_game_screen = pygame.image.load('data/screen_images/game_screen.png')
image_after_game_screen = pygame.image.load('data/screen_images/screen_after_game.png')
image_score_screen = pygame.image.load('data/screen_images/score_screen.png')
image_about_screen = pygame.image.load('data/screen_images/screen_about.png')
image_tutorial_screen = pygame.image.load('data/screen_images/tutorial_screen.png')
image_yellow_minion = pygame.image.load('data/balls/yellow.png')
image_unicorn = pygame.image.load('data/balls/unicorn.png')
image_banana = pygame.image.load('data/balls/banana.png')
image_purple_minion = pygame.image.load('data/balls/purple.png')
image_green_minion = pygame.image.load('data/balls/green.png')
image_red_minion = pygame.image.load('data/balls/red.png')
image_symbol = pygame.image.load('data/balls/black.png')
image_button_start_white = pygame.image.load('data/buttons/start_white.png')
image_button_quit_white = pygame.image.load('data/buttons/quit_white.png')
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
image_button_score_white = pygame.image.load('data/buttons/score_white.png')
image_button_about_white = pygame.image.load('data/buttons/about_white.png')
image_button_reset_white = pygame.image.load('data/buttons/reset_white.png')
image_button_time_white = pygame.image.load('data/buttons/time_white.png')
image_arrows = pygame.image.load('data/buttons/arrows.png')


SPAWN_SYMBOL_X = 540
SPAWN_SYMBOL_Y = 360
cord_x_symbol = SPAWN_SYMBOL_X
cord_y_symbol = SPAWN_SYMBOL_Y
displacement = 30
level = 'normal'

cord_out_screen = (-200, -200)

cord_x_yellow_minion, cord_y_yellow_minion = generate_random_coordinates()
cord_x_purple_minion, cord_y_purple_minion = generate_random_coordinates()
cord_x_green_minion, cord_y_green_minion = generate_random_coordinates()
cord_x_red_minion, cord_y_red_minion = generate_random_coordinates()
cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = generate_random_coordinates()

collision_counter = 0
score_list = [0]
the_highest_score = 0
time_choice = 30
start_time_tutorial = 0
