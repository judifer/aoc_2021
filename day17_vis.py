import matplotlib.pyplot as plt
import matplotlib.patches as patches

xrange = (248, 285)
yrange = (-85, -56)

def check_land(v):
    x1 = list()
    y1 = list()
    global max_x
    global max_y
    speed = [0, 0]
    x1.append(0)
    y1.append(0)
    while True:
        speed[0] += v[0]
        speed[1] += v[1]
        if v[0] > 0: v[0] -= 1
        v[1] -= 1
        x1.append(speed[0])
        y1.append(speed[1])
        if ((xrange[0] <= speed[0] <= xrange[1]) and (yrange[0] <= speed[1] <= yrange[1])):
            if max(x1) > max_x:
                max_x = max(x1)
            if max(y1) > max_y:
                max_y = max(y1)
            xs.append(x1)
            ys.append(y1)
            break
        elif speed[0] > xrange[1] or speed[1] < yrange[0]:
            break
 

xs = list()
ys = list()
max_x = 0
max_y = 0

for x in range(22, 286):
    for y in range(-85, 85):
        check_land([x, y])

fig, axe = plt.subplots(figsize=(12, 10))
plt.suptitle("Day 17 - Throwing a probe")
plt.xlim([0, max_x])
plt.ylim([-100, max_y])
for i in range(0, len(xs)):
    axe.plot(xs[i], ys[i])
rect = patches.Rectangle((xrange[0], yrange[0]), 37, 29, linewidth=1, linestyle="--", visible=True, zorder=5000, edgecolor="r", fill=False)
axe.add_patch(rect)
fig.savefig('Visualizations/Day17_Visualization.png', transparent=False)
plt.close()