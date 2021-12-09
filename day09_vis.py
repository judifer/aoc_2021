import matplotlib.pyplot as plt

with open("day9.txt") as f:
    data = [[int(x) for x in y.strip()] for y in f]

fig, axe = plt.subplots(dpi=800)
axe.set_title("Basins visualised")
im = axe.imshow(data, cmap="hot_r")
axe.figure.colorbar(im, ax=axe)
fig.savefig("img/Day9_Visualization.png")
plt.close(fig)