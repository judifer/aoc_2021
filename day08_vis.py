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

def print_boards(num, line, idx):
    stdout = sys.stdout
    with open(f"img/img{idx:03d}.txt", "w") as f:
        sys.stdout = f
        print(f"{' ' * 33}Line number {idx + 1}:\n{line}\n")
        a = print_num(num[0])
        b = print_num(num[1])
        c = print_num(num[2])
        d = print_num(num[3])
        print()
        print()
        print()
        for i in range(0, len(a)):
            print(f"{' ' * 30}{a[i][0]}   {b[i][0]}   {c[i][0]}   {d[i][0]}{' ' * 30}")
        print()
        print()
        print()
    sys.stdout = stdout

def print_num(num):    
    if num == "0":
        show = [
            [" @@@@ "],
            ["@    @"],
            ["@    @"],
            [" .... "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "]
        ]
    elif num == "1":
        show= [
            [" .... "],
            [".    @"],
            [".    @"],
            [" .... "],
            [".    @"],
            [".    @"],
            [" .... "]
        ]
    elif num == "2":
        show= [
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" @@@@ "],
            ["@    ."],
            ["@    ."],
            [" @@@@ "]
        ]
    elif num == "3":
        show = [
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" @@@@ "]
        ]
        
    elif num == "4":
        show = [
            [" .... "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" .... "]
        ]
    elif num == "5":
        show = [
            [" @@@@ "],
            ["@    ."],
            ["@    ."],
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" @@@@ "]
        ]
    elif num == "6":
        show = [
            [" @@@@ "],
            ["@    ."],
            ["@    ."],
            [" @@@@ "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "]
        ]
    elif num == "7":
        show = [
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" .... "],
            [".    @"],
            [".    @"],
            [" .... "]
        ]
    elif num == "8":
        show = [
            [" @@@@ "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "]
        ]
    elif num == "9":
        show = [
            [" @@@@ "],
            ["@    @"],
            ["@    @"],
            [" @@@@ "],
            [".    @"],
            [".    @"],
            [" @@@@ "]
        ]
    else:
        show = "Error."
    return show

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
    print_boards(outlet, data[i], i)