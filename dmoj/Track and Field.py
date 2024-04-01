import math
straight = 84.39
lane = 1.22
radius = 36.5
exchange = 20

for i in xrange(1, 9):
    inside = ((radius + (lane * (i - 1))) * 2 * math.pi) + (straight * 2)
    outside = ((radius + (lane * i)) * 2 * math.pi) + (straight * 2)
    insideS = inside - 400
    if inside < 400:
        insideS = 400
    outsideS = outside - 400
    print "Lane "+str(i)+":"
    print "Inside: "+str(inside)
    print "Outside: "+str(outside)
    print ""
