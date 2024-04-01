import sys, collections
sys.setrecursionlimit(100000)
thing = map(int, raw_input().split())
cities = thing[0]
roads = thing[1]
destinations = thing[2]
dict1 = collections.defaultdict(dict)
visit = []
parents = {i:i for i in xrange(1, cities + 1)}
lowestCost = 1e6

for i in xrange(roads):
    line = map(int, raw_input().split())
    x = line[0]
    y = line[1]
    lists = [x,y]
    lists.sort()
    x = lists[0]
    y = lists[1]
    weight = line[2]
    try:
        old = dict1[x][y]
        dict1[x][y] = max(old, weight)
    except KeyError:
        dict1[x][y] = weight

for i in xrange(destinations):
    d = int(raw_input())
    visit.append(d)

edges = [(dict1[x][y], x, y) for x in dict1.keys() for y in dict1[x].keys()]
edges.sort(reverse=True)

def parent(start, graph, visited):
    end = graph[start]
    if start == end:
        for i in visited:
            if graph[i] != start:
                graph[i] = start
        return start
    
    visited.append(end)
    return parent(end, graph, visited)

for i in edges:
    cost = i[0]
    a = i[1]
    b = i[2]
    parent1 = parent(a, parents, [a])
    parent2 = parent(b, parents, [b])
    if parent1 != parent2:
        parents[parent1] = parent2
        if cost < lowestCost:
            try:
                visit.remove(a)
                lowestCost = cost
            except ValueError:
                pass
            try:
                visit.remove(b)
                lowestCost = cost
            except ValueError:
                pass

    if visit == []:
        break
            
print lowestCost
