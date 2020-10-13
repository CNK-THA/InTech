map = [
    ['x','x','x','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ',' ','x',' ','f','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x',' ','x',' ',' ','x'],
    ['x',' ',' ','x','p',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x'],
]

current_position = (4,4) #index from 0!
previous_position = (4,4)

def display_map():
    for i in range(0, len(map)):
        for k in range(0, len(map[0])):
            print(map[i][k], end='')
        print()


def move_player():
    global current_position #say that we want to refer to the one above!
    if map[current_position[0]][current_position[1]] == 'x':
        print('we hit a wall!!')
        current_position = previous_position
    else:
        if map[current_position[0]][current_position[1]] == 'f':
            map[current_position[0]][current_position[1]] = 'p'
            map[previous_position[0]][previous_position[1]] = ' '
            print('we made it!')
            return True
        map[current_position[0]][current_position[1]] = 'p'
        map[previous_position[0]][previous_position[1]] = ' '
        




while True:
    display_map()
    move = input()
    finish = False
    if move == 'w':
        previous_position = current_position
        current_position = (current_position[0] - 1, current_position[1])
        finish = move_player()
    elif move == 's':
        previous_position = current_position
        current_position = (current_position[0] + 1, current_position[1])
        finish = move_player()
    elif move == 'a':
        previous_position = current_position
        current_position = (current_position[0], current_position[1] - 1)
        finish = move_player()
    elif move == 'd':
        previous_position = current_position
        current_position = (current_position[0], current_position[1] + 1)
        finish = move_player()
    else:
        print('invalid key!')

    if finish == True:
        break


    


