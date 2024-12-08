import copy

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
map = []
vis = {}
orgMap = []
obs = []
dir = 0
x = 0
y = 0
for li,l in enumerate(lines):
    lineObs = []
    step = []
    for ci,c in enumerate(l):
        step.append(c)
        if c == "#":
            lineObs.append(ci)
        if c == '^':
            x = ci
            y = li
    obs.append(lineObs)
    orgMap.append(step)

def walkX(fr, to, d):
    global y
    global x
    global dir
    global result
    for i in range(fr,to,d):
        if i in obs[y]:
            vin = f'd{dir}y{y}x{i}'
            if vin in vis and vis[vin]:
                result += 1
                return 1
            vis[vin] = True
            dir = (dir + 1) % 4
            x = i-d
            return 0
        if (d<0 and i == 0) or (d > 0 and i == len(map[y])-1):
            return 2

def walkY(fr, to, d):
    global y
    global x
    global dir
    global result
    for i in range(fr,to,d):
        if x in obs[i]:
            vin = f'd{dir}y{i}x{x}'
            if vin in vis and vis[vin]:
                result += 1
                return 1
            vis[vin] = True
            y = i-d
            dir = (dir + 1) % 4
            return 0
        if (d<0 and i == 0) or (d > 0 and i == len(map)-1):
            return 2

def walk():
    global y
    global x
    global dir
    global result
    while True:
        if dir == 0:
            re = walkY(y,-1,-1)
        elif dir == 1:
            re = walkX(x,len(map[y]),1)
        elif dir == 2:
            re = walkY(y,len(map),1)
        elif dir == 3:
            re = walkX(x,-1,-1)

        if re:
            return

orgObs = copy.deepcopy(obs)
sX = x
sY = y
aY = 0
aX = 0
for i,row in enumerate(orgMap):
    for j,s in enumerate(row):
        if orgMap[i][j] != "#" and not(i == sY and j == sX) and not(i == sY-1 and j == sX):
            map = copy.deepcopy(orgMap)
            obs = copy.deepcopy(orgObs)
            x = sX
            y = sY
            dir = 0
            obs[i].append(j)
            map[i][j] = 'A'
            vis = {}
            aY = i
            aX = j
            walk()

print(result)
