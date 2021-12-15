import numpy as np
import matplotlib.pyplot as plt

with open("day11.txt") as f:
    data = [[int(x) for x in y.strip()] for y in f]

data = np.pad(data, pad_width=1, constant_values=100)
# print(data)

neighbours = dict()

def get_neighbours(y, x):
    neighbours = [(x + 1, y), (x -1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]
    global flashes
    flashes += 1
    data[y][x] = 0
    for i in neighbours:
        nx, ny = i
        if data[ny][nx] == 100:
            continue
        elif data[ny][nx] == 0:
            continue
        else:
            data[ny][nx] += 1
            if data[ny][nx] >= 10:
                data[ny][nx] = data[ny][nx] % 10
                get_neighbours(ny, nx)
    return

def print_map(l):
    l_del = l[1:-1, 1:-1]
    fig, axe = plt.subplots(dpi=300)
    fig.patch.set_facecolor('black')
    im = axe.imshow(l_del, cmap="hot_r")
    plt.axis('off')
    fig.savefig(f"img/img{steps:03d}.png", bbox_inches='tight')
    plt.close(fig)


flashes = 0
steps = 0
while True:
    steps += 1
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            data[y][x] += 1
    for y in range(1, (len(data) - 1)):
        for x in range(1, (len(data[y]) - 1)):
            if data[y][x] == 10:
                get_neighbours(y, x)
    if steps == 100:
        print("Part 1:", flashes)
    print_map(data)
    l_del = data[1:-1, 1:-1]
    if np.all(l_del == 0):
        print("Part 2:", steps)
        break