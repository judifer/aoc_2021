start_one = 4
start_two = 8
x = False
score_one = 0
score_two = 0
c = 0
i = 0
while x == False:
    if c == 0:
        i = 1
    else:
        i += 6
    c += 6
    start_one += (i + i + 1 + i + 2) % 10
    start_two += (i + 3 + i + 4 + i + 5) % 10
    if start_one > 10:
        start_one -= 10
    if start_two > 10:
        start_two -= 10
    score_one += start_one
    if score_one >= 1000:
        x = True
        c -= 3
        break
    score_two += start_two
    if score_two >= 1000:
        x = True
        break

print(score_one)
print(score_two)
print(c)

if score_one < score_two:
    print("Part 1:", score_one * c)
else:
    print("Part 1:", score_two * c)


    x = False
score_one = 0
score_two = 0
c = 0
i = 0



while x == False:
    if c == 0:
        i = 1
    else:
        i += 6
    c += 6
    start_one += (i + i + 1 + i + 2) % 10
    start_two += (i + 3 + i + 4 + i + 5) % 10
    if start_one > 10:
        start_one -= 10
    if start_two > 10:
        start_two -= 10
    score_one += start_one
    if score_one >= 1000:
        x = True
        c -= 3
        break
    score_two += start_two
    if score_two >= 1000:
        x = True
        break