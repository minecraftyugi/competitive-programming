import math

def area(p1, p2, p3):
    return 1.5 * abs(direction(p1, p2, p3))

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calcAngle(p1, p2, p3):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    aLen = math.sqrt(x**2 +  y**2)
    x2 = p3[0] - p2[0]
    y2 = p3[1] - p2[1]
    bLen = math.sqrt(x2**2 + y2**2)
    dot = x*x2 + y*y2
    if dot == 0:
        angle = math.pi / 2
    elif x > 0:
        angle = math.acos(dot/(aLen*bLen))
    else:
        angle = math.pi - math.acos(dot/(aLen*bLen))

    return angle, aLen

def orderPoints(points, startX, startY):
    visited = {}
    possible = {((startX, startY), -1)}
    order = []

    for point in points:
        angle, aLen = calcAngle(point, (startX, startY), (point[0], startY))         
        if angle in visited:
            if aLen > visited[angle][0]:
                possible.remove((visited[angle][1], angle))
                visited[angle] = (aLen, point)
                possible.add((point, angle))              
        else:
            visited[angle] = (aLen, point)
            possible.add((point, angle))
        
    for point in possible:
        order.append(point)

    order.sort(key = lambda x: x[1])
    return [i[0]for i in order]

def direction(p1, p2, p3):
    return(p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])
    
def hull(points):
    order = []
    order.extend(points[:3])
    for point in points[3:]:
        while direction(order[-2], order[-1], point) <= 0:
            order.pop(-1)

        order.append(point)
    
    return order

def pairs(p):
    total = []
    maximum = 0
    n = len(p) - 1
    i = 0
    j = 1
    
    while area(p[n], p[i], p[j+1]) > area(p[n], p[i], p[j]):
        j += 1

    k = j
    while i <= j and k <= n:
        total.append((p[i], p[k]))
        maximum = max(maximum, distance(p[i], p[k]))
        
        while k < n and area(p[i], p[i+1], p[k+1]) > area(p[i], p[i+1], p[k]):
            total.append((p[i], p[k]))
            k += 1
            maximum = max(maximum, distance(p[i], p[k]))
        
        i += 1

    return maximum

def brute(points):
    maximum = 0
    if len(points) != 3:
        for a in points:
            for b in points:
                maximum = max(maximum, distance(a, b))
    else:
        p1, p2, p3 = points
        a = distance(p1, p2)
        b = distance(p2, p3)
        c = distance(p1, p3)
        a, b, c = sorted([a, b, c])
        if a**2 + b**2 <= c**2:
            maximum = max(a, b, c)
        else:
            s = (a + b + c) / 2
            maximum = a * b * c / (2 * math.sqrt(s*(s-a)*(s-b)*(s-c)))

    return maximum

n = input()
lists = []
ans = []
dict1 = {}

for i in xrange(n):
    point = map(float, raw_input().split())
    lists.append(tuple(point))

if len(lists) < 4:
   print"{0:.2f}".format(brute(lists))
else:  
    lists.sort(key = lambda x:(x[1], x[0]))
    start = lists[0]
    ordered = orderPoints(lists[1:], start[0], start[1])
    points = hull(ordered)
    ans = pairs(points)
    print"{0:.2f}".format(ans)
