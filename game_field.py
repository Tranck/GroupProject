import consts
import random
import Soldier

field = [[consts.EMPTY_CELL for col in range(consts.BOARD_COLS)] for row in range(consts.BOARD_ROWS)]

def build_field():
    global field

    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS

    #start soldier pos
    for row in range(consts.SOLDIER_ROWS):
        for col in range(1, 1 + consts.SOLDIER_COLS):
            field[row][col] = consts.SOLDIER_CELL

    #define random place for bombs
    for bomb in range(consts.BOMBS_AMOUNT):
        rnd_place_bomb_r = random.randint(0, consts.BOARD_ROWS - 1)
        rnd_place_bomb_c = random.randint(0, consts.BOARD_COLS - 1)
        while field[rnd_place_bomb_r][rnd_place_bomb_c] == consts.SOLDIER_CELL or \
            field[rnd_place_bomb_r][rnd_place_bomb_c] == consts.BOMB_CELL or \
                field[rnd_place_bomb_r][rnd_place_bomb_c] == consts.FLAG_CELL or \
                rnd_place_bomb_c + consts.BOMB_LEN >= consts.BOARD_COLS:
            rnd_place_bomb_r = random.randint(0, consts.BOARD_ROWS - 1)
            rnd_place_bomb_c = random.randint(0, consts.BOARD_COLS - 1)
        consts.bomb_list.append((rnd_place_bomb_r, rnd_place_bomb_c))

    #after fill bomb list, place them in grid
    for bomb in consts.bomb_list:
        for col in range(bomb[1], bomb[1] + consts.BOMB_LEN):
            field[bomb[0]][col] = consts.BOMB_CELL

    #fill flag position
    for row in range(flag_row, consts.BOARD_ROWS):
        for col in range(flag_col, consts.BOARD_COLS):
            field[row][col] = consts.FLAG_CELL


def set_location(direction):
    head = Soldier.soldier_head()

    new_head_location = check_cell(head[0], head[1], direction)
<<<<<<< HEAD
    if Soldier.border(new_head_location):
        for row in range(new_head_location[0] + consts.SOLDIER_BODY_ROWS, new_head_location[0], - 1):
            for col in range(new_head_location[1], new_head_location[1] + consts.SOLDIER_COLS):
                if field[row][col] == consts.BOMB_CELL:
                    return False
                elif field[row][col] == consts.FLAG_CELL:
                    return True
                elif field[row][col] == consts.EMPTY_CELL:
                    field[row][col] = consts.SOLDIER_CELL
                    field[head[0]][head[1]] = consts.EMPTY_CELL
                    field[head[0]][head[1] + 1] = consts.EMPTY_CELL
    else:
        print("Out of board")
=======

    if not Soldier.border(new_head_location):
        print("Out of board")
        return None

    height = consts.SOLDIER_ROWS
    width = consts.SOLDIER_COLS
    
    new_cells = [(row, col)
                 for row in range(new_head_location[0], new_head_location[0] + height)
                 for col in range(new_head_location[1], new_head_location[1] + width)]

    old_cells = [(row, col)
                 for row in range(head[0], head[0] + height)
                 for col in range(head[1], head[1] + width)]

    for row, col in new_cells:
        if field[row][col] == consts.BOMB_CELL:
            return consts.LOSE_STATE
        elif field[row][col] == consts.FLAG_CELL:
            return consts.WIN_STATE

    for row, col in old_cells:
        field[row][col] = consts.EMPTY_CELL

    for row, col in new_cells:
        field[row][col] = consts.SOLDIER_CELL
>>>>>>> main

    return None


def check_cell(row, col, direction):
    if direction == consts.DOWN:
        return row + 1, col
    elif direction == consts.UP:
        return row - 1, col
    elif direction == consts.LEFT:
        return row, col - 1
    elif direction == consts.RIGHT:
        return row, col + 1

    return None
