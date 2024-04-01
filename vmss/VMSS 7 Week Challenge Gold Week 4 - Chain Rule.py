import sys, collections, heapq

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
g = collections.defaultdict(list)
for i in xrange(m):
    a, b, t = map(int, raw_input().split())
    g[a].append((b, t))
    g[b].append((a, t))

def shortest(start, cost, dist, visited, heap):
    while 1:
        for node, w in g[start]:
            val = cost + w
            if val < dist[node]:
                dist[node] = val
                heapq.heappush(heap, (val, node))

        found = False
        while heap and not found:
            cost, start = heapq.heappop(heap)
            if not visited[start]:
                found = True
                visited[start] = True

        if not found:
            break
        
dist1 = [10**9]*n
dist1[0] = 0
visited = [0]*n
visited[0] = 1
shortest(0, 0, dist1, visited, [(0,0)])
dist2 = [10**9]*n
dist2[n-1] = 0
visited = [0]*n
visited[n-1] = 1
shortest(n-1, 0, dist2, visited, [(0,n-1)])
maximum = 0
for i in xrange(n):
    maximum = max(maximum, dist1[i] + dist2[i])

print maximum
