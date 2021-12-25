with open("day22.txt") as f:
    data = f.readlines()

on = set()

for i in data:
    first = i.split(",")
    for j in first:
        a = j.split("=")
        if a[0] == "y":
            ys = [int(x) for x in a[1].split("..")]
            # print(ys)
        elif a[0] == "z":
            zs = [int(x) for x in a[1].split("..")]
        else:
            xs = [int(x) for x in a[1].split("..")]
    for x in range(xs[0], xs[1] + 1):
        if x > 50 or x < -50:
            continue
        else:
            for y in range(ys[0], ys[1] + 1):
                if y > 50 or y < -50:
                    continue
                else:
                    for z in range(zs[0], zs[1] + 1):
                        if z > 50 or z < -50:
                            continue
                        else:
                            if i.startswith("on"):
                                on.add((x, y, z))
                            else:
                                if (x, y, z) in on:
                                    on.discard((x, y, z))

print(len(on))

# Part two:

on = set()

for i in data:
    first = i.split(",")
    for j in first:
        a = j.split("=")
        if a[0] == "y":
            ys = [int(x) for x in a[1].split("..")]
            # print(ys)
        elif a[0] == "z":
            zs = [int(x) for x in a[1].split("..")]
        else:
            xs = [int(x) for x in a[1].split("..")]
    for x in range(xs[0], xs[1] + 1):
        for y in range(ys[0], ys[1] + 1):
            for z in range(zs[0], zs[1] + 1):
                if i.startswith("on"):
                    on.add((x, y, z))
                else:
                    if (x, y, z) in on:
                        on.discard((x, y, z))

print(len(on))