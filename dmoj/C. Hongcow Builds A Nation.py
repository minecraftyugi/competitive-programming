import sys, collections

raw_input = sys.stdin.readline
n, m, k = map(int, raw_input().split())
govs = set(map(int, raw_input().split()))
graph = collections.defaultdict(set)
nodes = set(i for i in range(1, n+1))
gov_components = []
other_components = []
total_component_size = 0
ans = 0

for i in xrange(m):
    u, v = map(int, raw_input().split())
    graph[u].add(v)
    graph[v].add(u)


def bfs(starts, edges, gov, graph, visited):
    new = set()
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            i0 = min(start, neighbour)
            i1 = max(start, neighbour)
            edge = (i0, i1)
            edges.add(edge)
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)
                if neighbour in govs:
                    gov = True

    if len(new) == 0:
        return visited, edges, gov
    else:
        return bfs(new, edges, gov, graph, visited)

while nodes:
    start = nodes.pop()
    nodes.add(start)
    gov = start in govs
    connected, edges, gov = bfs([start], set(), gov, graph, set([start]))
    if gov:
        gov_components.append((connected, len(edges)))
    else:
        other_components.append((connected, len(edges)))

    for node in connected:
        nodes.remove(node)
   
for connected, edge_count in gov_components:
    maximum = len(connected) * (len(connected) - 1) / 2
    ans += maximum - edge_count

for connected, edge_count in other_components:
    maximum = len(connected) * (len(connected) - 1) / 2
    ans += maximum - edge_count
    total_component_size += len(connected)

for i in range(len(other_components)):
    for j in range(i+1, len(other_components)):
        num_nodes1 = len(other_components[i][0])
        num_nodes2 = len(other_components[j][0])
        ans += num_nodes1 * num_nodes2

maximum = 0
for connected, edge_count in gov_components:
    maximum = max(maximum, len(connected))

ans += maximum * total_component_size
print ans
