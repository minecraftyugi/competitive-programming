import collections

n = input()
start, end = map(int, raw_input().split())
people = collections.defaultdict(list)
classes = []
G = []
G2 = []
q = []
q2 = []

for i in range(n):
    p, s = map(int, raw_input().split())
    ids = map(int, raw_input().split())
    classes.append(p)
    G2.append(ids)
    for ID in ids:
        people[ID].append(i)

    if start in ids:
        q.append(i)

    if end in ids:
        q2.append(i)

for i in range(n):
    nodes = set([])
    period = classes[i]
    for pid in G2[i]:
        for clas in people[pid]:
            if classes[clas] > period:
                nodes.add(clas)

    G.append(nodes)

def path(start_q, end_q):
    q = start_q[:]
    q2 = end_q[:]
    min_period = 1000
    for class1 in q:
        for class2 in q2:
            if class1 == class2:
                min_period = min(min_period, classes[class1])

    if min_period != 1000:
        return 1, min_period

    visited = [0]*(n+1)
    for clas in q:
        visited[clas] = 1

    steps = 2
    found = False
    while q:
        new_q = []
        while q:
            node = q.pop()
            for neighbour in G[node]:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    new_q.append(neighbour)
                    if neighbour in q2:
                        found = True
                        min_period = min(min_period, classes[neighbour])

        if found:
            return steps, min_period

        steps += 1
        q = new_q[:]

    return -1

ans = path(q, q2)
if ans == -1:
    print "delivery failure"
else:
    print ans[0]
    print ans[1]
