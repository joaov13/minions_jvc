import random


def is_hovering_quit(mouse):
    return (379 + 300 > mouse[0] > 379) and (569 + 75 > mouse[1] > 569)


def is_hovering_quit_game(mouse):
    return (911 + 145 > mouse[0] > 912) and (30 + 36 > mouse[1] > 30)


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
    return list_x[0], list_x[1], list_x[2], list_x[3], list_x[4], list_x[5], list_y[0], list_y[1], list_y[2], list_y[3], list_y[4], list_y[5]


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


