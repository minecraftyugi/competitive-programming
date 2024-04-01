"""
import sys, collections
raw_input = sys.stdin.readline
n, m, k = map(int, raw_input().split())
dict1 = collections.defaultdict(set)
ans = {i:[set([i])for j in xrange(k)]for i in xrange(1, n+1)}

for i in xrange(m):
    x, y = map(int, raw_input().split())
    dict1[x].add(y)
    dict1[y].add(x)

for point in dict1:
    ans[point][0].update(dict1[point])

for i in xrange(1, k):
    for point in dict1:
        for neighbour in dict1[point]:
            ans[point][i].update(ans[neighbour][i-1])
            
for i in xrange(1, n+1):
    print len(ans[i][-1])
"""

import sys, pprint
raw_input = sys.stdin.readline
n, m, k = map(int, raw_input().split())
dict1 = [[0 for i in xrange(n+1)]for i in xrange(n+1)]
dict2 = [[0 for i in xrange(n+1)]for i in xrange(n+1)]
ans = [0]*(n+1)

for i in xrange(n+1):
    dict1[i][i] = 1
    dict2[i][i] = 1
    
for i in xrange(m):
    x, y = map(int, raw_input().split())
    dict1[x][y] += 1
    dict1[y][x] += 1
    dict2[x][y] += 1
    dict2[y][x] += 1

for i in xrange(n+1):
    ans[i] = sum(dict1[i])

pprint.pprint(dict1)
print ans
