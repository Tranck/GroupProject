import consts
import game_field

#return left_upper head
def soldier_head():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if game_field.field[row][col] == consts.SOLDIER_CELL:
                return row, col
    return None


<<<<<<< HEAD
=======

>>>>>>> main
#return left_foot
def soldier_feet(head):
    return head[0] + consts.SOLDIER_BODY_ROWS, head[1] + consts.SOLDIER_COLS


def border(head):
<<<<<<< HEAD
    foot = soldier_feet(head)
    if foot[0] < consts.BOARD_ROWS and foot[1] < consts.BOARD_COLS:
        return True
    elif head[0] < consts.BOARD_ROWS and foot[1] < consts.BOARD_COLS:
=======
    height = consts.SOLDIER_ROWS
    width = consts.SOLDIER_COLS
    if head[0] < 0 or head[1] < 0:
        return False
    if head[0] + height > consts.BOARD_ROWS or head[1] + width > consts.BOARD_COLS:
        return False
    if head[0] + height < consts.BOARD_ROWS and head[1] + width < consts.BOARD_COLS:
>>>>>>> main
        return True
    return False



