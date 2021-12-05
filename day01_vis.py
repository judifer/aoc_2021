import matplotlib.pyplot as plt

with open("day1.txt") as f:
    data = [0 - int(x) for x in f.readlines()]

steps = list(range(0, len(data)))

line = list([0] * (len(steps)))

fig, axe = plt.subplots(dpi=300)
for i in steps:
    if i < 2:
        plt.plot(steps[(i - 2):i], line[(i - 2):i], "b")
        plt.plot(steps[(i - 2):i], data[(i - 2):i], "y")
        fig.savefig(f"img/img{i}.png")
plt.close(fig)