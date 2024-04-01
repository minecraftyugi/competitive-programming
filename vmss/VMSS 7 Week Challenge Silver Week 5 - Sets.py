import sys

raw_input = sys.stdin.readline
n = input()
sets = set()
elements = [set() for i in range(26)]
g = [set() for i in range(26)]
g2 = [set() for i in range(26)]
for i in xrange(n):
    a, _, b = raw_input().split()
    a, b = ord(a)-65, ord(b)-65
    sets.add(a)
    if b <= 25:
        sets.add(b)
        g[a].add(b)
        g2[b].add(a)
    else:
        elements[a].add(chr(b+65))

def dfs(node, graph):
    global time
    visited[node] = 1
    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph)

    time += 1
    times.append((time, node))

def explore(node, original, graph):
    visited[node] = 1
    parents[node] = original
    groups[original].update(elements[node])
    for child in graph[node]:
        if not visited[child]:
            explore(child, original, graph)
        else:
            groups[original].update(groups[parents[child]])
    
visited = [0]*26
times = []
time = 0
for ch in sets:
    if not visited[ch]:
        dfs(ch, g2)

times.sort(reverse=True)
parents = [i for i in range(26)]
visited = [0]*26
groups = {}
for time, node in times:
    if not visited[node]:
        groups[node] = set()
        explore(node, node, g)

for ch in sorted(sets):
    s = chr(ch+65) + " = {"
    s += ",".join(sorted(groups[parents[ch]])) + "}"
    print s
