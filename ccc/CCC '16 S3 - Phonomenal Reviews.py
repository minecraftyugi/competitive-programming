import sys, collections

def bfs1(starts):
    """ (list or set of int) -> set of int

    Return nodes that are not part of the new graph, that are reachable from
    nodes in starts and keeping track of visited nodes in visited.

    """

    new = set()
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            graph[neighbour].remove(start)
            #hasnt been visited, not a pho, is a leaf node
            if neighbour not in visited and neighbour not in pho \
               and len(graph[neighbour]) == 1:
                new.add(neighbour)
                visited.add(neighbour)

    if len(new) == 0:
        return visited

    return bfs1(new)

def bfs2(starts):
    """ (list or set of int) -> int

    Return the farthest leaf from the starting nodes in starts, keeping track
    of visited nodes in visited.

    """

    new = set()
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)

    if len(new) == 0:
        return starts.pop()

    return bfs2(new)

def distance(starts, node2, count):
    """ (list or set of int, int, int, set of int) -> int

    Return the distance between nodes in starts and node2.
    Precondition: nodes in starts and node2 are all in the graph, and node2 is
    reachable from the start nodes.

    """

    new = set()
    for start in starts:
        neighbours = graph[start]
        for neighbour in neighbours:
            if neighbour == node2:
                return count + 1

            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)

    return distance(new, node2, count + 1)
            
sys.setrecursionlimit(100000)
raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
pho = set(map(int, raw_input().split()))
graph = collections.defaultdict(set)

for i in range(n-1):
    a, b = map(int, raw_input().split())
    graph[a].add(b)
    graph[b].add(a)

leaves = []
for node in graph:
    if len(graph[node]) == 1 and node not in pho:
        leaves.append(node)

visited = set(leaves)
remove = bfs1(leaves)
for node in remove:
    graph.pop(node)

start_node = pho.pop()
visited = set([start_node])
start = bfs2([start_node])
pho.add(start_node)
visited = set([start])
end = bfs2([start])
visited = set([start])
max_distance = distance([start], end, 0)
print 2*(len(graph)-1) - max_distance
