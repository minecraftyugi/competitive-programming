import sys
raw_input = sys.stdin.readline
line = map(int, raw_input().split())
n = line[0]
m = line[1]
dict1 = {}
lists = []

def parent(graph, visited):
    test = graph[visited[-1]][0]
    if test == visited[-1]:
        for i in visited:
            current = graph[i]
            if current[0] != visited[-1]:
                graph[i] = (visited[-1], current[1])
        return visited[-1]
    else:
        visited.append(test)
        return parent(graph, visited)

for i in xrange(1, n + 1):
    dict1[i] = (i, 0)

for i in xrange(m):
    edge = map(int, raw_input().split())
    a = edge[0]
    b = edge[1]
    parent1 = parent(dict1, [a])
    parent2 = parent(dict1, [b])
    if parent1 != parent2:
        rank1 = dict1[parent1][1]
        rank2 = dict1[parent2][1]
        if rank1 == rank2:
            dict1[parent1] = (parent1, rank1 + 1)
            dict1[parent2] = (parent1, 0)
            pass
        elif rank1 > rank2:
            dict1[parent1] = (parent1, rank1 + 1)
            dict1[parent2] = (parent1, 0)
            pass
        else:
            dict1[parent1] = (parent2, 0)
            dict1[parent2] = (parent2, rank2 + 1)
            pass
        lists.append(i + 1)

for i in dict1:
    parent(dict1, [i])

check = all(dict1[x][0] == dict1[1][0] for x in dict1.keys())

if check:
    for i in lists:
        print i
else:
    print "Disconnected Graph"
