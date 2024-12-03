import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
do = True
for l in lines:
    matches = re.findall('mul\(([\d]{1,3}),([\d]{1,3})\)|(do\(\))|(don\'t\(\))', l)
    for match in matches:
        if match[2] == 'do()':
            do = True
        elif match[3] == "don't()":
            do = False
        elif do:
            result += int(match[0]) * int(match[1])

print(result)
