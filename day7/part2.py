
import copy

def calc(res, val, nrs):
    if not nrs:
        return res == val
    if res > val:
        return False

    next = nrs.pop(0)
    if res != 0:
        comb = int(str(res) + str(next))
        if calc(comb, val, copy.deepcopy(nrs)):
            return True
    if calc(res + next, val, copy.deepcopy(nrs)):
        return True
    if calc((res or 1) * next, val, copy.deepcopy(nrs)):
        return True

    return False

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0

for l in lines:
    lv = l.strip().split(":")
    val = int(lv[0])
    nrs = list(map(int, lv[1].strip().split(" ")))
    if calc(0, val, nrs):
        result += val


print(result)
