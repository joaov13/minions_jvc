import random


SPAWN_SYMBOL_X = 540
SPAWN_SYMBOL_Y = 360


def is_hovering_quit(mouse):
    return (379 + 300 > mouse[0] > 379) and (569 + 75 > mouse[1] > 569)


def is_hovering_quit_game(mouse):
    return (911 + 145 > mouse[0] > 912) and (30 + 36 > mouse[1] > 30)


def is_hovering_quit_down(mouse):
    return (380 + 300 > mouse[0] > 380) and (638 + 75 > mouse[1] > 638)


def is_hovering_reset(mouse):
    return (380 + 300 > mouse[0] > 380) and (468 + 75 > mouse[1] > 468)


def is_hovering_menu_down(mouse):
    return (380 + 300 > mouse[0] > 380) and (553 + 75 > mouse[1] > 553)


def is_hovering_start(mouse):
    return (204 + 300 > mouse[0] > 204) and (212 + 75 > mouse[1] > 212)


def is_hovering_level(mouse):
    return (539 + 300 > mouse[0] > 539) and (212 + 75 > mouse[1] > 212)


def is_hovering_sounds(mouse):
    return (204 + 300 > mouse[0] > 204) and (331 + 75 > mouse[1] > 331)


def is_hovering_about(mouse):
    return (204 + 300 > mouse[0] > 204) and (450 + 75 > mouse[1] > 450)


def is_hovering_time(mouse):
    return (539 + 300 > mouse[0] > 539) and (331 + 75 > mouse[1] > 331)


def is_hovering_score(mouse):
    return (539 + 300 > mouse[0] > 539) and (450 + 75 > mouse[1] > 450)


def generate_random_coordinates():
    """ Generates random x and y inside the screen and NOT in the center region """
    pos_x = (random.randint(60, 990))
    # does not spawn in the center region of the screen
    while 480 < pos_x < 620:
        pos_x = (random.randint(60, 990))

    pos_y = (random.randint(150, 650))
    # does not spawn in the center region of the screen
    while 270 < pos_y < 460:
        pos_y = (random.randint(150, 650))

    return pos_x, pos_y


def reset_pos_balls():
    x_uni, y_uni = generate_random_coordinates()
    x_banana, y_banana = generate_random_coordinates()
    x_yellow, y_yellow = generate_random_coordinates()
    x_purple, y_purple = generate_random_coordinates()
    x_green, y_green = generate_random_coordinates()
    x_red, y_red = generate_random_coordinates()
    x_symbol = SPAWN_SYMBOL_X
    y_symbol = SPAWN_SYMBOL_Y
    return x_uni, y_uni, x_banana, y_banana, x_yellow, y_yellow, x_purple, y_purple, x_green, y_green, x_red, y_red, \
        x_symbol, y_symbol


def reading_scores_from_score_data():
    read_scores = []
    highest_score = 0
    with open('score_data.txt', 'r') as score_to_read:
        for score in score_to_read:
            if score != '\n':
                read_scores.append(int(score))
    for scores in read_scores:
        if (highest_score == 0) or (scores > highest_score):
            highest_score = scores
    return highest_score
