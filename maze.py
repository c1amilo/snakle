import readchar
import random
from os import system
system("cls")

POS_X = 0
POS_Y = 0
MAP_WIDTH = 20
MAP_HEIGH = 20
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
############################
                        ####
######################  ####
######################  ####
###########                 
###################  #######
###############            #
########          ##########
###############             
#####################  #####
###############          ###
#########        ######     
#########  ############   ##
#########  ################ 
############################\
"""

my_position = [POS_X, POS_Y]
tail_length = 0
tail = []
direction = " "

# Generate random objects on the map
map_objects = []

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
print(obstacle_definition)

while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0,MAP_WIDTH-1),random.randint(0,MAP_HEIGH-1)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

def mapping(tail,tail_length,direction):
    system("cls")
    print("+"+ "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGH):
        print("|",end = "")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if coordinate_x == map_object[0] and coordinate_y == map_object[1]:
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[0] == coordinate_x  and tail_piece[1] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece
            if coordinate_x == my_position[0] and coordinate_y == my_position[1]:
                if direction == "w":
                    char_to_draw = "^"
                elif direction == "s":
                    char_to_draw = "v"
                elif direction == "a":
                    char_to_draw = "<"
                elif direction == "d":
                    char_to_draw = ">"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:
                    tail_length = -1
            print(" {} ".format(char_to_draw), end = "")
        print("|")
    print("+"+ "-" * MAP_WIDTH * 3 + "+")
    return(tail_length)

while True:
    tail_length=mapping(tail,tail_length,direction)
    if tail_length == -1:
        system("cls")
        print("You dead!")
        break
    elif tail_length == NUM_OF_MAP_OBJECTS:
        system("cls")
        print("You won!")
        break
    # Ask user where he wants to move
    direction = readchar.readchar().decode()
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[1] -= 1
        my_position[1] %= MAP_HEIGH
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[1] += 1
        my_position[1] %= MAP_HEIGH
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[0] -= 1
        my_position[0] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[0] += 1
        my_position[0] %= MAP_WIDTH
    elif direction == "p":
        system("cls")
        print("Thanks for playing!\n\n\n")
        break