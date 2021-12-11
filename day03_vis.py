import matplotlib.pyplot as plt
import numpy as np

with open("day3.txt") as f:
    data = [x.strip() for x in f]

one_list = list()
zero_list = list()
for i in range(0, len(data[0])):
    ones = 0
    zeroes = 0
    for j in data:
        if j[i] == "1":
            ones += 1
        else:
            zeroes += 1
    one_list.append(ones)
    zero_list.append(zeroes)

fig, axe = plt.subplots(dpi=800)
axe.set_title("Distribution of 1s and 0s")
index = np.arange(len(one_list))
values1 = one_list
values2 = zero_list
axe.bar(index, values1, color="teal", label="1s")
axe.bar(index, values2, bottom=values1, color="turquoise", label="0s")
plt.axhline(y=500, color='black', linestyle='--', linewidth=1)
plt.tick_params(bottom=False,
                labelbottom=False,)
plt.legend(loc="upper left")
fig.savefig("img/Day3_Visualization.png")
plt.close(fig)
