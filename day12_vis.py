from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

with open("day12.txt") as f:
    data = [[x.strip() for x in y.split("-")] for y in f.readlines()]

neighbours = defaultdict(list)

for i in data:
    a, b = i
    neighbours[a].append(b)
    neighbours[b].append(a)

graph = nx.DiGraph()


for i in neighbours.keys():
    if i == "start":
        graph.add_node(i, color="green")
    elif i == "end":
        graph.add_node(i, color="red")
    else:
        graph.add_node(i, color="blue")

for i in neighbours.keys():
    for j in neighbours[i]:
        graph.add_edge(i, j)

color_map = ['red' if node == 'end' else 'green' if node == 'start' else 'blue' for node in graph]        
nx.draw(graph, with_labels=True, node_color=color_map)
plt.savefig("Visualizations/Day12_Visualization.png")