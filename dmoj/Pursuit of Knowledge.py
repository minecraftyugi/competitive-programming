import sys
sys.setrecursionlimit(40)
raw_input = sys.stdin.readline
n, m, t = map(int, raw_input().split())
dict1 = {}
ans = [[0 for y in xrange(n+1)] for x in xrange(n+1)]

for i in xrange(m):
    a, b = map(int, raw_input().split())
    try:
        dict1[a].append(b)
    except KeyError:
        dict1[a] = []
        dict1[a].append(b)

q = int(raw_input())

def shortest(start, visit, steps, graph, answer, visited):
    if len(visit) == 0:
        return
    new = set()
    for i in visit:
        try:
            neighbours = graph[i]
        except KeyError:
            continue
        for neighbour in neighbours:
            try:
                test = visited[neighbour]
            except KeyError:
                new.add(neighbour)
                answer[start][neighbour] = steps
                visited[neighbour] = 1

    return shortest(start, new, steps + 1, graph, answer, visited)

for i in dict1:
    shortest(i, [i], 1, dict1, ans, {i:0})

for i in xrange(q):
    a, b = map(int, raw_input().split())
    print ans[a][b] * t if ans[a][b] != 0 else "Not enough hallways!"
