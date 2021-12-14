from collections import defaultdict

with open("day14.txt") as f:
    data = f.read().split("\n\n")

pol = [x.split() for x in data[0]]
directions = [[x for x in y.split(" -> ")] for y in data[1].split("\n")]
dir = defaultdict(str)

for x, y in directions:
    dir[x] = y

pairs = defaultdict(int)

vals = defaultdict(int)

for i in range(0, len(pol)):
    vals[pol[i][0]] += 1
    if i > 0:
        a = pol[i - 1][0] + pol[i][0]
        pairs[a] += 1

for i in range(40):
    temp = defaultdict(int)
    for p in pairs.keys():
        ins = dir[p]
        a = p[0] + ins
        b = ins + p[1]
        temp[a] += pairs[p]
        temp[b] += pairs[p]
        vals[ins] += pairs[p]
    pairs = temp
    if i == 9:
        a = max(vals.values())
        b = min(vals.values())
        print("Part 1:", a - b)

a = max(vals.values())
b = min(vals.values())
print("Part 2:", a - b)