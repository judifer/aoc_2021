with open("day3.txt") as f:
    data = [x.strip() for x in f]

gamma = list()
epsilon = list()

def popular_bit(x):
    if sum(x) == (len(x) / 2):
        return "both"
    elif sum(x) > (len(x) / 2):
        return "1"
    else:
        return "0"

def part_one():
    for i in range(0, len(data[0])):
        bitslist = list()
        for j in data:
            bitslist.append(int(j[i]))
        bit = popular_bit(bitslist)
        if bit == "both":
            print("wat.")
        elif bit == "0":
            gamma.append("0")
            epsilon.append("1")
        else:
            gamma.append("1")
            epsilon.append("0")
    gam = "".join(gamma)
    ep = "".join(epsilon)
    res = int(gam, 2) * int(ep, 2)
    return res

print("Part one:", part_one())

def part_two(data):
    for j in range(0, len(data[0])):
        temp_data = list()
        bitslist = list()
        for i in data:
            bitslist.append(int(i[j]))
        bit = popular_bit(bitslist)
        if bit == "both":
            for i in data:
                if i[j] == "1":
                    temp_data.append(i)
        else:
            for i in data:
                if i[j] == bit:
                    temp_data.append(i)
        data = [x for x in temp_data]
        if len(data) == 1:
            return int(data[0], 2)

def part_two_co(data):
    for j in range(0, len(data[0])):
        temp_data = list()
        bitslist = list()
        for i in data:
            bitslist.append(int(i[j]))
        bit = popular_bit(bitslist)
        if bit == "both":
            for i in data:
                if i[j] == "0":
                    temp_data.append(i)
        else:
            for i in data:
                if i[j] != bit:
                    temp_data.append(i)
        data = [x for x in temp_data]
        if len(data) == 1:
            return int(data[0], 2)

print("Part two:", part_two(data) * part_two_co(data))