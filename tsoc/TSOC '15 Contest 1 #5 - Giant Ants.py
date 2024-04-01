import collections
n, m = map(int, raw_input().split())
dict1 = collections.defaultdict(list)
ants = set()

for i in xrange(m):
    x, y = map(int, raw_input().split())
    dict1[x].append(y)
    dict1[y].append(x)

w = int(raw_input())

for i in xrange(w):
    ants.add(int(raw_input()))

def paths(start, end, moves, blocked, visited, graph):
    new = set()
    add = set()
    if end in start:
        return moves
    if len(start) == 0:
        return "sacrifice bobhob314"
    if moves % 4 == 0 and moves:
        for node in blocked:
            for neighbour in graph[node]:
                add.add(neighbour)
        blocked = blocked.union(add)
        visited = visited.union(blocked)
        add.clear()

    for node in start:
        for neighbour in graph[node]:
            if neighbour not in visited:
                new.add(neighbour)
                add.add(neighbour)

    visited = visited.union(add)
    return paths(new, end, moves+1, blocked, visited, graph)

print paths([1], n, 0, ants, {1}, dict1)
