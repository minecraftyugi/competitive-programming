sx, sy, sz = map(int, raw_input().split())
tx, ty, tz = map(int, raw_input().split())
closest = ((sx - tx)**2 + (sy - ty)**2 + (sz - tz)**2)**.5
x = 1
y = 0
z = 0
line = raw_input()
while line != "E":
    dist, direction = line.split()
    dist = int(dist)
    sx += x * dist
    sy += y * dist
    sz += z * dist
    closest = min(closest, ((sx - tx)**2 + (sy - ty)**2 + (sz - tz)**2)**.5)
    if x:
        if direction == "L":
            y = x
            x = 0
        elif direction == "R":
            y = -x
            x = 0
        elif direction == "U":
            z = 1
            x = 0
        else:
            z = -1
            x = 0
    elif y:
        if direction == "L":
            x = -y
            y = 0
        elif direction == "R":
            x = y
            y = 0
        elif direction == "U":
            z = 1
            y = 0
        else:
            z = -1
            y = 0
    else:
        if direction == "L":
            pass
