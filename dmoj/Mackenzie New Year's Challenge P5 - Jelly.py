#why do heaps always tle holy dragonballs
import sys
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline
x, y, z = map(int, raw_input().split())
dict2 = [[[0 for j in xrange(z)]for k in xrange(y)]for i in xrange(x)]

for i in xrange(z):
    for j in xrange(y):
        line = list(raw_input().strip())
        
        for k,num in enumerate(line):
            try:
                num = int(num)
            except ValueError:
                num = "J"
                starter = (j,k,i)

            dict2[j][k][i] = num

def path(start, currentCost, weights, vertices, minDict):
    a, b, c = start
    nodes = []

    if any((a==0,b==0,c==0,a==x-1,b==y-1,c==z-1)):
        return currentCost

    if a+1 < x:
        nodes.append((a+1,b,c))
    if a-1 >= 0:
        nodes.append((a-1,b,c))
    if b+1 < y:
        nodes.append((a,b+1,c))
    if b-1 >= 0:
        nodes.append((a,b-1,c))
    if c+1 < z:
        nodes.append((a,b,c+1))
    if c-1 >= 0:
        nodes.append((a,b,c-1))
    
    for neighbour in nodes:
        a, b, c = neighbour
        weight = vertices[a][b][c]
        new = weights[a][b][c]
        if new == "J":
            continue
        if currentCost + new < weight and vertices[a][b][c]:
            vertices[a][b][c] = currentCost + new
            minDict[neighbour] = currentCost + new

    minNode = min(minDict.items(), key=lambda x: x[1])[0]
    a, b, c = minNode
    minimum = vertices[a][b][c]
    vertices[a][b][c] = False
    del minDict[minNode]
    return path(minNode, minimum, weights, vertices, minDict)

a, b, c = starter
thing = [[[1e10 for j in xrange(z)]for k in xrange(y)]for i in xrange(x)]
thing[a][b][c] = 0
print path(starter, 0, dict2, thing, {})
