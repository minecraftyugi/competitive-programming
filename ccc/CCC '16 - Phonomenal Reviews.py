import sys, collections, heapq
raw_input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, raw_input().split())
stores = map(int, raw_input().split())
storeSet = set(stores)
storeSet2 = set(stores)
dict1 = collections.defaultdict(list)
distances = {}

for i in xrange(n-1):
    x, y = map(int, raw_input().split())
    dict1[x].append(y)
    dict1[y].append(x)

def bfs(starts, restaurants, maxNode, graph, visited):
    new = set()
    
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)
                if neighbour in restaurants:
                    maxNode = neighbour

    if len(new) == 0:
        return maxNode
        
    return bfs(new, restaurants, maxNode, graph, visited)

def bfs2(starts, chain, graph, visited):
    new = set()

    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)
                if neighbour in chain:
                    return neighbour

    return bfs2(new, chain, graph, visited)

def path(start, end, currentCost, restaurants, graph, vertices, parents, heap):
    if start == end:
        ans = set([first, end])
        final = end
        while 1:
            final = parents[final]
            if final in restaurants:
                ans.add(final)
            if final == first:
                break
                
        return currentCost, ans
    
    neighbours = graph[start]

    for neighbour in neighbours:
        if neighbour in vertices:
            if currentCost + 1 < vertices[neighbour]:
                heapq.heappush(heap, (currentCost + 1, neighbour))
                parents[neighbour] = start

    while 1:
        try:
            newCost, node = heapq.heappop(heap)
            test = vertices[node]
            break
        except KeyError:
            pass

    del vertices[node]
    return path(node, end, newCost, restaurants, graph, vertices, parents, heap)

first = bfs([stores[0]], storeSet, stores[0], dict1, set())
last = bfs([first], storeSet, first, dict1, set())
v = {i:1e10 for i in xrange(n)}
p = {i:0 for i in xrange(n)}
answer, remove = path(first, last, 0, storeSet, dict1, v, p, [])

for point in remove:
    storeSet2.remove(point)

for point in storeSet2:
    first = point
    last = bfs2([point], remove, dict1, set())
    v = {i:1e10 for i in xrange(n)}
    p = {i:0 for i in xrange(n)}
    cost, thing = path(first, last, 0, storeSet, dict1, v, p, [])
    distances[first] = thing

lists = distances.items()
lists.sort(key = lambda x: len(x[1]), reverse=True)

for thing in lists:
    check, points = thing
    length = len(points) - 1
    if check in storeSet2:
        answer += length * 2
        for point in points:
            storeSet2.discard(point)

print answer
print storeSet2
