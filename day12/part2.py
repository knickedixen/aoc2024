
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
        top = (y-1,x) in region
        topLeft = (y-1,x-1) in region
        bot = (y+1,x) in region
        botLeft = (y+1,x-1) in region
        right = (y,x+1) in region
        topRight = (y-1,x+1) in region
        left = (y,x-1) in region
        botRight = (y+1,x+1) in region

        if not top and not left:
            fence += 1
        if not top and not right:
            fence += 1
        if not bot and not left:
            fence += 1
        if not bot and not right:
            fence += 1

        if not topLeft and top and left:
            fence += 1
        if not topRight and top and right:
            fence += 1
        if not botLeft and bot and left:
            fence += 1
        if not botRight and bot and right:
            fence += 1

    return fence

for key,val in map.items():
    region = searchRegion(key,val)
    if region:
        area = len(region)
        fence = calcFence(region)
        result += area * fence

print(result)

