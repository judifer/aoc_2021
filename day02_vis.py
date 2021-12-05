import matplotlib.pyplot as plt

with open("day2.txt") as f:
    ship = [x.strip() for x in f.readlines()]

with open("day1.txt") as g:
    data = [0 - int(x) for x in g.readlines()]

x = 0
y = 0
y2 = 0

xs = list()
y2s = list()

for i in ship:
    a, b = i.split()
    b = int(b)
    if a == "forward":
        x += b
        y2 += y * b
    elif a == "down":
        y += b
    else:
        y -= b
    y2s.append(0 - y2)
    xs.append(x)

ground = list()
for i in xs:
    ground.append(data[i])

line = list([0] * (len(xs)))

fig, axe = plt.subplots(dpi=300)
for i in range(0, len(xs)):
    plt.plot(xs[:i], line[:i], "b")
    plt.plot(xs[:i], y2s[:i], "r")
    plt.plot(xs[:i], ground[:i], "y")
    fig.savefig(f"img/img{i}.png")
plt.close(fig)