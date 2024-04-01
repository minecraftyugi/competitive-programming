import sys, bisect
raw_input = sys.stdin.readline
n = int(raw_input())
edges = [0]
for i in xrange(n):
    x,y = map(int, raw_input().split())
    edges.append((x,y))

x = int(raw_input())
q = int(raw_input())
times = []
vertices = {i:1e13 if i!= x else 0 for i in xrange(1,n+1)}

while len(vertices)>0:
    minimum = min(vertices.items(), key=lambda x: x[1])[0]
    currentCost = vertices[minimum]
    times.append(currentCost)
    x1,y1 = edges[minimum]
    del vertices[minimum]

    for neighbour in xrange(1,n+1):
        if neighbour in vertices and neighbour != minimum:
            x2,y2 = edges[neighbour]
            newWeight = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
            if currentCost + newWeight < vertices[neighbour]:
                vertices[neighbour] = currentCost + newWeight

for i in xrange(q):
    num = int(raw_input())
    ans = bisect.bisect_right(times, num)
    print ans
