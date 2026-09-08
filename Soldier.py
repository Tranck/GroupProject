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
def soldier_feet(head):
    return head[0] + consts.SOLDIER_BODY_ROWS, head[1] + consts.SOLDIER_COLS


def border(head):
    foot = soldier_feet(head)
    if foot[0] < consts.BOARD_ROWS and foot[1] < consts.BOARD_COLS:
        return True
    elif head[0] < consts.BOARD_ROWS and foot[1] < consts.BOARD_COLS:
        return True
    return False



