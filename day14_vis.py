import matplotlib.pyplot as plt
from collections import defaultdict

with open("day14.txt") as f:
    data = f.read().split("\n\n")

pol = [x.split() for x in data[0]]
directions = [[x for x in y.split(" -> ")] for y in data[1].split("\n")]
dir = defaultdict(str)

for x, y in directions:
    dir[x] = y

all_values = list()

pairs = defaultdict(int)

vals = defaultdict(int)
lengths = list()
for i in range(0, len(pol)):
    vals[pol[i][0]] += 1
    if i > 0:
        a = pol[i - 1][0] + pol[i][0]
        pairs[a] += 1
lengths.append(len(pol))
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
    length = 0
    for j in vals:
        length += vals[j]
    lengths.append(length)
    fig, axe = plt.subplots(dpi=800)
    axe.set_title("Distribution of polymer-parts")
    label = vals.keys()
    values = vals.values()
    axe.bar(label, values)
    fig.savefig(f"img/img{i:03d}.png")
    plt.close(fig)


line = list()
for i in lengths:
    line.append(0)

fig, axe = plt.subplots(dpi=800)
axe.set_title("Length of our polymer per step")
axe.plot(lengths, "g")
fig.savefig(f"Visualizations/Day14_Visualization.png")
plt.close(fig)