import numpy as np

with open("day5.txt") as f:
    data = [x.replace(" -> ", ",").strip().split(",") for x in f.readlines()]

for x in range(0, len(data)):
    for y in range(0, len(data[x])):
        data[x][y] = int(data[x][y])

size = max([item for sublist in data for item in sublist])

grid = np.zeros(shape=(size + 1, size + 1))

for i in data:
    x1, y1, x2, y2 = i
    if x1 == x2:
        if y1 < y2:
            for j in range(y1, y2 + 1):
                grid[x1][j] += 1
        else:
            for j in range(y2, y1 + 1):
                grid[x1][j] += 1
    elif y1 == y2:
        if x1 < x2:
            for j in range(x1, x2 + 1):
                grid[j][y2] += 1
        else:
            for j in range(x2, x1 + 1):
                grid[j][y2] += 1

cunt = 0

for i in grid:
    for j in i:
        if j > 1:
            cunt += 1

print("Part one:", cunt)

for line in data:
    x1, y1, x2, y2 = line
    if x1 != x2 and y1 != y2:
        if x1 < x2:
            if y1 < y2:
                while x1 <= x2:
                    grid[x1][y1] += 1
                    x1 += 1
                    y1 += 1
            else:
                while x1 <= x2:
                    grid[x1][y1] += 1
                    x1 += 1
                    y1 -= 1
        else:
            if y1 < y2:
                while x1 >= x2:
                    grid[x1][y1] += 1
                    x1 -= 1
                    y1 += 1
            else:
                while x1 >= x2:
                    grid[x1][y1] += 1
                    x1 -= 1
                    y1 -= 1

cunt = 0

for i in grid:
    for j in i:
        if j > 1:
            cunt += 1

print("Part two:", cunt)