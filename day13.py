import numpy as np

with open("day13.txt") as f:
    data = f.read().split("\n\n")

coords = [[int(x) for x in y.split(",")] for y in data[0].split("\n")]
directions = [[x for x in y.split(" ")] for y in data[1].split("\n")]
dirs = list()
for i in directions:
    a, b, c = i
    d, e = c.split("=")
    dirs.append([d, int(e)])

def fold_up(x):
    new_coords = set()
    for i in range(0, len(coords)):
        if coords[i][1] > x:
            new_cord = abs(coords[i][1] - (x * 2))
            coords[i][1] = new_cord
        new_coords.add((coords[i][0], coords[i][1]))
    c = list()
    for j in new_coords:
        c.append([j[0], j[1]])
    return c

def fold_left(x):
    new_coords = set()
    for i in range(0, len(coords)):
        if coords[i][0] > x:
            new_cord = abs(coords[i][0] - (x * 2))
            coords[i][0] = new_cord
        new_coords.add((coords[i][0], coords[i][1]))
    c = list()
    for j in new_coords:
        c.append([j[0], j[1]])
    return c

new_coords = set()

for i in dirs:
    num = i[1]
    if i[0] == "x":
        coords = fold_left(num)
    else:
        coords = fold_up(num)
    if i == dirs[0]:
        print("Part 1:", len(coords))

max_x = list()
max_y = list()
for i in coords:
    max_x.append(i[0])
    max_y.append(i[1])

a = max(max_x)
b = max(max_y)

grid = np.zeros(shape=(b + 1, a + 1))

for i in coords:
    x = i[0]
    y = i[1]
    grid[y][x] = 1

print(grid)
print("Part 2: Whatever letters you see in the grid.")