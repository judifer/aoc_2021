from collections import deque
from collections import defaultdict

with open("day9.txt") as f:
    data = [[int(j) for j in i.strip()] for i in f.readlines()]

riskpoints = 0
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        b = data[y][x]
        smallercnt = 0
        if x < (len(data[y]) - 1):
            a = data[y][x + 1]
            if a < b or a == b:
                smallercnt += 1
        if x > 0:
            a = data[y][x - 1]
            if a < b or a == b:
                smallercnt += 1
        if y < (len(data) - 1):
            a = data[y + 1][x]
            if a < b or a == b:
                smallercnt += 1
        if y > 0:
            a = data[y - 1][x]
            if a < b or a == b:
                smallercnt += 1
        if smallercnt == 0:
            riskpoints += (b + 1)        
        
print("Part 1:", riskpoints)

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] != 9:
            data[y][x] = 0

basin_sizes = list()

def find_basins(grid, y, x):
    basin = 0
    if grid[y][x] == 0:
        grid[y][x] = 1
        basin = 1
        if x < (len(grid[y]) - 1):
            basin += find_basins(grid, y, x + 1)
        if x > 0:
            basin += find_basins(grid, y, x - 1)
        if y < (len(grid) - 1):
            basin += find_basins(grid, y + 1, x)
        if y > 0:
            basin += find_basins(grid, y - 1, x)
    return basin

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        basin_sizes.append(find_basins(data, y, x))

basin_sizes.sort()
a, b, c = basin_sizes[-3:]
print("Part 2:", a * b * c)