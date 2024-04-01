import heapq
r, c = map(int, raw_input().split())
dict1 = {(i,j):{} for i in xrange(r) for j in xrange(c)}
dict2 = {}
largest = 0
dist = []
ans = []

for i in xrange(r):
    line = raw_input().split()
    for j in xrange(c):
        if line[j].isdigit():
            line[j] = int(line[j])
        if line[j] == ".":
            line[j] = 0
            
        if line[j] == largest and isinstance(line[j], int):
            dist.append((i, j))
            dict2[(i, j)] = line[j]
        elif line[j] > largest and isinstance(line[j], int):
            largest = line[j]
            dist = [(i, j)]
            dict2[(i, j)] = line[j]
        elif line[j] == "X":
            start = (i, j)
            dict2[(i, j)] = 0
        elif line[j] == ".":
            dict2[(i, j)] = 0
        else:
            dict2[(i, j)] = int(line[j])

for i in dict1:
    x, y = i[0], i[1]
    if x - 1 >= 0:
        dict1[(x, y)][(x-1, y)] = dict2[(x-1, y)]
    if x + 1 <= r - 1:
        dict1[(x, y)][(x+1, y)] = dict2[(x+1, y)]
    if y - 1 >= 0:
        dict1[(x, y)][(x, y-1)] = dict2[(x, y-1)]
    if y + 1 <= c - 1:
        dict1[(x, y)][(x, y+1)] = dict2[(x, y+1)]

a = start[0]
b = start[1]
dist.sort(key = lambda x: ((x[0]-a)**2 + (x[1]-b)**2)**0.5)
a1 = dist[0][0]
b1 = dist[0][1]

for i in dist:
    a2 = i[0]
    b2 = i[1]
    if ((a2-a)**2 + (b2-b)**2)**2 == ((a1-a)**2 + (b1-b)**2)**2:
        ans.append(i)
    else:
        break


def paths(first, end, cost, vertices, parents, graph, heap):
    if first in end:
        return first, parents
    
    neighbours = graph[first]
    for i in neighbours:
        try:
            weight = vertices[i]
            new = graph[first][i]
            if new + cost < weight:
                vertices[i] = new + cost
                parents[i] = first
                heapq.heappush(heap, (new + cost, i))
        except KeyError:
            pass

    while 1:
        try:
            thing = heapq.heappop(heap)
            newCost = thing[0]
            newFirst = thing[1]
            test = vertices[newFirst]
            break
        except KeyError:
            pass
        except IndexError:
            return
        
    del vertices[newFirst]
    return paths(newFirst, end, newCost, vertices, parents, graph, heap)

thing1 = {(i,j):1000 for i in xrange(r) for j in xrange(c)}
thing2 = {(i,j):0 for i in xrange(r) for j in xrange(c)}
startNode, dict3 = paths(start, ans, 0, thing1, thing2, dict1, [])
count = 0

while 1:
    parent = dict3[startNode]
    if parent == start:
        break
    if dict2[parent] != 0:
        count += 1

    startNode = parent

print count
