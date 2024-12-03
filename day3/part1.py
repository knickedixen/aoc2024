import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0

for l in lines:
    matches = re.findall('mul\(([\d]{1,3}),([\d]{1,3})\)', l)
    for match in matches:
        result += int(match[0]) * int(match[1])

print(result)
