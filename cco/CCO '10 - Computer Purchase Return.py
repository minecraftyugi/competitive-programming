import sys

raw_input = sys.stdin.readline
t = input()
n = input()
types = [[]for i in xrange(t+1)]
for i in xrange(n):
    c, v, comp = map(int, raw_input().split())
    types[comp].append((c, v))

b = input()
ans = [[0]*(b+1)for i in xrange(t+1)]
indexes = [0]
for i in xrange(1, t+1):
    new = set()
    for index in indexes:
        for cost, value in types[i]:
            idx = cost + index            
            if idx <= b:
                ans[i][idx] = max(ans[i][idx], ans[i-1][idx-cost] + value)
                new.add(idx)

    indexes = list(new)

val = max(ans[t])
if val > 0:
    print val
else:
    print 0
