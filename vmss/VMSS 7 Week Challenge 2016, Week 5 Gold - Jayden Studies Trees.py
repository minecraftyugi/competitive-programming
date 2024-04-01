import sys, collections
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline

n = input()
dict1 = collections.defaultdict(set)
ans = 0

for i in xrange(n-1):
    a, b = map(int, raw_input().split())
    dict1[a].add(b)
    dict1[b].add(a)
    start = a

def paths(starts, length, graph, visited):
    new = set()
    for start in starts:
        if start in graph:
            neighbours = graph[start]
            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    new.add(neighbour)

    if len(new) == 0:
        return starts, length
    
    return paths(new, length + 1, graph, visited)

path, things = paths([a], 0, dict1, set())

for i in path:
    things, maxLen = paths([i], 0, dict1, set())
    if maxLen > ans:
        ans = maxLen

print ans
