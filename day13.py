import numpy as np

with open("day13.txt") as f:
    data = f.read().split("\n\n")

coords = [[int(x) for x in y.split(",")] for y in data[0].split("\n")]
directions = [[x for x in y.split(" ")] for y in data[1].split("\n")]
dirs = list()
for a, b, c in directions:
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
    for j, g in new_coords:
        c.append([j, g])
    return c

def fold_left(x):
    new_coords = set()
    for i in range(0, len(coords)):
        if coords[i][0] > x:
            new_cord = abs(coords[i][0] - (x * 2))
            coords[i][0] = new_cord
        new_coords.add((coords[i][0], coords[i][1]))
    c = list()
    for j, g in new_coords:
        c.append([j, g])
    return c

for i in dirs:
    num = i[1]
    if i[0] == "x":
        coords = fold_left(num)
    else:
        coords = fold_up(num)
    if i == dirs[0]:
        print("Part 1:", len(coords))

a = max([x for x, _ in coords])
b = max([y for _, y in coords])

grid = np.zeros(shape=(b + 1, a + 1))

for x, y in coords:
    grid[y][x] = 1

print(grid)
print("Part 2: Whatever letters you see in the grid.")