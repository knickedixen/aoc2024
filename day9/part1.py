import copy
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
l = lines[0]
arr = []
for ci, c in enumerate(lines[0]):
    for n in range(int(c)):
        if ci % 2 == 0:
            arr.append(ci/2)
        else:
            arr.append(".")

arrC = copy.deepcopy(arr)
arrR = list(reversed(copy.deepcopy(arr)))

la = len(arr)-1
for ai,a in enumerate(arr):
    if a == ".":
        for i,b in enumerate(arrR):
            bi = la - i
            if ai == bi:
                break
            if b != ".":
                arrC[ai] = b
                arrC[bi] = "."
                arrR[i] = "."
                break

for i,n in enumerate(arrC):
    if n == ".": 
        break
    result += i * int(n)

print(result)
