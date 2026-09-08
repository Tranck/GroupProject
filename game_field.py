import consts
import random

field = []

def build_field():
    global field

    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS

    #start soldier pos
    for row in range(consts.SOLDIER_ROWS):
        for col in range(1, consts.SOLDIER_COLS):
            field[row][col] = consts.SOLDIER_CELL

    #define random place for bombs
    for bomb in range(consts.BOMBS_AMOUNT):
        rnd_place_bomb_r = random.randint(0, consts.BOARD_ROWS - 1)
        rnd_place_bomb_c = random.randint(0, consts.BOARD_COLS - 1)
        while field[rnd_place_bomb_r][rnd_place_bomb_c] == consts.SOLDIER_CELL or \
            field[rnd_place_bomb_r][rnd_place_bomb_c] == consts.BOMB_CELL:
            rnd_place_bomb_r = random.randint(0, consts.BOARD_ROWS - 1)
            rnd_place_bomb_c = random.randint(0, consts.BOARD_COLS - 1)
        consts.bomb_list.append((rnd_place_bomb_r, rnd_place_bomb_c))

    #after fill bomb list, place them in grid
    for bomb in consts.bomb_list:
        for col in range(bomb[1], bomb[1] + consts.BOMB_LEN):
            field[bomb[0]][col] = consts.BOMB_CELL

    #fill flag pos
    for row in range(flag_row, consts.BOARD_ROWS):
        for col in range(flag_col, consts.BOARD_COLS):
            field[row][col] = consts.FLAG_CELL


