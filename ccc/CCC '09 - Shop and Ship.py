import sys
from heapq import heappush, heappop
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline
n = int(raw_input())
t = int(raw_input())
dict1 = [[10001 for x in xrange(n+1)] for y in xrange(n+1)]
costs = []
current = float("inf")

def flatten(start, currentCost, vertices, graph, heap, paths):
    nodes = graph[start]
    nodes = [(x, nodes[x]) for x in xrange(n+1) if nodes[x] != 10001]
    for i in nodes:
        neighbour = i[0]
        try:
            cost = vertices[neighbour]
            if i[1] + currentCost < cost:
                vertices[neighbour] = i[1] + currentCost
                paths[neighbour] = i[1] + currentCost
                heappush(heap, (i[1] + currentCost, neighbour))           
        except KeyError:
            pass
        
    while 1:
        try:
            new = heappop(heap)
            minNode = new[1]
            currentMin = new[0]
            test = vertices[minNode]
            break
        except KeyError:
            continue
        except IndexError:
            return paths

    del vertices[minNode]
    return flatten(minNode, currentMin, vertices, graph, heap, paths)

for i in xrange(t):
    line = map(int, raw_input().split())
    x = line[0]
    y = line[1]
    c = line[2]
    old = dict1[x][y]
    if c < old:
        dict1[x][y] = c
        dict1[y][x] = c

k = int(raw_input())

for i in xrange(k):
    line = map(int, raw_input().split())
    city = line[0]
    cost = line[1]
    costs.append((city, cost))

costs.sort(key = lambda x: x[1])
d = int(raw_input())
distances = flatten(d, 0, {x:10001 for x in xrange(1,n+1)}, dict1, [], {x:10001 for x in xrange(1,n+1)})
distances[d] = 0

for i in costs:
    if i[1] + distances[i[0]] < current:
        current = i[1] + distances[i[0]]
    
print current
