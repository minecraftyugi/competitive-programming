import sys, collections

raw_input = sys.stdin.readline
n = input()
g = [[]for i in xrange(n)]
g2 = [0 for i in xrange(n)]
for i in xrange(n-1):
    a, b, x, t = map(int, raw_input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g2[b] = (a, x*0.01, t)

ans = map(int, raw_input().split())
tree_q = collections.deque([0])
q = []
while tree_q:
    node = tree_q.popleft()
    q.append(node)
    for child in g[node]:
        tree_q.append(child)

index = n - 1
while index > 0:
    node = q[index]
    val = ans[node]
    parent, flow, special = g2[node]
    if special:
        val = val**0.5

    ans[parent] = max(ans[parent], val / flow)
    index -= 1
    
print ans[0]
