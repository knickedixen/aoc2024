
def valid(update):
    for rule in rules:
        try:
            fid = update.index(rule[0])
            lid = update.index(rule[1])
            if fid > lid:
                return False
        except:
            continue
    return True

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0
rules = []
updates = []
for l in lines:
    if "|" in l:
        rules.append(l.split("|"))
    elif l:
        updates.append(l.split(','))

for update in updates:
    if valid(update):
        result += int(update[int(len(update)/2)])

print(result)
