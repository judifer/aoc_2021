from pprint import pp
import copy
import matplotlib.pyplot as plt

with open("day25.txt") as f:
    data = [[x for x in y.strip()] for y in f.readlines()]

all_maps = list()

for i in range(0,  1000):
    temp = list()
    temp = copy.deepcopy(data)
    state = copy.deepcopy(data)
    for idx, y in enumerate(data):
        for idx2, x in enumerate(y):
            if x == ">":
                if idx2 >= (len(y) - 1):
                    if data[idx][0] == ".":
                        temp[idx][idx2] = "."
                        temp[idx][0] = ">"
                else:
                    if data[idx][idx2 + 1] == ".":
                        temp[idx][idx2] = "."
                        temp[idx][idx2 + 1] = ">"
    data = copy.deepcopy(temp)
    for idx, y in enumerate(data):
        for idx2, x in enumerate(y):
            if x == "v":
                if idx >= (len(data) - 1):
                    if data[0][idx2] == ".":
                        temp[0][idx2] = "v"
                        temp[idx][idx2] = "."
                else:
                    if data[idx + 1][idx2] == ".":
                        temp[idx + 1][idx2] = "v"
                        temp[idx][idx2] = "."
    data = copy.deepcopy(temp)
    for idx, y in enumerate(temp):
        for idx2, x in enumerate(y):
            if x == ".":
                temp[idx][idx2] = 0
            elif x == ">":
                temp[idx][idx2] = 2
            elif x == "v":
                temp[idx][idx2] = 4
    all_maps.append(temp)
    if state == data:
        print("Part 1:", i + 1)
        break

c = 0
for i in all_maps:
    fig, axe = plt.subplots(dpi=150)
    axe.set_title("Sea cucumber movement")
    im = axe.imshow(i, cmap="BuGn")
    plt.axis('off')
    fig.savefig(f"img/img{c:03d}.png", bbox_inches='tight')
    plt.close(fig)
    c += 1