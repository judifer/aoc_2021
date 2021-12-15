import matplotlib.pyplot as plt
import networkx as nx

with open("day15.txt") as f:
    data = [[int(x) for x in y.strip()] for y in f]

def generate_graph(data):
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data)):
            G.add_node((x, y))
            neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nex, ney in neighbours:
                if 0 <= nex < len(data) and 0 <= ney < len(data):
                    G.add_edge((x, y), (nex, ney), weight=data[ney][nex])
    return G

def part_one():
    goal = len(data) - 1
    G = generate_graph(data)
    return G

def part_two():
    new_data = [x for x in data]
    for i in range(1, 5):
        for y in range(len(data)):
            for x in range(len(data)):
                new = data[y][x] + i
                if new > 9:
                    new -= 9
                new_data[y].append(new)
    
    for i in range(1, 5):
        for y in range(len(data)):
            new_data.append([])
            for x in range(len(new_data[0])):
                new = new_data[y][x] + i
                if new > 9:
                    new -= 9
                new_data[-1].append(new)

    goal = len(new_data) - 1
    G = generate_graph(new_data)
    return new_data, G

first_graph = part_one()
new_map, second_graph = part_two()

fig = plt.figure(figsize=(200, 200)) 
edges,weights = zip(*nx.get_edge_attributes(first_graph,'weight').items())
nx.draw(first_graph, node_color='b', node_size=1000, edgelist=edges, edge_color=weights, width=10.0, edge_cmap=plt.cm.spring_r, node_shape="h")
plt.savefig("Visualizations/Day15_Visualization_1.png")

fig, axe = plt.subplots(dpi=800)
axe.set_title("Danger caves")
im = axe.imshow(new_map, cmap="spring_r")
axe.figure.colorbar(im, ax=axe)
fig.savefig("Visualizations/Day15_Visualization_2.png")
plt.close(fig)