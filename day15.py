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
    print(G)
    path = nx.shortest_path(G, source=(0, 0), target=(goal, goal), weight='weight')
    risk = sum(data[y][x] for x, y in path[1:])
    return risk

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
    print(G)
    path = nx.shortest_path(G, source=(0, 0), target=(goal, goal), weight='weight')
    risk = sum(new_data[y][x] for x, y in path[1:])
    return risk

print("Part one:", part_one())
print("Part two:", part_two())