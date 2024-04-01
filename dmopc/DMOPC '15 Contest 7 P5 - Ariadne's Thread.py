import sys
raw_input = sys.stdin.readline

n = input()
dict1 = {}
time = 0

for i in xrange(n):
    points = map(int, raw_input().split())[1:]
    dict1[i+1] = points

def dfs(vertice, graph, visited, times):
    global time
    print vertice, time
    times[vertice] = time
    time += 1
    points = graph[vertice]
    visited.add(vertice)
    
    for point in points:
        if point not in visited:
            dfs(point, graph, visited, times)
        else:
            print point

    time += 1
    return times

def bfs(starts, end, time, graph, visited):
    new = set()

    for start in starts:
        if start == end:
            return time
        
        neighbours = graph[start]
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                new.add(neighbour)

    return bfs(new, end, time + 1, graph, visited)

ans = dfs(1, dict1, set(), {})
lastVisit = max(ans.items(), key = lambda x: x[1])[0]
lastTime = ans[lastVisit]
back = bfs([1], lastVisit, 1, dict1, set([1])) + lastTime - 1
print lastVisit, back, "hi"

q = input()

for i in xrange(q):
    a, b = map(int, raw_input().split())
    if ans[b] - ans[a] >= 0:
        print ans[b] - ans[a]
    else:
        print ans[b] - ans[a] + back

print dict1
