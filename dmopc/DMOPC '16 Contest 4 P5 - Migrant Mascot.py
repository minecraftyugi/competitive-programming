import sys, collections

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
g = [[]for i in xrange(n+1)]
edges = []
for i in xrange(m):
    a, b, p = map(int, raw_input().split())
    edges.append((a, b, p))
    g[a].append((b, p))
    g[b].append((a, p))

edges.sort(key=lambda x: x[2], reverse=True)
parents = [i for i in xrange(n+1)]
g2 = collections.defaultdict(list)
def find_parent(node, graph, visited):
    if graph[node] == node:
        for child in visited:
            graph[child] = node

        return node
    else:
        visited.append(node)
        return find_parent(graph[node], graph, visited)

for a, b, val in edges:
    p1 = find_parent(parents[a], parents, [])
    p2 = find_parent(parents[b], parents, [])
    if p1 != p2:
        parents[p1] = p2
        g2[a].append((b, val))
        g2[b].append((a, val))

dists = [0]*(n+1)
visited = [0]*(n+1)
visited[1] = 1
def dfs(node, graph, minimum, visited):
    for child, val in graph[node]:
        if not visited[child]:
            visited[child] = 1
            new_min = min(minimum, val)
            dists[child] = new_min
            dfs(child, graph, new_min, visited)

dfs(1, g2, 1<<30, visited)
print "\n".join(map(str, dists[1:]))
