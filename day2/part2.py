
def validLevel(diff, pdiff):
    if abs(diff) > 3 or abs(diff) < 1:
        return False
    elif pdiff != 0:
        if pdiff > 0 and diff < 0:
            return False
        elif pdiff < 0 and diff > 0:
            return False

    return True

def validReport(curr, parts, pdiff, skipped):
    if not parts:
        return True

    next = parts.pop()
    diff = curr - next

    if not validLevel(diff, pdiff):
        if skipped:
            return False
        else:
            return validReport(curr, parts, pdiff, True)

    return validReport(next, parts, diff, skipped)


result = 0

with open("input.txt") as file:
    for line in file:
        parts = list(map(int, line.strip().split()))
        partsR = list(reversed(parts))
        if validReport(parts.pop(), parts, 0, False) or validReport(partsR.pop(), partsR, 0, False):
            result += 1

print(result)
