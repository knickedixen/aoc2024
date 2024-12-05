
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

def order(update):
    while not valid(update):
        for rule in rules:
            try:
                fid = update.index(rule[0])
                lid = update.index(rule[1])
                if fid > lid:
                    update[fid], update[lid] = update[lid], update[fid]
            except:
                continue
    return update

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
    if not valid(update):
        orderedUpdate = order(update)
        result += int(orderedUpdate[int(len(orderedUpdate)/2)])

print(result)
