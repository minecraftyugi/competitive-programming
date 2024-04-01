l = input()
def solve(order, graph):
    prev = 0
    parents = {0:-1}
    for node in order:
        if node != parents[prev]:
            graph[prev].append(node)
            parents[node] = prev

        prev = node
    
    return 20 * (height(0, graph) - 1)

def height(start, graph):
    h = 1
    for child in graph[start]:
        h = max(h, 1 + height(child, graph))
        
    return h

for i in xrange(l):
    n = input()
    total = 10 * n
    nodes = {}
    g = {0:[]}
    order = []
    num = 1
    for j in xrange(n):
        order.append(raw_input())

    nodes[order[-1]] = 0
    for j in xrange(n):
        node = order[j]
        if node not in nodes:
            nodes[node] = num
            g[num] = []
            num += 1      

        order[j] = nodes[node]

    print total - solve(order, g)
