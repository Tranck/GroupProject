import pygame
import pandas

import consts
import Soldier
import game_field
import Screen

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
                state["direction"] = "left"

            elif direction == pygame.K_RIGHT: #move to right
                state["direction"] = "right"

            elif direction == pygame.K_UP: #move up
                state["direction"] = "up"

            elif direction == pygame.K_DOWN: #move down
                state["direction"] = "down"


def move_to():
    direction = state["direction"]
    if not game_field.set_location(direction):
        state["state"] = consts.LOSE_STATE
    elif game_field.set_location(direction):
        state["state"] = consts.WIN_STATE
    else:
        game_field.set_location(direction)

