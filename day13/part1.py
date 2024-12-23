
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

result = 0

for i in range(0, len(lines), 4):
    ax = int(lines[i].split("+")[1].split(',')[0])
    ay = int(lines[i].split("+")[2])
    bx = int(lines[i+1].split("+")[1].split(',')[0])
    by = int(lines[i+1].split("+")[2])
    px = int(lines[i+2].split("=")[1].split(',')[0])
    py = int(lines[i+2].split("=")[2])
    maxb = int(max(px/bx, by/py)) + 1
    maxa = int(max(px/ax, ay/py)) + 1
    price = 0
    for j in range(maxb, 0, -1):
        for k in range(0,maxa,1):
            prx = j*bx + k*ax
            pry = j*by + k*ay
            tot = j + k*3
            if prx == px and pry == py:
                if not price:
                    price = tot
                price = min(tot, price)
    result += price

print(result)
