import collections, heapq

s, r = map(int, raw_input().split())
u, v, t = map(int, raw_input().split())
q = 0
dict1 = {}
dict2 = collections.defaultdict(dict)

for i in xrange(r):
    group = map(int, raw_input().split())
    q += group[0]
    dict1[i+1] = group[1:]

for i in xrange(q):
    group = map(int, raw_input().split())
    route = group[0]
    station = group[1]
    times = group[3:]
    dict2[station][route] = sorted(times)

def paths(start, end, currentCost, currentTime, graph, vertices, heap):
    if start == end:
        return currentCost
    
    routes = graph[start].keys()

    for route in routes:
        for position, startTime in enumerate(graph[start][route]):
            if startTime < currentTime:
                cost = 1440 - currentTime
                cost += startTime
            else:
                cost = startTime - currentTime
                
            destinations = dict1[route]

            for destination in destinations:
                if destination == start:
                    continue
                
                endTime = graph[destination][route][position]

                if endTime <= startTime:
                    new = cost + 1440 - startTime
                    new += endTime
                else:
                    new = cost + endTime - startTime
                    
                if endTime in vertices:
                    if destination in vertices[endTime]:
                        if currentCost + new < vertices[endTime][destination]:
                            vertices[endTime][destination] = currentCost + new
                            heapq.heappush(heap, (currentCost + new, destination, endTime))

    while 1:
        try:
            newCost, newStart, newTime = heapq.heappop(heap)

            if newTime in vertices:
                if newStart in vertices[newTime]:
                    break
        except IndexError:
            return "stay home"

    del vertices[newTime][newStart]         
    return paths(newStart, end, newCost, newTime, graph, vertices, heap)

thing = {i:{i:1e6 for i in xrange(1,s+1) if i != u} for i in xrange(1440)}
print paths(u, v, 0, t, dict2, thing, [])
