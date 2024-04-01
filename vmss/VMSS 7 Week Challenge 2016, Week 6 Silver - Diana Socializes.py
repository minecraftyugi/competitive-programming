import collections
n, m = map(int, raw_input().split())
dict1 = {}
dict2 = collections.defaultdict(set)
dict3 = {}
walls = []
space = []
spaceSet = set()
old = set()
count = 0

for i in xrange(n):
    line = list(raw_input())
    for j, value in enumerate(line):
        if value == "X":
            walls += [(i, j)]
        else:
            space += [(i, j)]
            spaceSet.add((i, j))

def paths(start, graph, visited, order):
    new = set()
    for point in start:
        x, y = point
        if (x-1, y) not in visited and (x-1, y) in graph:
            new.add((x-1, y))
            visited.add((x-1, y))
        if (x+1, y) not in visited and (x+1, y) in graph:
            new.add((x+1, y))
            visited.add((x+1, y))
        if (x, y-1) not in visited and (x, y-1) in graph:
            new.add((x, y-1))
            visited.add((x, y-1))
        if (x, y+1) not in visited and (x, y+1) in graph:
            new.add((x, y+1))
            visited.add((x, y+1))

    if len(new) == 0:
        return (order+1, visited)
    else:
        return paths(new, graph, visited, order)

for i in space:
    if i not in old:
        count, places = paths([i], spaceSet, set([i]), count)
        old = old.union(places)
        for place in places:
            dict1[place] = count

for i in walls:
    x, y = i
    if (x-1, y) in spaceSet:
        dict2[i].add(dict1[(x-1, y)])
    if (x+1, y) in spaceSet:
        dict2[i].add(dict1[(x+1, y)])
    if (x, y-1) in spaceSet:
        dict2[i].add(dict1[(x, y-1)])
    if (x, y+1) in spaceSet:
        dict2[i].add(dict1[(x, y+1)])

for i in dict2:
    dict3[i] = len(dict2[i])
                    
thing = dict3.items()
thing.sort(key = lambda x:(x[0][0], x[0][1]))
thing.sort(key = lambda x:x[1], reverse=True)
point, length = thing[0]
group = sorted(map(str, dict2[point]))

if length == 1:
    print -1
else:
    print length
    print point[1], point[0]
    print " ".join(group)
