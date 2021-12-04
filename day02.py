with open("day2.txt") as f:
    data = [x.strip() for x in f.readlines()]

x = 0
y = 0
y2 = 0

for i in data:
    a, b = i.split()
    b = int(b)
    if a == "forward":
        x += b
        y2 += y * b
    elif a == "down":
        y += b
    else:
        y -= b

print("Part one:", x * y)
print("Part two:", x * y2)