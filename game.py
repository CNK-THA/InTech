import copy
import time

map1 = [
    ['x','x','x','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ',' ','x',' ','f','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x',' ','x',' ',' ','x'],
    ['x',' ',' ','x','p',' ','x',' ',' ','x'],
    ['x',' ',' ','x','x','x','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x'],
]





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
##root = Tree(map1, (4,4))
##root.display_map()
##while True:
##    move = input()
##    if root.move_player(move):
##        root.display_map()
##        break
##    root.display_map()



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

        
    
        

