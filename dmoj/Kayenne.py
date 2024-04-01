import collections, math

for i in xrange(10):
    homeX, homeY = map(int, raw_input().split())
    points = []
    possible = [(homeX, homeY)]
    
    for i in xrange(20*5):
        x, y, party = raw_input().split()
        x = int(x)*1.0
        y = int(y)*1.0
        points.append((x, y, party))

    for i in xrange(51):
        for j in xrange(51):
            newX = homeX + i
            newY = homeY + j
            if i != 0 and j != 0:
                if math.sqrt((newX-homeX)**2 + (newY-homeY)**2) <= 50:
                    if i == 0:
                        possible.append((newX, newY))
                        possible.append((newX, newY-2*j))
                    elif j == 0:
                        possible.append((newX, newY))
                        possible.append((newX-2*i, newY))
                    else:
                        possible.append((newX, newY))
                        possible.append((newX, newY-2*j))
                        possible.append((newX-2*i, newY))
                        possible.append((newX-2*i, newY-2*j))

    r = 0
    d = 0
    
    for thing in possible:
        x1, y1 = thing
        dict1 = collections.defaultdict(list)
        
        for point in points:
            x2, y2, party = point
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            dict1[dist].append(point)

        count = 0
        finalR = 0
        finalD = 0
        
        while 1:
            minimum = min(dict1)
            length = len(dict1[minimum])
            #if length > 1:print length, count
            count += length
            republicans = 0
            democrats = 0
            
            for stuff in dict1[minimum]:
                party = stuff[2]
                if party == "D":
                    democrats += 1
                else:
                    republicans += 1

            if length == 1:
                if count < 3:
                    finalR += republicans
                    finalD += democrats
                else:
                    finalR += republicans
                    finalD += democrats
                    break
            else:
                if count < 3:
                    if republicans > democrats:
                        finalR += republicans
                    else:
                        finalD += democrats
                else:
                    if republicans > democrats:
                        finalR += 1
                    else:
                        finalD += 1

                    break
            
            del dict1[minimum]
            #print dict1[minimum], thing

        if finalR > finalD:
            r += 1
        else:
            d += 1

    print round(d*1.0/(r+d)*100, 1)

"""
-81 83
15 -198 R
-17 89 R
197 -174 R
-67 89 D
180 -101 D
-78 -173 R
182 121 D
-129 179 R
-100 -53 D
64 -61 D
-123 -152 D
-15 -67 R
20 194 D
125 16 D
133 -28 D
19 -9 R
121 168 D
165 -39 R
-170 -3 D
-27 61 D
"""
