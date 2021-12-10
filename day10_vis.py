import sys

with open("day10.txt") as f:
    data = [x.strip() for x in f.readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

incomplete_lines = list()

to_print = dict()


score = 0
corrupt_lines = dict()
score2 = 0
scores = list()
for idx, i in enumerate(data):
    score2 = 0
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
                score += points[j]
                corrupt = True
                to_print[i] = j
                break
    if corrupt == False:
        chars = list()
        for a in instruction[::-1]:
            score2 *= 5
            score2 += points[a]
            chars.append(pairs[a])
        scores.append(score2)
        characters = "".join(chars)
        ins = "".join(instruction)
        to_print[ins] = characters

print_lines = list()

for i in to_print.keys():
    if len(to_print[i]) > 1:
        a = f"{i}{' ' * (110 - len(i))}Incomplete! Complete with {to_print[i]}"
        print_lines.append(a)
    else:
        a = f"{i}{' ' * (110 - len(i))}Corrupt! Unexpected \'{to_print[i]}\'{' ' * 20}"
        print_lines.append(a)

for num in range(0, len(print_lines)):
    stdout = sys.stdout
    with open(f"img/img{num:03d}.txt", "w") as f:
        sys.stdout = f
        if num > 30:
            for line in range(num - 30, num):
                print(print_lines[line])
        else:
            for line in range(0, num):
                print(print_lines[line])
            print("\n" * (29 - num))
    sys.stdout = stdout