import utils_npc_step as uns


def print_pole(game_list):
    """
    Отрисовать поле
    :param game_list: Игровое поле
    :return: отрисованное поле
    """
    for index, value in enumerate(game_list):
        if index % 3 == 0:
            print()

        print(value, end='  ')
    print()


def input_step(game_list):
    """
    Ввод игроком координаты установки крестика
    :param game_list:
    :return: Возвращает отвалидированную координату
    """
    print()
    i = True
    while i:
        x = int(input('введите координату Х '))
        if check_input_step(x, game_list):
            i = False
            return x
        else:
            print('Неправильные координаты, давай ещё раз')


def check_input_step(x, game_list):
    """
    Проверка введённого значения координаты
    :param x: Введенная координата установки крестика
    :param game_list: Игровое поле
    :return: Возвращает отвалидированные данные
    """
    if 0 <= x < 9 and game_list[x] == '-':
        return True
    else:
        return False


def npc_step(game_list, last_step_user):
    """
    Ход NPC
    :param game_list: игровое поле
    :return: Возвращает поле с ходом NPC
    """
    count = 0
    for i in game_list:
        if i != '-':
            count += 1
    # print(count)

    if count == 1:
        game_list = uns.first_step(game_list)
    elif count == 3:
        game_list = uns.two_step(game_list, last_step_user)
    elif count == 5:
        uns.three_step(game_list)
    elif count == 7:
        uns.four_step(game_list)

    return game_list


def check_win(game_list):
    """
    Проверка на предмет выигрыша
    :param game_list:
    :return:
    """
    game_ower = False

    all_win_option = uns.all_option()
    list_step_user = [item for item, value in enumerate(game_list) if value == 'X']
    for option in all_win_option:
        if option == list_step_user:
            print()
            print('X - win')
            game_ower = True
    return game_ower



