with open("day7.txt") as f:
    text = f.read()

data = list(map(int, text.split(",")))

fuel = list()

for i in range(min(data), max(data)):
    counter = 0
    for crab in data:
        if crab > i:
            counter += crab - i
        elif crab < i:
            counter += i - crab
    fuel.append(counter)

print("Part one:", min(fuel))

fuel = list()

for i in range(min(data), max(data)):
    counter = 0
    for crab in data:
        steps = 1
        if crab > i:
            steps = crab - i
            counter += steps * (steps + 1) / 2
        elif crab < i:
            steps = i - crab
            counter += steps * (steps + 1) / 2
    fuel.append(counter)

print("Part two:", min(fuel))