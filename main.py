import pygame
import pandas
import consts
import game_field

state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "direction": ""
}

def main():
    pygame.init()

    while state["is_window_open"]:
        handle_user_events()

        move_to()


def handle_user_events():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            direction = event.key
            if direction == pygame.K_LEFT: #move to left
                state["direction"] = consts.LEFT

            elif direction == pygame.K_RIGHT: #move to right
                state["direction"] = consts.RIGHT

            elif direction == pygame.K_UP: #move up
                state["direction"] = consts.UP

            elif direction == pygame.K_DOWN: #move down
                state["direction"] = consts.DOWN


def move_to():
    direction = state["direction"]
    if not direction:
        return
    res = game_field.set_location(direction)
    state["direction"] = ""
    if res == consts.LOSE_STATE:
        state["state"] = consts.LOSE_STATE
    elif res == consts.WIN_STATE:
        state["state"] = consts.WIN_STATE

