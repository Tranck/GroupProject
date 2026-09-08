import consts
import game_field

def soldier_head(row, col):
    return game_field.field[row][col] == consts.SOLDIER_CELL


def soldier_feet(row, col):
    return (row + 3, col), (row + 3, col + 1)


def border(new_location): #[0] - row, [1] - col
    if new_location[0] == consts.BOARD_ROWS or new_location[1] == consts.BOARD_COLS:
        return False
    return True


def set_location(row, col, direction):
    if direction == consts.DOWN:
        return (row + 1, col)
    elif direction == consts.UP:
        return (row - 1, col)
    elif direction == consts.LEFT:
        return (row, col - 1)
    elif direction == consts.RIGHT:
        return (row, col + 1)

    return None


