from math import log10
from math import pow
from time import time
start_time = time()

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
line = lines[0]
blinks = 75
mem = {}

def count(st, de):
    if de == blinks:
        return 1

    de += 1
    key = f'({st},{de}'

    if key in mem:
         return mem[key]

    if st == 0:
        res = count(1, de)
    else:
        lst = int(log10(st)) + 1
        even = lst % 2 == 0
        if even:
            lst2 = pow(10, lst/2)
            le = st // lst2
            ri = st % lst2
            res = count(le,de) + count(ri,de)
        else:
            res = count(st*2024, de)

    mem[key] = res
    return res

for st in line.split(' '):
    result += count(int(st), 0)

print()
print(result)

print("--- %s seconds ---" % (time() - start_time))
