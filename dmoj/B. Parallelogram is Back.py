import itertools

p1 = map(int, raw_input().split())
p2 = map(int, raw_input().split())
p3 = map(int, raw_input().split())
points = set()

def parallelogram(p1, p2, p3, p4):
    l = itertools.permutations([p1, p2, p3, p4], 4)
    for group in l:
        p1, p2, p3, p4 = group
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        if x2-x1 == x3-x4 and y2-y1 == y3-y4:
            return True
        if x2-x1 == x4-x3 and y2-y1 == y4-y3:
            return True
        if x3-x1 == x2-x4 and y3-y1 == y2-y4:
            return True
        if x3-x1 == x4-x2 and y3-y1 == y4-y2:
            return True

        return False

for group in itertools.permutations([p1, p2, p3], 3):
    p1, p2, p3 = group
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    rise = y2 - y1
    run = x2 - x1
    p4 = (x3 + run, y3 + rise)
    if parallelogram((x1, y1), (x2, y2), (x3, y3), p4):
        points.add(str(p4[0]) + " " + str(p4[1]))

print len(points)
print "\n".join(points)
