import sys
from collections import defaultdict

lines = sys.stdin.read().strip().split('\n')
n = int(lines[0])
graph = defaultdict(list)

for i in xrange(1, len(lines) - 1):
    numbers = map(int, lines[i].split())
    a, b = numbers[0], numbers[1]
    graph[a].append(b)

paths = [0] * (n+1)
paths[1] = 1

#Counts the number of paths from 1 to i
#For each node, it sums the amount of times it was accesed by parent nodes

for i in xrange(1, n+1):
    for j in graph[i]:
        paths[j] += paths[i]
        
print paths[n]
