with open("day10.txt") as f:
    data = [x.strip() for x in f.readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

incomplete_lines = list()

score = 0

for i in data:
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
                break
    incomplete_lines.append(instruction)


print("Part 1:", score)

points = {"(": 1, "[": 2, "{": 3, "<": 4}

score = 0
scores = list()
for i in incomplete_lines:
    score = 0
    for j in i[::-1]:
        score *= 5
        score += points[j]
    scores.append(score)

scores.sort()
score = scores[(len(scores)) // 2]

print("Part 2:", score)