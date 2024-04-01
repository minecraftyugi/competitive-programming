import collections, sys
raw_input = sys.stdin.readline
sys.setrecursionlimit(40)

n, m, a, b = map(int, raw_input().split())
dict1 = collections.defaultdict(list)

for i in xrange(m):
    x, y = map(int, raw_input().split())
    dict1[x].append(y)
    dict1[y].append(x)

def path(starts, end, graph, visited):
    new = set()

    if len(starts) == 0:
        return "NO SHAHIR!"

    for start in starts:
        neighbours = graph[start]
        if start == end:
            return "GO SHAHIR!"
        for neighbour in neighbours:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)

    return path(new, end, graph, visited)

print path([a], b, dict1, set([a]))
