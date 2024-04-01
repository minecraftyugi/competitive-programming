import math, sys

raw_input = sys.stdin.readline
n = int(raw_input())
points = []
total = 0

for x in xrange(1, n+1):
    y = int(raw_input())
    points.append((x, y))

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def direction(p1, p2, p3):
    return(p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])
    
def hull(points):
    upper = []
    for point in points:
        while len(upper) > 1 and direction(upper[-2], upper[-1], point) >= 0:
            upper.pop(-1)

        upper.append(point)
    
    return upper

ordered = hull(points)

for i in xrange(len(ordered) - 1):
    p1 = ordered[i]
    p2 = ordered[i+1]
    total += distance(p1, p2)

print "{0:.1f}".format(total)
