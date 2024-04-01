import sys, heapq
raw_input = sys.stdin.readline
sys.setrecursionlimit(100000)
k, n, m = map(int, raw_input().split())
dict1 = [[[] for x in xrange(n+1)] for y in xrange(n+1)]

for i in xrange(m):
    a, b, t, h = map(int, raw_input().split())
    dict1[a][b].append((t, h))
    dict1[b][a].append((t, h))

def shortest(start, end, currentCost, hull, graph, vertices, heap):
    if start == end:
        return currentCost
    
    nodes = graph[start]
    nodes = [(i, x[0], x[1]) for i in xrange(n+1) for x in nodes[i]]
    for i in nodes:
        neighbour = i[0]
        newHull = hull - i[2]
        try:
            current = vertices[(neighbour, newHull)]
            if i[1] + currentCost < current and newHull > 0:
                vertices[(neighbour, newHull)] = i[1] + currentCost
                heapq.heappush(heap, (i[1] + currentCost, neighbour, newHull))  
        except KeyError:
            continue

    while 1:
        try:
            new = heapq.heappop(heap)
            newCost = new[0]
            newStart = new[1]
            newHull = new[2]
            test = vertices[(newStart, newHull)]
            break
        except KeyError:
            continue
        except IndexError:
            return -1

    del vertices[(newStart, newHull)]
    return shortest(newStart, end, newCost, newHull, graph, vertices, heap)

a, b = map(int, raw_input().split())
thing = {(x, i):1e9 for x in xrange(1,n+1) for i in xrange(1,k+1)}
print shortest(a, b, 0, k, dict1, thing, [])
