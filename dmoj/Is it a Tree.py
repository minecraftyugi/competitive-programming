import sys
dict1 = {i:[] for i in xrange(4)}

for i in xrange(4):
    line = map(int, raw_input().split())
    for j in xrange(1+i):
        if line[j] == 1:
            dict1[i].append(j)

ans = {i:i for i in xrange(4)}

def parent(start, visited, graph):
    end = graph[start]
    if start == end:
        for num in visited:
            graph[num] = start
        return start

    visited.append(end)
    return parent(end, visited, graph)

for i in dict1.keys():
    for j in dict1[i]:
        parent1 = parent(i, [i], ans)
        parent2 = parent(j, [j], ans)
        if parent1 != parent2:
            ans[parent1] = parent2
        else:
            print "No"
            sys.exit()

for i in xrange(4):
    parent(i, [i], ans)

if all(ans[0] == ans[i] for i in xrange(4)):
    print "Yes"
