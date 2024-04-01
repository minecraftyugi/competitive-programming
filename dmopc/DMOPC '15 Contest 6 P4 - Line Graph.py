import sys
sys.setrecursionlimit(100000)
n, k = map(int, raw_input().split())
thing = map(int, raw_input().split())
edges = []
ans = {i:i for i in xrange(1, n+1)}
answer = 0

for i in xrange(1, n+1):
    if i + k <= n:
        edges.append((0, (i, i + k)))
    else:
        break

for i in xrange(1, n):
    edges.append((thing[i-1], (i, i + 1)))

edges.sort(key = lambda x: x[0])

def parent(start, visited, graph):
    end = graph[start]

    if start == end:
        for i in visited:
            graph[i] = end
            
        return end

    visited.append(end)
    return parent(end, visited, graph)

for group in edges:
    thing = group[1]
    x, y = thing
    parent1 = parent(x, [x], ans)
    parent2 = parent(y, [y], ans)

    if parent1 != parent2:
        ans[parent1] = parent2
        answer += group[0]

print answer
