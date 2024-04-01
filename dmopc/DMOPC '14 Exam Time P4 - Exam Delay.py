import heapq, math

v = input()
e = input()
G = [[]for i in xrange(1001)]

for i in xrange(e):
    m, n, d, s = map(int, raw_input().split())
    cost = 60.0*d/s
    G[m].append((n, cost))
    G[n].append((m, cost))

visited = [0]*1001
costs = [1e9]*1001
costs[1] = 0
pathcount = [1e9]*1001
pathcount[1] = 0
heap = [(0, 1)]
while heap:
    cost, node = heapq.heappop(heap)
    if visited[node]:
        continue

    visited[node] = 1
    newpath = pathcount[node] + 1
    for neighbour, time in G[node]:
        newcost = cost + time
        if newcost == costs[neighbour]:
            pathcount[neighbour] = min(pathcount[neighbour], newpath)
            
        if not visited[neighbour] and newcost < costs[neighbour]:
            pathcount[neighbour] = newpath
            costs[neighbour] = newcost
            heapq.heappush(heap, (newcost, neighbour))

print pathcount[v]
print int(round(costs[v] * 4 / 3 - costs[v]))
