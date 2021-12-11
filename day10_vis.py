import sys

with open("day10.txt") as f:
    data = [x.strip() for x in f.readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

to_print = list()

for idx, i in enumerate(data):
    corrupt = False
    instruction = list()
    for j in i:
        if j in opening:
            instruction.append(j)
        elif j in closing:
            if j == ")" and instruction[-1] == "(":
                instruction.pop()
            elif j == "]" and instruction[-1] == "[":
                instruction.pop()
            elif j == "}" and instruction[-1] == "{":
                instruction.pop()
            elif j == ">" and instruction[-1] == "<":
                instruction.pop()
            else:
                corrupt = True
                a = f"{i}{' ' * (110 - len(i))}Corrupt! Unexpected \'{j}\'{' ' * 20}"
                to_print.append(a)
                break
    if corrupt == False:
        chars = list()
        for a in instruction[::-1]:
            chars.append(pairs[a])
        a = f"{i}{' ' * (110 - len(i))}Incomplete! Complete with {''.join(chars)}"
        to_print.append(a)

for num in range(0, len(to_print)):
    stdout = sys.stdout
    with open(f"img/img{num:03d}.txt", "w") as f:
        sys.stdout = f
        if num > 30:
            for line in range(num - 30, num):
                print(to_print[line])
        else:
            for line in range(0, num):
                print(to_print[line])
            print("\n" * (29 - num))
    sys.stdout = stdout