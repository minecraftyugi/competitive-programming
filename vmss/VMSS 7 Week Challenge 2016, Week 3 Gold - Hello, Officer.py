import sys, heapq
raw_input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, b, q = map(int, raw_input().split())
dict1 = {}

for i in xrange(m):
    x, y, z = map(int, raw_input().split())
    if x in dict1:
        dict1[x].append((y, z))
    else:
        dict1[x] = [(y, z)]
    if y in dict1:
        dict1[y].append((x, z))
    else:
        dict1[y] = [(x, z)]


def shortest(start, cost, graph, visited, heap, costs):
    if start in graph:
        for neighbours in graph[start]:
            neighbour, newCost = neighbours
            if neighbour in visited:
                if newCost + cost < visited[neighbour]:
                    visited[neighbour] = newCost + cost
                    costs[neighbour] = newCost + cost
                    heapq.heappush(heap, (newCost + cost, neighbour))

    while 1:
        try:
            newCost, newStart = heapq.heappop(heap)
            test = visited[newStart]
            break
        except IndexError:
            return costs
        except KeyError:
            pass

    del visited[newStart]
    costs[newStart] = newCost
    
    return shortest(newStart, newCost, graph, visited, heap, costs)

costs = shortest(b, 0, dict1, {i:1e10 if i!=b else 0 for i in xrange(1, 2001)}, [], {b:0})

for i in xrange(q):
    a = int(raw_input())
    if a in costs:
        print costs[a]
    else:
        print -1
