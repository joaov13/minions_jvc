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
cord_y_unicorn = cord_x_unicorn = cord_y_banana = cord_x_banana = generate_random_coordinates()

collision_counter = 0
score_list = [0]
the_highest_score = 0
time_choice = 30
