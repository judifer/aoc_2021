import sys

with open("day8.txt") as f:
    data = [x.strip() for x in f.readlines()]

out = list()
inp = list()

for i in range(0, len(data)):
    a, b = data[i].split(" | ")
    inp.append(a)
    out.append(b)

nums = {0: 6, 1: 2, 2: 5, 2: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

count = 0

for i in out:
    a = i.split(" ")
    for j in a:
        if len(j) == nums[1] or len(j) == nums[4] or len(j) == nums[7] or len(j) == nums[8]:
            count += 1

print("Part 1:", count)

count = 0

for i in range(0, len(data)):
    outlet = ""
    long = data[i].split(" | ")
    a = long[0].split(" ")
    b = long[1].split(" ")
    for letter in (a + b):
        if len(letter) == 2:
            one = letter
        elif len(letter) == 4:
            four = letter
    for j in b:
        if len(j) == nums[1]:
            outlet += "1"
        elif len(j) == nums[4]:
            outlet += "4"
        elif len(j) == nums[7]:
            outlet += "7"
        elif len(j) == nums[8]:
            outlet += "8"
        elif len(j) == nums[2]:
            if len((set(j).intersection(one))) == 2:
                outlet += "3"
            elif len(set(j).intersection(four)) == 2:
                outlet += "2"
            else:
                outlet += "5"
        else:
            if len(set(j).intersection(four)) == 4:
                outlet += "9"
            elif len(set(j).intersection(one)) == 2:
                outlet += "0"
            elif len(set(j).intersection(four)) == 4:
                outlet += "9"
            else:
                outlet += "6"
    count += int(outlet)

print("Part 2:", count)