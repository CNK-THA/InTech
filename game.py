import copy
import time

map1 = [
    ['x','x','x','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ',' ','x',' ','f','x'],
    ['x',' ',' ',' ','x',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x',' ','x',' ','p','x'],
    ['x',' ',' ','x',' ',' ','x',' ',' ','x'],
    ['x',' ','x','x','x','x','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x'],
]

map2 = [
    ['x','x','x','x','x','x','x','x','x','x'],
    ['x','p',' ',' ',' ',' ','x',' ','f','x'],
    ['x',' ',' ',' ','x',' ','x',' ','x','x'],
    ['x',' ',' ','x','x','x','x',' ',' ','x'],
    ['x',' ',' ','x',' ',' ','x',' ',' ','x'],
    ['x',' ','x','x','x',' ',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ','x',' ',' ','x'],
    ['x',' ',' ','x',' ','x','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x'],
]

map3 = [
    ['x','x','x','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ',' ','x',' ','f','x'],
    ['x',' ',' ',' ','x',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x',' ','x',' ',' ','x'],
    ['x',' ',' ','x',' ','p','x',' ',' ','x'],
    ['x',' ','x','x','x','x','x',' ',' ','x'],
    ['x',' ','x',' ',' ',' ','x',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ',' ','x'],
    ['x',' ',' ',' ','x',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x'],
]


#DECLARING VARIABLES OF THE PLAYER
current_position = (4,4) #index from 0! #Y AXIS FIRST
previous_position = (4,4) #previous position of the player
level = 1 #which level are we on

def find_player():
    """
    Find current position of the player.

    Returns: 0 if it is sucessfully found, None otherwise
    """
    global current_position, previous_position
    for row in range(0, len(map1)):
        for column in range(0, len(map1[0])):
            if map1[row][column] == 'p': #if this position is the player
                current_position = (row, column)
                previous_position = (row,column)
                return 0 #exit from the function
            

def display_map():
    """
    Display the game map to the screen.
    """
    for row in range(0, len(map1)): #for all rows
        for column in range(0, len(map1[0])): #for all column
            print(map1[row][column], end='')
        print()

def move_player():
    """
    Handle moving player in different directions. If it collides with a wall then remain
    at the same position otherwise move to the new position. Also check if we have reach the flag.

    Returns: True if we have reached the flag. None otherwise.
    """
    global current_position #say that we want to refer to the one above!
    if map1[current_position[0]][current_position[1]] == 'x':
        print('we hit a wall!!')
        current_position = previous_position
    else:
        if map1[current_position[0]][current_position[1]] == 'f':
            map1[current_position[0]][current_position[1]] = 'p'
            map1[previous_position[0]][previous_position[1]] = ' '
            print('we made it!')
            return True
        map1[current_position[0]][current_position[1]] = 'p'
        map1[previous_position[0]][previous_position[1]] = ' '


option = input("Press 1 to play or press 2 for AI: ")
if option == 1: #WE want to play the game
    find_player()
    while True: #it's not game over yet
        display_map()
        move = input() #get user movement
        finish = False #we haven't win the ggame yet
        if move == 'w': #MOVE FORWARD
            previous_position = current_position
            current_position = (current_position[0] - 1, current_position[1])
            finish = move_player()
        elif move == 's': #MOVE DOWN
            previous_position = current_position
            current_position = (current_position[0] + 1, current_position[1])
            finish = move_player()
        elif move == 'a': #MOVE LEFT
            previous_position = current_position
            current_position = (current_position[0], current_position[1] - 1)
            finish = move_player()
        elif move == 'd': #MOVE RIGHT
            previous_position = current_position
            current_position = (current_position[0], current_position[1] + 1)
            finish = move_player()
        else: #ERROR
            print('invalid key!')

        if finish == True: #we have finished this level move on to the next level otherwise end the program
            level += 1
            if level == 2:
                map1 = map2
            elif level == 3:
                map1 = map3
            else:
                break
            find_player()
else: #AI mode
    print('AI is playing....') 
        




























class Tree1:
    def __init__(self, game_map, player_position):
        self.game_map = game_map
        self.child = []
        self.parent = None
        self.current_position = player_position #index from 0!
        self.action = None


    def add_child(self, t):
        self.child.append(t)
        

    def display_map(self):
        for i in range(0, len(self.game_map)):
            for k in range(0, len(self.game_map[0])):
                print(self.game_map[i][k], end='')
            print()

    def check_collision(self, position):
        if self.game_map[position[0]][position[1]] == 'x':
            print('we hit a wall!!')
            return -1
        return 1
        
        
    def check_win(self, position):
        if self.game_map[position[0]][position[1]] == 'f':
            print('we made it!')
            return True
        return False

    def move_player(self, action):
        new_position = None
        if action == 'w':
            new_position = (self.current_position[0] - 1, self.current_position[1])
        elif action == 's':
            new_position = (self.current_position[0] + 1, self.current_position[1])
        elif action == 'a':
            new_position = (self.current_position[0], self.current_position[1] - 1)
        elif action == 'd':
            new_position = (self.current_position[0], self.current_position[1] + 1)
        else:
            print('invalid key!')

        if self.check_collision(new_position) == 1:
            self.action = action
            if self.check_win(new_position):
                self.game_map[new_position[0]][new_position[1]] = 'p'
                self.game_map[self.current_position[0]][self.current_position[1]] = ' '
                return True
            self.game_map[new_position[0]][new_position[1]] = 'p'
            self.game_map[self.current_position[0]][self.current_position[1]] = ' '
            self.current_position = new_position
            

            return False
            
            
        return None #collide with sth
    def __eq__(self, another):
        return another != None and self.current_position == another.current_position
    def __hash__(self):
        return hash(self.current_position)
        

        

       
#USER PLAY MODE       
# root = Tree1(map1, (4,4))
# root.display_map()
# while True:
#    move = input()
#    if root.move_player(move):
#        root.display_map()
#        break
#    root.display_map()



#AUTO MODE
root = Tree1(map1, (4,4))
root.display_map()
toVisit = []
toVisit.append(root)

visited = set()


solution = []
while len(solution) == 0:
    current = toVisit.pop(0) #the first one
    visited.add(current)

    for action in ['w','s','a','d']:
        c = Tree1(copy.deepcopy(current.game_map), current.current_position)
        status = c.move_player(action)
        c.parent = current

        if status != None:
            c.display_map()
        
        if status == True:
            print('found solution')
            while c.action != None:
                solution.append(c.action)
                c = c.parent
            solution.reverse()
            break #out of for loop

        elif status == None: #invalid so skip
            continue
        else: #False
            if c not in visited:
                current.add_child(c)
                toVisit.append(c)

        
root = Tree1(map1, (4,4))

for action in solution:
    root.display_map()
    root.move_player(action)
    time.sleep(0.5)

        
    
        

