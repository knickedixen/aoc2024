
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
map = {}
processed = {}

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        map[y,x] = c

def searchRegion(pos,type):
    if pos not in map:
        return []

    current = map[pos]
    if current != type or pos in processed:
        return []

    processed[pos] = 1
    region = [pos]

    y,x = pos
    region += searchRegion((y,x+1),type)
    region += searchRegion((y,x-1),type)
    region += searchRegion((y+1,x),type)
    region += searchRegion((y-1,x),type)

    return region

def calcFence(region):
    fence = 0
    for pos in region:
        y,x = pos
        if (y,x+1) not in region:
            fence += 1
        if (y,x-1) not in region:
            fence += 1
        if (y+1,x) not in region:
            fence += 1
        if (y-1,x) not in region:
            fence += 1
    return fence

for key,val in map.items():
    region = searchRegion(key,val)
    if region:
        area = len(region)
        fence = calcFence(region)
        result += area * fence

print(result)

