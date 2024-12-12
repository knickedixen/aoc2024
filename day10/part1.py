
with open("input.txt") as file:
    map = [list(line.rstrip()) for line in file]

result = 0
max = len(map)

def check(x,y,p):
    if x >= max or y >= max or y < 0 or x < 0:
        return []
    h = int(map[x][y])
    if h-p != 1:
        return []
    if h == 9:
        return [f"{x},{y}"]

    return explore(x,y,h)

def explore(x,y,p):
    res = []
    res.extend(check(x+1,y,p))
    res.extend(check(x-1,y,p))
    res.extend(check(x,y+1,p))
    res.extend(check(x,y-1,p))

    return res 

for x in range(max):
    for y in range(len(map[x])):
        if int(map[x][y]) == 0:
            result += len(list(set(explore(x,y,0))))

print(result)
