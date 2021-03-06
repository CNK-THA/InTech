import copy
import time

"""
Last Modified: 31/10/2020
Editor: Chanon Kachorn.
InTech IT Online Class

This file is a 10x10 maze game. User can choose to play the game themself or let the AI play the game.

"""

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

class Node:
    def __init__(self, current_map): #constructor
        self.current_map = current_map
        self.current_position = None
        self.previous_position = None
        self.child = [] #all possible positions that we can go to (up/down/left/right)
        self.parent = None
        self.action = None
        self.find_player()

<<<<<<< .mine
    def add_child(self, circle):
        self.child.append(circle)
||||||| .r3
=======
#DECLARING VARIABLES OF THE PLAYER
current_position = (4,4) #index from 0! #Y AXIS FIRST
previous_position = (4,4) #previous position of the player
level = 1 #which level are we on
>>>>>>> .r7

<<<<<<< .mine
    def display_map(self):
        for i in range(0, len(self.current_map)):
            for k in range(0, len(self.current_map[0])):
                print(self.current_map[i][k], end='')
            print()

    def find_player(self):
        for row in range(0, len(self.current_map)):
            for column in range(0, len(self.current_map[0])):
                if self.current_map[row][column] == 'p': #if this position is the player
                    self.current_position = (row, column)
                    self.previous_position = (row,column)
                    return 0 #exit from the function


    def check_collision(self, position):
        if self.current_map[position[0]][position[1]] == 'x':
            print('we hit a wall!!')
            return -1
        return 1
        
        
    def check_win(self, position):
        if self.current_map[position[0]][position[1]] == 'f':
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
                self.current_map[new_position[0]][new_position[1]] = 'p'
                self.current_map[self.current_position[0]][self.current_position[1]] = ' '
                return True
            self.current_map[new_position[0]][new_position[1]] = 'p'
            self.current_map[self.current_position[0]][self.current_position[1]] = ' '
            self.current_position = new_position
            return False
        return None #collide with sth

    def __eq__(self, another):
        return another != None and self.current_position == another.current_position
    def __hash__(self):
        return hash(self.current_position)











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
        current_position = previous_position #hit a wall so  we return to the previous position
    else:
        if map1[current_position[0]][current_position[1]] == 'f': #check have we reach the flag yet
            map1[current_position[0]][current_position[1]] = 'p' #set new position to be the player
            map1[previous_position[0]][previous_position[1]] = ' ' #set prvious position to be empty space
            print('we made it!')
            return True
        map1[current_position[0]][current_position[1]] = 'p' #move the player to the next position
        map1[previous_position[0]][previous_position[1]] = ' '


option = int(input("Press 1 to play or press 2 for AI: "))
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
            else: #Once finish all levels we end the program
                break
            find_player()
else: #AI mode
    mapToPlay = map2 #CHANGE THIS FOR EACH LEVEL YOU WANT IT TO PLAY
    print('AI is playing....')
    AI = Node(mapToPlay)
    AI.display_map()

    toVisit = [] ##stores list of nodes that has NOT been EXPANDED yet
    toVisit.append(AI)
    visited = set() #stores list of nodes that HAS ALREADY been EXPANDED
    solution = []

    while len(solution) == 0: #keep expanding more child nodes
        current = toVisit.pop(0) #the first one
        visited.add(current)

        for action in ['w','s','a','d']:
            newChild = Node(copy.deepcopy(current.current_map))
            status = newChild.move_player(action) #did we hit a wall or reach the flag?
            newChild.parent = current

            if status != None: #comment out these two lines if don't want to see AI playing
                newChild.display_map()
        
            if status == True:
                print('found solution')
                while newChild.action != None:
                    solution.append(newChild.action)
                    newChild = newChild.parent
                solution.reverse()
                break #out of for loop

            elif status == None: #invalid movement aka hit a wall, or some error happens so skip
                continue

            else: #False, we have not reach the flag and didn't hit a wall, keep playing
                if newChild not in visited:
                    current.add_child(newChild)
                    toVisit.append(newChild)

    #SHOW RESULT OF AI PLAYING
    root = Node(mapToPlay)
    for action in solution:
        root.display_map()
        root.move_player(action)
        time.sleep(0.5)
        





























||||||| .r3
=======
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
        




























>>>>>>> .r7
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
        

        

<<<<<<< .mine
||||||| .r3
       
#USER PLAY MODE       
##root = Tree(map1, (4,4))
##root.display_map()
##while True:
##    move = input()
##    if root.move_player(move):
##        root.display_map()
##        break
##    root.display_map()
=======
       
#USER PLAY MODE       
# root = Tree1(map1, (4,4))
# root.display_map()
# while True:
#    move = input()
#    if root.move_player(move):
#        root.display_map()
#        break
#    root.display_map()
>>>>>>> .r7


    
        

