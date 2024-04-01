import sys
sys.setrecursionlimit(200000)

n = input()
nodes = [0] + map(int, raw_input().split())
order = map(int, raw_input().split())
G = [[] for i in range(n+1)]
    
for i in range(1, n+1):
    if nodes[i] == 0:
        root = i
    else:
        G[nodes[i]].append(i)

#pre and post ordering
clock = 0
pre = [0]*(n+1)
post = [0]*(n+1)
visited = [0]*(n+1)

def explore(node):
    global clock
    
    clock += 1
    pre[node] = clock
    for neighbour in G[node]:
        if not visited[neighbour]:
            explore(neighbour)

    visited[node] = 1
    clock += 1
    post[node] = clock

explore(root)

#BIT processing
tree = [0]*(2*n+1)

def add(val, node):
    while node <= 2*n:
        tree[node] += val
        tree[node] %= 10**9 + 7
        node += node & -node

def query(node):
    ans = 0
    while node:
        ans += tree[node]
        ans %= 10**9 + 7
        node -= node & -node

    return ans

ans = [0]*(n+1)
for node in order:
    val = query(post[node]) - query(pre[node] - 1) + 1
    val %= 10**9 + 7
    ans[node] = val
    add(val, pre[node])

print " ".join(map(str, ans[1:]))
