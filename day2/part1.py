
def validLevel(diff, pdiff):
    if abs(diff) > 3 or abs(diff) < 1:
        return False
    elif pdiff != 0:
        if pdiff > 0 and diff < 0:
            return False
        elif pdiff < 0 and diff > 0:
            return False

    return True

def validReport(curr, parts, pdiff):
    if not parts:
        return True

    next = parts.pop()
    diff = curr - next

    if not validLevel(diff, pdiff):
        return False

    return validReport(next, parts, diff)


result = 0

with open("input.txt") as file:
    for line in file:
        parts = list(map(int, line.strip().split()))
        if validReport(parts.pop(), parts, 0):
            result += 1

print(result)
