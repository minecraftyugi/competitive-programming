import sys, heapq
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline
thing = map(int, raw_input().split())
n = thing[0]
m = thing[1]
dict1 = [[1e5 for i in xrange(n+1)] for j in xrange(n+1)]

for i in xrange(m):
    line = map(int, raw_input().split())
    x = line[0]
    y = line[1]
    w = line[2]
    old = dict1[x][y]
    dict1[x][y] = min(w, old)
    dict1[y][x] = min(w, old)

def paths(start, currentCost, graph, vertices, vertices2, heap):
    nodes = graph[start]
    nodes = [(i, nodes[i]) for i in xrange(n+1) if nodes[i] != 1e5]
    for i in nodes:
        neighbour = i[0]
        try:
            weight = vertices[neighbour]
            new = i[1]
            if currentCost + new < weight:
                vertices[neighbour] = currentCost + new
                vertices2[neighbour] = currentCost + new
                heapq.heappush(heap, (currentCost + new, neighbour))
        except KeyError:
            pass
    
    while 1:
        try:
            new = heapq.heappop(heap)
            newCost = new[0]
            newStart = new[1]
            test = vertices[newStart]
            break
        except IndexError:
            return vertices2
        except KeyError:
            pass

    del vertices[newStart]
    return paths(newStart, newCost, graph, vertices, vertices2, heap)

ans = paths(1, 0, dict1, {i:1e5 for i in xrange(1,n+1)}, {i:1e5 for i in xrange(1,n+1)}, [])

for i in xrange(1, n+1):
    if i == 1:
        print 0
    elif ans[i] == 1e5:
        print -1
    else:
        print ans[i]
