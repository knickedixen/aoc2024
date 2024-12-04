
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

mases = []
result = 0
for lid, l in enumerate(lines):
    for cid,c in enumerate(l):
        if c == "A":
            if lid+1 >= len(lines) or cid+1 >= len(l) or lid-1 < 0 or cid-1 < 0:
                continue

            tl = lines[lid-1][cid-1]
            tr = lines[lid-1][cid+1]
            bl = lines[lid+1][cid-1]
            br = lines[lid+1][cid+1]

            tlbr = tl+br
            trbl = tr+bl
            if (tlbr == "MS" or tlbr == "SM") and (trbl == "MS" or trbl == "SM"):
                result +=1


print(result)
