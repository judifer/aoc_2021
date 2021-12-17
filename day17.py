# target area: x=248..285, y=-85..-56

xrange = (248, 285)
yrange = (-85, -56)

vel = abs(yrange[0]) - 1
maxheight = (vel + 1) * vel // 2
print("Part 1:", maxheight)

total = 0
def check_land(v):
    global total
    speed = [0, 0]
    while True:
        speed[0] += v[0]
        speed[1] += v[1]
        if v[0] > 0: v[0] -= 1
        v[1] -= 1
        if ((xrange[0] <= speed[0] <= xrange[1]) and (yrange[0] <= speed[1] <= yrange[1])):
            total += 1
            break
        elif speed[0] > xrange[1] or speed[1] < yrange[0]:
            break
 
for x in range(22, 286):
    for y in range(-85, 85):
        check_land([x, y])
 
print("Part 2:", total)