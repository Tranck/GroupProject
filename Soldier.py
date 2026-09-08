import consts
import game_field

#return left_upper head
def soldier_head():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if game_field.field[row][col] == consts.SOLDIER_CELL:
                return row, col
    return None


#return left_foot
def soldier_feet():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if game_field.field[row][col] == consts.SOLDIER_CELL:
                return consts.SOLDIER_BODY_ROWS + row, col
    return None


def border(new_location): #[0] - row, [1] - col
    if new_location[0] == consts.BOARD_ROWS or new_location[1] == consts.BOARD_COLS:
        return False
    return True



