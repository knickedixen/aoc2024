import copy
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0

files = {}
space = {}
for ci,c in enumerate(lines[0]):
    if ci % 2 == 0:
        files[int(ci/2)] = int(c)
    else:
        space[int(ci/2)] = int(c)

fc = copy.deepcopy(files)
fcR = list(reversed(copy.deepcopy(files)))

sd = {}
fd = {}
for f,fl in reversed(fc.items()):
    for s, sl in space.items():
        if f < s:
            break;
        if sl >= fl:
            if not s in sd:
                sd[s] = []
            sd[s].append({f:fl})
            space[s] = sl - fl
            files[f] = 0
            fd[f] = fl
            break

arr = []
for i,f in files.items():
    if i in fd:
        for c in range(fd[i]):
            arr.append(False)
    else:
        for c in range(f):
            arr.append(i)
    if i in sd:
        for sdf in sd[i]:
           for fds,fdsl in sdf.items():
                for j in range(fdsl):
                    arr.append(fds)
    if i in space:
        for j in range(space[i]):
            arr.append(False)

for i,n in enumerate(arr):
    if n != False: 
        result += i * int(n)

print(result)
