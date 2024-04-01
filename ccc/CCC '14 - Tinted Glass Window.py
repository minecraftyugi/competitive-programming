#uses difference arrays approach. new data structure learned yay
n = input()
t = input()
xDict = {}
yDict = {}
xIndex = []
yIndex = []
points = []
xLen = set()
yLen = set()
ans = 0

for i in xrange(n):
    x1, y1, x2, y2, t1 = map(int, raw_input().split())
    xLen.add(x1)
    xLen.add(x2)
    yLen.add(y1)
    yLen.add(y2)
    points += [(x1, x2, y1, y2, t1)]

lists = [[0 for i in xrange(len(xLen))]for j in xrange(len(yLen))]

xIndex = list(sorted(xLen))
for i, x in enumerate(xIndex):
    xDict[x] = i

yIndex = list(sorted(yLen))
for i, y in enumerate(yIndex):
    yDict[y] = i

for point in points:
    xStart = xDict[point[0]]
    xEnd = xDict[point[1]]
    yStart = yDict[point[2]]
    yEnd = yDict[point[3]]
    value = point[4]
    for i in xrange(yStart, yEnd):
        lists[i][xStart] += value
        lists[i][xEnd] -= value

for i in xrange(len(xLen)-1):
    for j in xrange(len(yLen)-1):
        if lists[j][i] >= t:
            xStart = xIndex[i]
            xEnd = xIndex[i+1]
            yStart = yIndex[j]
            yEnd = yIndex[j+1]
            ans += (xEnd - xStart) * (yEnd - yStart)

        lists[j][i+1] += lists[j][i]

print ans
