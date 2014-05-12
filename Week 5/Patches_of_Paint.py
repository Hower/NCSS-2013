import time
def fill(d, e):

    toDo = [(d, e)]
    while toDo:
        x, y = toDo.pop()
        if y < 0 or y >= rowCount or x < 0 or x >= columnCounts[y]:
            continue
        if grid[y][x] != '%':
            continue

        grid[y][x] = '.'

        for a, b in (x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y), \
                    (x + 1, y + 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y - 1):
            toDo.append((a, b))
h = time.clock()
grid = [list(line.strip()) for line in open('patches.txt', 'r')]
rowCount = len(grid)

columnCounts = []
for row in grid:
    columnCounts.append(len(row))

count = 0

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '%':
            fill(x, y)
            count += 1

print(count, "patches" if count != 1 else "patch")
print(time.clock() - h)