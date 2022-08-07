import readchar
import random
from os import system
system("cls")

POS_X = 0
POS_Y = 0
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
   #########################
                        ####
###                     ####
######################  ####
######################  ####    
###################    #####
###############        #####
########          ##########
###############        #####
#####################  #####
###############        #####
#########        ###########
#########  #################
#########  #################
############################\
"""

my_position = [POS_X, POS_Y]
tail_length = 0
tail = []
direction = " "

# Generate random objects on the map
map_objects = []

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGH = len(obstacle_definition)

while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0,MAP_WIDTH-1),random.randint(0,MAP_HEIGH-1)]
    if new_position not in map_objects and new_position != my_position and \
            obstacle_definition[new_position[1]][new_position[0]] != "#":
        map_objects.append(new_position)

def mapping(tail,tail_length,direction,my_position):
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
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end = "")
        print("|")
    print("+"+ "-" * MAP_WIDTH * 3 + "+")
    return(tail_length)

while True:
    tail_length=mapping(tail,tail_length,direction,my_position)
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
    new_position = None
    if direction == "w":
        new_position = [my_position[0], (my_position[1] - 1) % MAP_WIDTH]
    elif direction == "s":
        new_position = [my_position[0], (my_position[1] + 1) % MAP_WIDTH]
    elif direction == "a":
        new_position = [(my_position[0]-1) % MAP_WIDTH, my_position[1]]
    elif direction == "d":
        new_position = [(my_position[0]+1) % MAP_WIDTH, my_position[1]]
    elif direction == "p":
        system("cls")
        print("Thanks for playing!\n\n\n")
        break
    if new_position:
        if obstacle_definition[new_position[1]][new_position[0]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position