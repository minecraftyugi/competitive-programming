t = int(raw_input())
x1, y1 = map(int, raw_input().split())
x2, y2 = map(int, raw_input().split())
dict1 = {(a,b):[] for a in xrange(17) for b in xrange(17)}

for i in xrange(17):
    for j in xrange(17):
        if i+1<=16 and j+1<=16:
            dict1[(i, j)] += (i+1, j+1),
        if i+1<=16 and j-1>=0:
            dict1[(i, j)] += (i+1, j-1),
        if i-1>=0 and j+1<=16:
            dict1[(i, j)] += (i-1, j+1),
        if i-1>=0 and j-1>=0:
            dict1[(i, j)] += (i-1, j-1),

def paths(start, end, time, graph, visited):
    new = set()
    add = set()
    if end in start:
        return "It takes {} minute(s) to get to ({}, {}).".format(time, end[0], end[1])
    if time > t:
        return "Cannot get there on time."
    if len(start) == 0:
        return "Cannot physically get there."
    for node in start:
        try:
            for neighbour in graph[node]:
                if neighbour not in visited:
                    add.add(neighbour)
                    new.add(neighbour)
        except KeyError:
            pass

    visited = add | visited
    return paths(new, end, time + 1, graph, visited)

print paths([(x1, y1)], (x2, y2), 0, dict1, set())
