import pygame
import consts
import random
import time

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.GREEN)
objects = {} #loading all the images into here

def create_soldier():
    soldier_img = pygame.image.load(consts.SOLDIER_IMG).convert_alpha()
    size = (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)
    soldier_sized = pygame.transform.scale(soldier_img, size)
    return soldier_sized

def create_flag():
    flag = pygame.image.load(consts.FLAG_IMG).convert_alpha()
    size = (consts.FLAG_COLS * consts.CELL_SIZE,
            consts.FLAG_ROWS * consts.CELL_SIZE)
    flag_sized = pygame.transform.scale(flag, size)
    return flag_sized
def create_bomb():
    bomb = pygame.image.load(consts.BOMB_IMG).convert_alpha()
    size = (consts.MINE_COLS * consts.CELL_SIZE,
            consts.MINE_ROWS * consts.CELL_SIZE)
    bomb_sized = pygame.transform.scale(bomb,size)
    return bomb_sized
def create_grass():
    grass = pygame.image.load(consts.GRASS_IMG).convert_alpha()
    sized_grass = pygame.transform.scale(grass, consts.GRASS_SIZE)
    return sized_grass
def create_night_soldier():
    night_soldier = pygame.image.load(consts.NIGHT_SOLDIER_IMG).convert_alpha()
    size = (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)
    night_sized = pygame.transform.scale(night_soldier, size)
    return night_sized

objects["soldier"] = create_soldier()
objects["flag"] = create_flag()
objects["bomb"] = create_bomb()
objects["grass"] = create_grass()
objects["night_soldier"] = create_night_soldier()




def place_grass():
    #making a list of unique coordinates to place the grass
    while len(consts.grass_place) < consts.GRASS_COUNT:
        x = random.randrange(0, consts.BOARD_COLS, consts.GRASS_COLS)
        y = random.randrange(0, consts.BOARD_ROWS-1, consts.GRASS_ROWS)
        if (x,y) not in consts.grass_place and (x,y) not in consts.bomb_list:
            consts.grass_place.append((x,y))
    #blit-ing the grass into the board
    for item in consts.grass_place:
        place = (item[0] * consts.CELL_SIZE, item[1] * consts.CELL_SIZE)
        screen.blit(objects["grass"],place)
def show_grass():
    #returning grass after night mode
    for item in consts.grass_place:
        place = (item[0] * consts.CELL_SIZE, item[1] * consts.CELL_SIZE)
        screen.blit(objects["grass"],place)

def place_bombs():
    for place in consts.bomb_list:
        x = place[0] * consts.CELL_SIZE
        y = place[1] * consts.CELL_SIZE
        screen.blit(objects["bomb"],(x,y))
        pygame.display.update()

def place_soldier(x,y):
    x = x*consts.CELL_SIZE
    y = y*consts.CELL_SIZE
    screen.blit(objects["soldier"],(x,y))

def night_background():
    for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            screen.fill(consts.BLACK, rect)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)


def night_mode(x,y):
    #the function gets the pos of the soldier and shows the bombs
    x = x*consts.CELL_SIZE
    y = y*consts.CELL_SIZE
    night_background()
    screen.blit(objects["night_soldier"],(x,y))
    place_bombs()
    time.sleep(consts.NIGHT_TIME)
    pygame.display.update()


def back_to_day(x,y):
    #returns the board to regular mode
    screen.fill(consts.GREEN)
    show_grass()
    place_soldier(x,y)


def pixel_place(pixel_x,pixel_y):
    screen.blit(objects["soldier"],(pixel_x,pixel_y))

def move_down(x,y):
    x_pixel = x*consts.CELL_SIZE
    y_pixel = (y-1)*consts.CELL_SIZE
    while y_pixel <y *consts.CELL_SIZE:
        pixel_place(x_pixel, y_pixel)
        pygame.display.update()
        screen.fill(consts.GREEN)
        show_grass()
        y_pixel += consts.SOLDIER_STEP
        time.sleep(consts.SOLDIER_PACE)

def move_up(x,y):
    x_pixel = x*consts.CELL_SIZE
    y_pixel = (y+1)*consts.CELL_SIZE
    while y_pixel >y *consts.CELL_SIZE:
        pixel_place(x_pixel, y_pixel)
        pygame.display.update()
        screen.fill(consts.GREEN)
        show_grass()
        y_pixel -= consts.SOLDIER_STEP
        time.sleep(consts.SOLDIER_PACE)

def move_right(x,y):
    x_pixel = (x-1)*consts.CELL_SIZE
    y_pixel = y*consts.CELL_SIZE
    while x_pixel <x *consts.CELL_SIZE:
        pixel_place(x_pixel, y_pixel)
        pygame.display.update()
        screen.fill(consts.GREEN)
        show_grass()
        x_pixel += consts.SOLDIER_STEP
        time.sleep(consts.SOLDIER_PACE)

def move_left(x,y):
    x_pixel = (x+1)*consts.CELL_SIZE
    y_pixel = y*consts.CELL_SIZE
    while x_pixel >x *consts.CELL_SIZE:
        pixel_place(x_pixel, y_pixel)
        pygame.display.update()
        screen.fill(consts.GREEN)
        show_grass()
        x_pixel -= consts.SOLDIER_STEP
        time.sleep(consts.SOLDIER_PACE)


place_grass()
c = 1
while True:
    if c == 1:
        move_down(0, 1)
        c+=1
    place_soldier(0,1)
    if c == 2:
        move_right(1,1)
        c+=1
    place_soldier(1,1)
    if c == 3:
        move_left(0,1)
        c+=1
    place_soldier(0,1)
    if c == 4:
        move_up(0,0)
        c+=1
    place_soldier(0,0)



