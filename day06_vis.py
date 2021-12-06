import matplotlib.pyplot as plt

with open("day6.txt") as f:
    data = f.read()

fish = list(map(int, data.split(",")))

breed = dict()
for i in range(0, 10):
    breed[i] = 0
for i in fish:
    breed[i] += 1

x = 0

graph = list()
fishies = breed.values()
number = sum(fishies)
graph.append(number)

while x < 256:
    for fi in range(0, 10):
        if fi == 0:
            breed[9] += breed[fi]
            breed[7] += breed[fi]
            breed[fi] = 0
        else:
            breed[fi - 1] += breed[fi]
            breed[fi] = 0
    fishies = breed.values()
    number = sum(fishies)
    graph.append(number)
    steps = list(range(0, len(graph)))
    fig, axe = plt.subplots(dpi=300)
    axe.plot(steps, graph, "r")
    fig.savefig(f"img/grid{x}.png")
    plt.close(fig)
    x += 1