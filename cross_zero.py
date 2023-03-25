import utils

game_list = ['-' for x in range(9)]
game = True

utils.print_pole(game_list)

while game:

    x = utils.input_step(game_list)
    game_list[x] = 'X'
    utils.print_pole(game_list)
    if utils.check_win(game_list):
        break
    utils.npc_step(game_list, x)
    utils.print_pole(game_list)


