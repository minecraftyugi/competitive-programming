import collections

dict1 = collections.defaultdict(list)
routes = []
count = 0

while 1:
    x, y = raw_input()
    if x == y == "*":
        break
    else:
        routes.append(x+y)
        dict1[x].append(y)
        dict1[y].append(x)

def paths(starts, end, disconnect, graph, visited):
    new = set()
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            if start+neighbour == disconnect or neighbour+start == disconnect:
                continue
            if neighbour == end:
                return (0, 0)
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)

    if len(new) == 0:
        return (1, disconnect)
    else:
        return paths(new, end, disconnect, graph, visited)

for route in routes:
    add, road = paths(["A"], "B", route, dict1, set())
    count += add
    if add == 1:
        print road

print "There are {} disconnecting roads.".format(count)
