from collections import defaultdict, deque

with open("day12.txt") as f:
    data = [[x.strip() for x in y.split("-")] for y in f.readlines()]

neighbours = defaultdict(list)

def find_path(path, nl, allow_twice):
    if path[-1] == "end":
        return 1
    count = 0
    for i in nl[path[-1]]:
        if i.isupper() or i not in path:
            path.append(i)
            count += find_path(path, nl, allow_twice)
            path.pop()
        elif allow_twice and i not in ["start", "end"]:
            path.append(i)
            count += find_path(path, nl, False)
            path.pop()
    return count
        

for i in data:
    a, b = i
    neighbours[a].append(b)
    neighbours[b].append(a)

print(neighbours)

print("Part 1:", find_path(["start"], neighbours, False))
print("Part 2:", find_path(["start"], neighbours, True))
