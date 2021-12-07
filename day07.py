with open("day7.txt") as f:
    text = f.read()

data = list(map(int, text.split(",")))
data.sort()

fuel = sum([abs(x - data[((len(data) + 1) // 2)]) for x in data])

print("Part one:", fuel)

fuel = float("inf")
for i in range(0, max(data)):
    prev = fuel
    fuel = sum((abs(x-i)*(1 + abs(x-i)))//2 for x in data)
    if fuel > prev:
        fuel = prev
        break

print("Part two:", fuel)