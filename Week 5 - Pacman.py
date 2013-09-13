import copy
import time

def move(char):
    global points
    x, y = pacman()
    a, b = key[char]
    # updated x and y coordinates
    xu, yu = x + a, y + b
    if maze[yu][xu] == '#':
        return
    if maze[yu][xu] == 'G':
        return
    maze[y][x] = ' '
    original[y][x] = ' '
    if maze[yu][xu] == '.':
        points += 1
    maze[yu][xu] = 'P'

def won():
    for line in maze:
        if '.' in line:
            return False
    return True

def getPaths(pac):
    # Get coords of all the ghosts
    shortestPaths = []
    for lineNum, line in enumerate(maze):
        for index, char in enumerate(line):
            if char == "G":
                if original[lineNum][index] == '.':
                    maze[lineNum][index] = "."
                else:
                    maze[lineNum][index] = ' '
                shortestPaths.append(next(index, lineNum, pac))

    for moveTo, lineNum in shortestPaths:
        maze[lineNum][moveTo] = "G"

def pacman():
    for lineNum, line in enumerate(maze):
        if 'P' in line:
            return (line.index('P'), lineNum)

def output():
    print("Points:", points)
    for line in maze:
        print(''.join(line))

def next(index, lineNum, pac):
    visited = [[False] * columnLen for x in range(rowLen)]
    x, y = index, lineNum
    toDo = [(x, y - 1, (x, y - 1)), # up\
            (x - 1, y, (x - 1, y)), # left\
            (x, y + 1, (x, y + 1)), # down\
            (x + 1, y, (x + 1, y))] # right
    path = []
    while toDo:
        x, y, init = toDo.pop(0)
        if x < 0 or x >= columnLen or y >= rowLen or y < 0:
            continue

        if maze[y][x] == "#":
            continue

        if visited[y][x]:
            continue

        visited[y][x] = True
        if (x, y) == pac:
            path = init
            break

        for toFill in [(x, y - 1, init), (x - 1, y, init), (x, y + 1, init), (x + 1, y, init)]:
            toDo.append(toFill)

    return path

key = {}
key['U'] = (0, -1)
key['D'] = (0, 1)
key['L'] = (-1, 0)
key['R'] = (1, 0)

maze = [list(line.strip()) for line in open('maze.txt', 'r')]
original = copy.deepcopy(maze)
rowLen = len(maze)
columnLen = len(maze[0])
start = time.clock()
commands = input("Commands: ").split()
points = 0
for c in commands:
    if won():
        print('You won!')
        output()
        break
    if c == 'O':
        output()
        continue
    # location of pacman before he moves
    pac = pacman()
    move(c)
    getPaths(pac)
    if not pacman():
        print('You died!')
        output()
        break
else:
    if won():
        print('You won!')
    output()
print(time.clock() - start)