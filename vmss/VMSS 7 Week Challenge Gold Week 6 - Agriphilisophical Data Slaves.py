import sys

raw_input = sys.stdin.readline
n = input()
g = [[]for i in range(400000)]
def build(node):
    total = vals[node-1]
    for child in g[node]:
        total += build(child)

    totals[node-1] = total
    return total

for i in xrange(n-1):
    a, b = map(int, raw_input().split())
    g[a].append(b)

vals = map(int, raw_input().split())
totals = [0]*n
build(1)
print max(totals)
