with open("day1.txt") as f:
    data = [int(x) for x in f.readlines()]

def part_one():
    d = 0
    for idx, a in enumerate(data):
        if idx > 0:
            if a > data[idx - 1]:
                d += 1
    return d

def part_two():
    d = 0
    for idx, a in enumerate(data):
        if idx <= (len(data) - 4):
            if a < data[idx + 3]:
                d += 1
        else:
            break
    return d

print("Solution for first part:", part_one())
print("Solution for second part:", part_two())

