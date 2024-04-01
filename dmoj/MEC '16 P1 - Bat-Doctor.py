import math
r, c = map(int, raw_input().split())
points = []
count = 0

for y in xrange(r):
    line = raw_input()
    for x, value in enumerate(line):
        if value == "X":
            points.append((x*1.0, y*1.0))
            count += 1

points.sort(key = lambda x: x[0])

for i in xrange(count - 1):
    x2, y2 = points[i]
    x3, y3 = points[i+1]
    x1, y1 = x2, -1    
    len1 = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    len2 = math.sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2))
    vx1, vy1 = x2 - x1, y2 - y1
    vx2, vy2 = x2 - x3, y2 - y3
    dot = vx1 * vx2 + vy1 * vy2
    dist = abs(len1 * len2)
    angle = round(math.degrees(math.acos(dot / dist)), 3)
    print "{0:.3f}".format(angle)

if count <= 1:
    print "0.000"
