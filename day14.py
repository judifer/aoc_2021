from collections import defaultdict

with open("day14.txt") as f:
    data = f.read().split("\n\n")

pol = [x.split() for x in data[0]]
directions = [[x for x in y.split(" -> ")] for y in data[1].split("\n")]
dir = defaultdict(str)

for x, y in directions:
    dir[x] = y

pairs = defaultdict(int)

for i in range(1, len(pol)):
    a = pol[i - 1][0] + pol[i][0]
    pairs[a] += 1

print(pairs)
for i in range(40):
    temp = defaultdict(int)
    for p in pairs.keys():
        ins = dir[p]
        a = p[0] + ins
        b = ins + p[1]
        temp[a] += pairs[p]
        temp[b] += pairs[p]
    pairs = temp

# vals = defaultdict(int)

# for i in pairs.keys():
#     vals[i[0]] += pairs[i]

print(vals)

maxp = max(vals.values())
minp = min(vals.values())

print(maxp - minp)