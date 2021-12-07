import matplotlib.pyplot as plt

with open("day7.txt") as f:
    text = f.read()

data = list(map(int, text.split(",")))
line = [x for x in range(min(data), (max(data) + 1))]

fish_loc = dict()
for i in range(min(data), (max(data) + 1)):
    fish_loc[i] = 0

for i in data:
    fish_loc[i] += 1

fishes = [x for x in fish_loc.values()]

fuel = list()

for i in range(min(data), (max(data) + 1)):
    counter = 0
    for crab in data:
        if crab > i:
            counter += crab - i
        elif crab < i:
            counter += i - crab
    fuel.append(counter)

fuel2 = list()

for i in range(min(data), (max(data) + 1)):
    counter = 0
    for crab in data:
        steps = 1
        if crab > i:
            steps = crab - i
            counter += steps * (steps + 1) / 2
        elif crab < i:
            steps = i - crab
            counter += steps * (steps + 1) / 2
    fuel2.append(counter)

fig, axs = plt.subplots(3)
fig.suptitle('The Treachery of Whales')
plt.subplots_adjust(hspace = 0.7)
axs[0].fill_between(line, fishes, facecolor='b', alpha=0.8)
axs[0].set_title("Crabs")
axs[1].plot(line, fuel, "g")
axs[1].set_title("Fuel consumption, part 1")
axs[2].plot(line, fuel2, "r")
axs[2].set_title("Fuel consumption, part 2")
fig.savefig(f"img/img.png")
plt.close(fig)