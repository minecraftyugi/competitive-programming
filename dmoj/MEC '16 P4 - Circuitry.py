import sys, collections
sys.setrecursionlimit(100000)

n, m = map(int, raw_input().split())
dict1 = collections.defaultdict(list)
dict2 = collections.defaultdict(list)
edges = []
times = {}

for i in xrange(m):
    a, b, w = map(int, raw_input().split())
    thing = [a, b]
    thing.sort()
    edges.append(thing)
    dict1[a].append(b)
    dict1[b].append(a)
    dict2[a].append((b,w))
    dict2[b].append((a,w))

start = min(dict1)
times[start] = [0, 0, 0, 0]

def bridge(vertice, parents, time, graph, visited, answer):
    #visited, low, parent, children
    parents[vertice][0] = time
    parents[vertice][1] = time
    time += 1
    points = graph[vertice]
    visited.add(vertice)

    for point in points:        
        if point not in visited:
            parents[vertice][3] += 1
            parents[point] = [time, time, vertice, 0]
            bridge(point, parents, time, graph, visited, answer)

            parents[vertice][1] = min(parents[vertice][1], parents[point][1])
            
            if parents[point][1] > parents[vertice][0]:
                thing = [point, vertice]
                thing.sort()
                answer.add(tuple(thing))
        else:
            if point != parents[vertice][2]:
                parents[vertice][1] = min(parents[vertice][1], parents[point][0])        
             
    return answer

def path(starts, end, maximum, count, graph, visited):
    new = set()

    for start in starts:
        neighbours = graph[start]
        for thing in neighbours:
            neighbour, weight = thing
            
    return

bridges = bridge(start, times, 0, dict1, set(), set())
print bridges
