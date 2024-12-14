from math import log10
from math import pow

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
line = lines[0]
blinks = 25

def count(st, de):
    if de == blinks:
        return 1

    de += 1

    if st == 0:
        return count(1, de)

    lst = int(log10(st)) + 1
    even = lst % 2 == 0
    if even:
        lst2 = pow(10, lst/2)
        le = st // lst2
        ri = st % lst2
        return count(le,de) + count(ri,de)
    else:
        return count(st*2024, de)

for st in line.split(' '):
    result += count(int(st), 0)

print()
print(result)

