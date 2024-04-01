import sys

raw_input = sys.stdin.readline
n = input()
g = [[]for i in xrange(n+1)]
edges = []
visited = [0]*(n+1)
height = [0]*(n+1)
for i in xrange(n-1):
    a, b = map(int, raw_input().split())
    g[a].append(b)
    g[b].append(a)
    edges.append((a, b))

def dfs(node, level):
    visited[node] = 1
    height[node] = level
    for child in g[node]:
        if not visited[child]:
            dfs(child, level+1)

dfs(1, 0)
for a, b in edges:
    h1, h2 = height[a], height[b]
    if h1 < h2:
        if h1 % 2 == 0:
            print 1
        else:
            print 0
    else:
        if h2 % 2 == 0:
            print 0
        else:
            print 1
