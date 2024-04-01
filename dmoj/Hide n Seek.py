import collections, itertools
n, m, t = map(int, raw_input().split())
dict1 = {}
dict2 = collections.defaultdict(dict)
nodes = []
hiders = []
lowest = []

for i in xrange(n):
    line = raw_input()
    nodes.append(line)
    for j in xrange(m):
        if nodes[i][j] == ".":
            dict1[(i, j)] = []
        elif nodes[i][j] == "G":
            first = (i, j)
            dict1[(i, j)] = []
        elif nodes[i][j] == "H":
            hiders.append((i, j))
            dict1[(i, j)] = []
        else:
            pass

options = itertools.permutations(hiders, t)

for i in dict1:
    try:
        dict1[(i[0]-1,i[1])]
        dict1[i].append((i[0]-1,i[1]))
    except KeyError:
        pass
    try:
        dict1[(i[0],i[1]-1)]
        dict1[i].append((i[0],i[1]-1))
    except KeyError:
        pass
    try:
        dict1[(i[0]+1,i[1])]
        dict1[i].append((i[0]+1,i[1]))
    except KeyError:
        pass
    try:
        dict1[(i[0],i[1]+1)]
        dict1[i].append((i[0],i[1]+1))
    except KeyError:
        pass

def weight(start, end, steps, graph, visited):
    new = set()
    for i in start:
        neighbours = graph[i]
        for neighbour in neighbours:
            try:
                test = visited[neighbour]
            except KeyError:
                if neighbour == end:
                    return steps
                else:
                    new.add(neighbour)
                    visited[neighbour] = 0
                    
    return weight(new, end, steps + 1, graph, visited)

for i in hiders+[first]:
    for j in hiders+[first]:
        if i != j:
            ans = weight([i], j, 1, dict1, {i:0})
            dict2[i][j] = ans

for i in options:
    time = dict2[first][i[0]]
    for j in xrange(t-1):
        time += dict2[i[j]][i[j+1]]

    lowest.append(time)

print min(lowest)
