
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

mases = []
for lid, l in enumerate(lines):
    for cid,c in enumerate(l):
        if c == "X":
            mases.append(lines[lid][cid+1:cid+4])
            mases.append(lines[lid][cid-3:cid][::-1])
            if lid+3 < len(lines):
                mases.append(lines[lid+1][cid] + lines[lid+2][cid] + lines[lid+3][cid])
                if len(lines[lid+3]) > cid+3:
                    mases.append(lines[lid+1][cid+1] + lines[lid+2][cid+2] + lines[lid+3][cid+3])
                if cid-3 >= 0:
                    mases.append(lines[lid+1][cid-1] + lines[lid+2][cid-2] + lines[lid+3][cid-3])
            if lid-3 >= 0:
                mases.append(lines[lid-1][cid] + lines[lid-2][cid] + lines[lid-3][cid])
                if len(lines[lid-3]) > cid+3:
                    mases.append(lines[lid-1][cid+1] + lines[lid-2][cid+2] + lines[lid-3][cid+3])
                if cid-3 >= 0:
                    mases.append(lines[lid-1][cid-1] + lines[lid-2][cid-2] + lines[lid-3][cid-3])

print(len([i for i, x in enumerate(mases) if x == "MAS"]))

