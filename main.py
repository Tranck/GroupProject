import pygame
import pandas
import consts
import Soldier
import game_field
import Screen

state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True
}

def main():
    pygame.init()

    while state["is_window_open"]:
        handle_user_events()


def handle_user_events():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            direction = event.key
            if (direction == pygame.K_LEFT):
                soldier_predict_location = Soldier.set_location(row, col, direction)
                if Soldier.border(soldier_predict_location):
                    game_field.place_soldier(soldier_predict_location)

            elif (direction == pygame.K_RIGHT):
                soldier_predict_location = Soldier.set_location(row, col, direction)
                if Soldier.border(soldier_predict_location):
                    game_field.place_soldier(soldier_predict_location)

            elif (direction == pygame.K_UP):
                soldier_predict_location = Soldier.set_location(row, col, direction)
                if Soldier.border(soldier_predict_location):
                    game_field.place_soldier(soldier_predict_location)

            elif (direction == pygame.K_DOWN):
                soldier_predict_location = Soldier.set_location(row, col, direction)
                if Soldier.border(soldier_predict_location):
                    game_field.place_soldier(soldier_predict_location)


