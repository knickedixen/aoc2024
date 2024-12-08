
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
steps = []
obs = []
dir = 0
x = 0
y = 0
for li,l in enumerate(lines):
    lineObs = []
    step = []
    for ci,c in enumerate(l):
        step.append(0)
        if c == "#":
            lineObs.append(ci)
        if c == '^':
            x = ci
            y = li
    obs.append(lineObs)
    steps.append(step)

def walkX(fr, to, d):
    global y
    global x
    global dir
    for i in range(fr,to,d):
        if i in obs[y]:
            dir = (dir + 1) % 4
            x = i-d
            return False
        steps[y][i] = 1
        if (dir<0 and i == 0) or (dir > 0 and i == len(steps[y])):
            return True

def walkY(fr, to, d):
    global y
    global x
    global dir
    for i in range(fr,to,d):
        if x in obs[i]:
            y = i-d
            dir = (dir + 1) % 4
            return False
        steps[i][x] = 1
        if (dir<0 and i == 0) or (dir > 0 and i == len(steps[x])-1):
            return True

def walk():
    global y
    global x
    global dir
    steps[y][x] = 1
    while True:
        if dir == 0:
            if walkY(y,-1,-1):
                return
        elif dir == 1:
            if walkX(x,len(steps[y]),1):
                return
        elif dir == 2:
            if walkY(y,len(steps),1):
                return
        elif dir == 3:
            if walkX(x,-1,-1):
                return


walk()
for step in steps:
    for s in step:
        result += s

print(result)
