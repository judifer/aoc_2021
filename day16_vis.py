from collections import defaultdict
import matplotlib.pyplot as plt

with open("day16.txt") as f:
  inp = f.read()

data = ""

for i in inp:
  a = bin(int(i, 16))[2:]
  if len(a) < 4:
    data += "0" * (4 - len(a))
  data += a

long_list = list()

version_sum = 0
def parse_packet(packet, depth):
    global version_sum
    str_version = packet[0:3]
    str_type = packet[3:6]
    str_rest = packet[6:]
    # long_list.append(("Version:", str_version))
    version = int(str_version, 2)
    type = int(str_type, 2)
    long_list.append(type)
    version_sum += version
    if type == 4:
        str_literal = ""
        while str_rest:
            str_literal += str_rest[1:5]
            q = str_rest[0]
            str_rest = str_rest[5:]
            if q == "0":
                # long_list.append(("str_rest", str_literal))
                break
        return (version, int(str_literal,2), str_rest)
    else:
        content = []
        if str_rest[0] == "0":
            length = int(str_rest[1:16], 2)
            # long_list.append(("Length:", length))
            str_rest = str_rest[16:]
            str_subpackets = str_rest[:length]
            str_rest = str_rest[length:]
            while str_subpackets:
                rec_version, rec_content, str_subpackets = parse_packet(str_subpackets, depth + 1)
                content.append(rec_content)
        else:
            num = int(str_rest[1:12], 2)
            # long_list.append(("num_packs:", num))
            str_rest = str_rest[12:]
            m = list(range(num))
            for i in m:
                rec_version, rec_content, str_rest = parse_packet(str_rest, depth + 1)
                content.append(rec_content)
        result = 0
        if type == 0:
            result = sum(content)
        elif type == 1:
            result = 1
            for c in content:
                result *= c
        elif type == 2:
            result = min(content)
        elif type == 3:
            result = max(content)
        else:
            if (type == 5) and (content[0] > content[1]):
                result = 1
            if (type == 6) and (content[0] < content[1]):
                result = 1
            if (type == 7) and (content[0] == content[1]):
                result = 1
        return(version, result, str_rest)

rec_version, result, t_rest = parse_packet(data, 0)

types = defaultdict(int)

for i in long_list:
    types[i] += 1

so_types = sorted(types.keys())
so_vals = list()
for i in so_types:
    so_vals.append(types[i])


colors = ["r", "b", "g", "y", "pink", "orange", "purple", "indigo"]
label = [f"Type {i}" for i in so_types]
fig, ax = plt.subplots()
plt.suptitle("Day 16 - Types of packages")
ax.barh(so_types, so_vals, height=1, edgecolor="white", color=colors, linewidth=0.7, tick_label=label)
fig.savefig('Visualizations/Day16_Visualization.png')
plt.close()