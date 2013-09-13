shortestPaths = []
def next(index, lineNum):
    visited = [[False] * columnLen for x in range(rowLen)]
    x, y = index, lineNum
    toDo = [(x, y - 1, (x, y - 1)), # up\
            (x - 1, y, (x - 1, y)), # left\
            (x, y + 1, (x, y + 1)), # down\
            (x + 1, y, (x + 1, y))] # right

    while toDo:
        x, y, init = toDo.pop(0)

        if x < 0 or x >= columnLen or y >= rowLen or y < 0:
            continue

        if maze[y][x] == "#":
            continue

        if visited[y][x]:
            continue

        visited[y][x] = True

        if maze[y][x] == "P":
            shortestPaths.append(init)
            break

        for toFill in [(x, y - 1, init), (x - 1, y, init), (x, y + 1, init), (x + 1, y, init)]:
            toDo.append(toFill)

maze = [list(line.strip()) for line in open('maze.txt', 'r')]
rowLen = len(maze)
columnLen = len(maze[0])

# Get coords of all the ghosts and pacman himself
for lineNum, line in enumerate(maze):
    for index, char in enumerate(line):
        if char == "G":
            maze[lineNum][index] = " "
            next(index, lineNum)

# Move the "G"s to where they're supposed to go
for moveTo, lineNum in shortestPaths:
    maze[lineNum][moveTo] = "G"

for line in maze:
    print(''.join(line))