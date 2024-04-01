import sys
raw_input = sys.stdin.readline
gates = int(raw_input())
planes = int(raw_input())
count = 0
dict1 = {i:i for i in xrange(gates+1)}

def compress(start, visited, graph):
    end = graph[start]
    if start == end:
        for i in visited:
            if graph[i] != end:
                graph[i] = end
        return start
    visited.append(end)
    return compress(end, visited, graph)

for i in xrange(planes):
    port = int(raw_input())
    parent1 = compress(port, [port], dict1)
    if parent1 == 0:
        break
    parent2 = compress(parent1 - 1, [parent1 - 1], dict1)
    dict1[parent1] = parent2
    count += 1

print count
