
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0

freqs = {}
map = []
for li,l in enumerate(lines):
    row = []
    for ci,c in enumerate(l):
        row.append(".")
        if c != ".":
            ant = {"y": li, "x":ci}
            if c in freqs:
                freqs[c].append(ant)
            else:
                freqs[c] = [ant]
    map.append(row)

mapSize = len(map)
for freq,ants in freqs.items():
    for ant in ants:
        for other in freqs[freq]:
            if ant != other:
                antiy = ant["y"] + ant["y"] - other["y"]
                antix = ant["x"] + ant["x"] - other["x"]
                if antix >= 0 and antix < mapSize and antiy >= 0 and antiy < mapSize:
                    map[antiy][antix] = "#"

for m in map:
    for c in m:
        if c == "#":
            result += 1

print(result)
