from pprint import pp
import copy

with open("day25.txt") as f:
    data = [[x for x in y.strip()] for y in f.readlines()]

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
    data = temp
    if state == data:
        print("Part 1:", i + 1)
        break