n = float(input())
m = float(input())
p = float(input())
q = float(input())
p1 = (p, 0)
p2 = (n, q)
wall = "r"
total = 0
visited = set([p1])

#top: y = m
#bottom: y = 0
#left: x = 0
#right: x = n

def valid(x, y):
    if y == m or y == 0:
        if 0 <= x < 5 or n-5 < x <= n:
            return True
        
    if x == 0 or x == n:
        if 0 <= y < 5 or m-5 < y <= m:
            return True
    
    return False

while 1:
    if valid(round(p2[0], 0), round(p2[1], 0)):
        print total
        break

    if p2 in visited:
        print 0
        break

    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    if wall == "t":
        p0 = ((-slope*p1[0] + p1[1]) / (0 - slope), 0)
        diff = abs(p0[0] - p2[0])
        p3 = (p2[0] + diff, 0)
        if p3 == p0:
            p3 = (p2[0] - diff, 0)

        slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
        if p3[0] > n:
            wall = "r"
            y = slope2*n -slope2*p3[0] + p3[1]
            p3 = (n, y)
        elif p3[0] < 0:
            wall = "l"
            y = slope2*0 -slope2*p3[0] + p3[1]
            p3 = (0, y)
        else:
            wall = "b"

        #print p3, "T"
    elif wall == "b":
        p0 = ((-slope*p1[0] + p1[1] - m) / (0 - slope), m)
        diff = abs(p0[0] - p2[0])
        p3 = (p2[0] + diff, m)
        if p3 == p0:
            p3 = (p2[0] - diff, m)

        slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
        if p3[0] > n:
            wall = "r"
            y = slope2*n -slope2*p3[0] + p3[1]
            p3 = (n, y)
        elif p3[0] < 0:
            wall = "l"
            y = slope2*0 -slope2*p3[0] + p3[1]
            p3 = (0, y)
        else:
            wall = "t"

        #print p3, "B"
    elif wall == "l":
        p0 = (n, slope*n -slope*p1[0] + p1[1])
        diff = abs(p0[1] - p2[1])
        p3 = (n, p2[1] + diff)
        if p3 == p0:
            p3 = (n, p2[1] - diff)

        slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
        if p3[1] > m:
            wall = "t"
            x = (-slope2*p3[0] + p3[1] - m) / (0 - slope2)
            p3 = (x, m)
        elif p3[1] < 0:
            wall = "b"
            x = (-slope2*p3[0] + p3[1] - 0) / (0 - slope2)
            p3 = (x, 0)
        else:
            wall = "r"

        #print p3, "L"
    else:
        p0 = (0, -slope*p1[0] + p1[1])
        diff = abs(p0[1] - p2[1])
        p3 = (0, p2[1] + diff)
        if p3 == p0:
            p3 = (0, p2[1] - diff)

        slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
        if p3[1] > m:
            wall = "t"
            x = (-slope2*p3[0] + p3[1] - m) / (0 - slope2)
            p3 = (x, m)
        elif p3[1] < 0:
            wall = "b"
            x = (-slope2*p3[0] + p3[1] - 0) / (0 - slope2)
            p3 = (x, 0)
        else:
            wall = "l"

        #print p3, "R"

    visited.add(p2)
    p1, p2 = p2, p3
    total += 1
