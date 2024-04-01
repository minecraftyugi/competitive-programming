import sys, collections

raw_input = sys.stdin.readline
b, q = map(int, raw_input().split())
beacons = []
g = [[]for i in xrange(b)]
for i in xrange(b):
    beacons.append(map(int, raw_input().split()))

for i in xrange(b):
    x, y, r = beacons[i]
    dist = r**2
    for j in xrange(b):
        if i == j:
            continue
        
        x2, y2, r2 = beacons[j]
        if (x2-x)**2 + (y2-y)**2 <= dist:
            g[i].append(j)

def explore(start, end, graph):
    q = collections.deque()
    q.append(start)
    while q:
        node = q.popleft()
        for child in graph[node]:
            if not visited[child]:
                if child == end:
                    return 1
                
                visited[child] = 1
                q.append(child)

    return visited[end]

for i in xrange(q):
    x, y = map(int, raw_input().split())
    visited = [0]*b
    visited[x-1] = 1
    if explore(x-1, y-1, g):
        print "YES"
    else:
        print "NO"
