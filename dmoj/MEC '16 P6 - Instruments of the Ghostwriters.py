import sys, pprint, collections
raw_input = sys.stdin.readline

c, r, m, q = map(int, raw_input().split())
grid = [[1.0 for i in xrange(c+1)]for i in xrange(r+1)]
grid2 = [[1 for i in xrange(c)]for i in xrange(r)]
zeros = [[0 for i in xrange(c+1)]for i in xrange(r+1)]
prefix = [[0 for i in xrange(c)]for i in xrange(r)]
dict1 = collections.defaultdict(int)

for i in xrange(m):
    op, x, y, f = raw_input().split()
    x = int(x)
    y = int(y)
    f = int(f)
    
    if op == "c":
        if f != 0:
            grid[0][x-1] *= f
            grid[0][y] /= f
        else:
            zeros[0][x-1] += 1
            zeros[0][y] -= 1

    if op == "r":
        if f != 0:
            grid[x-1][0] *= f
            grid[y][0] /= f
        else:
            zeros[x-1][0] += 1
            zeros[y][0] -= 1

for y in xrange(r):
    for x in xrange(c):
        if x == 0:
            grid2[y][x] *= grid[y][x]
        else:
            grid2[y][x] *= grid2[y][x-1] * grid[y][x]

for y in xrange(1, r):
    for x in xrange(c):
        grid2[y][x] *= grid2[y-1][x]

pprint.pprint(grid2)
#zeros section
for y in xrange(r):
    for x in xrange(c):
        if x != 0:
            zeros[y][x] += zeros[y][x-1]

for y in xrange(1, r):
    for x in xrange(c):
        zeros[y][x] += zeros[y-1][x]
        
for y in xrange(r):
    for x in xrange(c):
        if zeros[y][x] > 0:
            grid2[y][x] = 0
            
        grid2[y][x] = int(round(grid2[y][x]))

for y in xrange(r):
    for x in xrange(c):
        if x == 0:
            prefix[y][x] += grid2[y][x]
        else:
            prefix[y][x] += prefix[y][x-1] + grid2[y][x]

for y in xrange(1, r):
    for x in xrange(c):
        prefix[y][x] += prefix[y-1][x]

prefix.insert(0, [0]*(c+1))

for i in xrange(1, c+1):
    prefix[i].insert(0, 0)

pprint.pprint(prefix)
for y in xrange(r, 0, -1):
    for x in xrange(c, 0, -1):
        point4 = prefix[y][x]
        for y2 in xrange(y-1, -1, -1):
            for x2 in xrange(x-1, -1, -1):
                point2 = prefix[y2][x]
                point3 = prefix[y][x2]
                point1 = prefix[y2][x2]
                number = point4 + point1 - point2 - point3
                dict1[number] += 1

for i in xrange(q):
    b, o = map(float, raw_input().split())
    if b == o == 0:
        print (c*(c+1)*r*(r+1))/4
        continue
    
    number = o / b
    if number == int(number):
        if int(number) in dict1:
            print dict1[number]

"""
3 3 4 1
c 2 3 2
c 3 3 4
r 2 3 3
c 1 2 0
3 72
"""
