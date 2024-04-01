import collections, sys
sys.setrecursionlimit(100)
r, c = map(int, raw_input().split())
dots = set()
dict1 = {}
dict2 = collections.defaultdict(list)
cage = 0

for i in xrange(r):
    line = list(raw_input())
    for j, char in enumerate(line):
        if char == "." or char == "M":
            dots.add((i, j))

        dict1[(i, j)] = char

for i in xrange(r):
    for j in xrange(c):
        if (i+1,j) in dict1:
            dict2[(i, j)].append((i+1,j))
        if (i-1,j) in dict1:
            dict2[(i, j)].append((i-1,j))
        if (i,j+1) in dict1:
            dict2[(i, j)].append((i,j+1))
        if (i,j-1) in dict1:
            dict2[(i, j)].append((i,j-1))
            
def explore(starts, count, graph, neighbours, visited, delete):
    #print starts, visited
    new = set()
    if len(starts) == 0:
        if count > 0:
            return 1, delete
        else:
            return 0, delete

    for point in starts:
        if graph[point] == "M":
            count += 1
        goto = neighbours[point]
        for neighbour in goto:
            if neighbour not in visited:
                if graph[neighbour] == "M":
                    count += 1
                    visited.add(neighbour)
                    new.add(neighbour)
                    delete.add(neighbour)
                elif graph[neighbour] == ".":
                    visited.add(neighbour)
                    new.add(neighbour)
                    delete.add(neighbour)
                else:
                    visited.add(neighbour)

    return explore(new, count, graph, neighbours, visited, delete)

while len(dots) > 0:
    point = dots.pop()
    num, remove = explore([point], 0, dict1, dict2, set([point]), set([point]))
    for point in remove:
        dots.discard(point)

    cage += num

print cage
