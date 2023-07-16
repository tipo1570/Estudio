# MAZE 2.0
import os

import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 20

MY_POSITION = [9, 7]

while True:

    # MAZE 1.0

    POS_X = 0
    POS_Y = 1

    MAP_WIDTH = 20
    MAP_HEIGHT = 20

    MY_POSITION = [10, 10]

    print("+" + "_" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_HEIGHT):
            if MY_POSITION[POS_X] == coordinate_x and MY_POSITION[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "_" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    if direction == "w" or "w":
        MY_POSITION[POS_Y] -= 1

    elif direction == "s" or "S":
        MY_POSITION[POS_Y] += 1

    elif direction == "a" or "A":
        MY_POSITION[POS_X] -= 1

    elif direction == "d" or "D":
        MY_POSITION[POS_X] += 1

    elif direction == "q" or "Q":
        break

    os.system("cls")
