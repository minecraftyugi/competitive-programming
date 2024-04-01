import sys, collections
raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
dict1 = collections.defaultdict(set)

for i in xrange(m):
    a, b = map(int, raw_input().split())
    dict1[a].add(b)
    dict1[b].add(a)

x, y = map(int, raw_input().split())

def paths(start, end, graph, visited):
    if len(start) == 0:
        return 0

    new = set()
    for i in start:
        neighbours = graph[i]
        for neighbour in neighbours:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)
                if neighbour == end:
                    return 1

    return paths(new, end, graph, visited)

print paths([x], y, dict1, set([x]))
