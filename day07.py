with open("day7.txt") as f:
    text = f.read()

data = list(map(int, text.split(",")))
data.sort()

fuel = 0

for i in range(min(data), max(data)):
    prev = fuel
    fuel = 0
    for crab in data:
        fuel += abs(crab - i)
    if i > 0 and fuel > prev:
        fuel = prev
        break

print("Part one:", fuel)

fuel = list()

fuel = 0
for i in range(min(data), max(data)):
    prev = fuel
    fuel = 0
    for crab in data:
        steps = abs(crab - i)
        fuel += int(steps * (steps + 1) / 2)
    if i > 0 and fuel > prev:
        fuel = prev
        break

print("Part two:", fuel)