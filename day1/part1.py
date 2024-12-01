import re

f = open("input.txt")
if not f:
    exit()

total = 0
left = []
right = []
while True:
    line = f.readline()
    if not line:
        break
    
    matches = re.search('^([\d]*)[\s]*([\d]*)$', line)

    left.append(int(matches.group(1)))
    right.append(int(matches.group(2)))

left.sort()
right.sort()

for i in range(len(left)):
    diff = left[i] - right[i]
    total += abs(diff)

print(total)
