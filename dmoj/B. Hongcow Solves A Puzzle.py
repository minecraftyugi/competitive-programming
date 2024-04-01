n, m = map(int, raw_input().split())
points = set()
topl = ""
topr = ""
bottoml = ""
bottomr = ""

for i in xrange(n):
    line = raw_input()
    for j in xrange(m):
        if line[j] == "X":
            if topl == "":
                topl = (i, j)
            else:
                pass
            if topr == "":
                topr = (i, j)
            else:
                if i == topr[0] and j > topr[1]:
                    topr = (i, j)
            if bottoml == "":
                bottoml = (i, j)
            else:
                if i > bottoml[0]:
                    bottoml = (i, j)
            if bottomr == "":
                bottomr = (i, j)
            else:
                if i > bottomr[0]:
                    bottomr = (i, j)
                elif i == bottomr[0] and j > bottomr[1]:
                    bottomr = (i, j)

            points.add((i,j))
            
if len(points):
    if bottoml[1] == topl[1] and bottomr[1] == topr[1]:
        valid = True
        for i in xrange(topl[0], bottoml[0] + 1):
            for j in xrange(topl[1], topr[1] + 1):
                if (i, j) not in points:
                    valid = False

        if valid:
            print "YES"
        else:
            print "NO"
    else:
        print "NO"
else:
    print "NO"
