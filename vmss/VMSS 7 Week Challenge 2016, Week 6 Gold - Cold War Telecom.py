import sys, collections

raw_input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, raw_input().split())
dict1 = collections.defaultdict(list)
times = {}
for i in xrange(m):
    x, y = map(int, raw_input().split())
    dict1[x].append(y)
    dict1[y].append(x)

start = min(dict1)
start = 6
times[start] = [0, 0, 0, 0]
def strong(vertice, parents, time, graph, visited, answer):
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
            strong(point, parents, time, graph, visited, answer)
            parents[vertice][1] = min(parents[vertice][1], parents[point][1]) 
            if parents[vertice][2] == 0 and parents[vertice][3] >= 2:
                answer.add(vertice)

            if parents[vertice][2] != 0 and parents[point][1] >= parents[vertice][0]:
                answer.add(vertice)             
        else:
            if point != parents[vertice][2]:
                parents[vertice][1] = min(parents[vertice][1], parents[point][0])        
             
    return answer

thing = strong(start, times, 0, dict1, set(), set())
print len(thing)
print "\n".join(map(str, sorted(thing)))

    
"""
4 4
1 2
1 3
2 3
3 4

8 9
1 2
1 3
2 3
3 4
4 5
5 6
5 7
6 7
6 8
"""
