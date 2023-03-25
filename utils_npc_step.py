import random


def first_step(game_list):
    """
    Первый ход NPC
    :param game_list:
    :return:
    """
    if game_list[4] == '-':
        game_list[4] = '0'
        return game_list
    elif game_list[0] == '-':
        game_list[0] = '0'
        return game_list


def two_step(game_list, last_step_user):
    global k
    list_step_user = [item for item, value in enumerate(game_list) if value == 'X']
    all_win_option = all_option()
    for option in all_win_option:
        if len(set(option).difference(set(list_step_user))) == 1:
            need_position = set(option).difference(set(list_step_user))
            for i in need_position:
                k = i
                if game_list[k] == '-':
                    game_list[k] = '0'
                    break
                elif game_list[2] == '-':
                    game_list[2] = '0'
                    break
                elif game_list[6] == '-':
                    game_list[6] = '0'
                    break
                elif game_list[8] == '-':
                    game_list[8] = '0'
                    break
        else:
            if last_step_user == 5:
                game_list[8] = '0'


    return game_list


def three_step(game_list):
    pass


def four_step(game_list):
    pass


def check_x_step(list_x):
    pass


def all_option():
    """Все возможные варианты выигрыша"""
    option = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    return option