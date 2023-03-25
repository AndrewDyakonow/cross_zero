import utils

game_list = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
game = True

while game:
    utils.print_pole(game_list)
    x, y = utils.input_step()
    game_list[y][x] = 'X'
    utils.print_pole(game_list)
    utils.npc_step(game_list)
    utils.print_pole(game_list)

    game = False
