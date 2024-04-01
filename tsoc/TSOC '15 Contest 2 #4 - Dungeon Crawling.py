import sys, collections

raw_input = sys.stdin.readline
n, m = map(int, raw_input().split())
g1 = collections.defaultdict(list)
g2 = collections.defaultdict(list)
sources = []
sinks = []
dist = {}

for i in xrange(m):
    a, b = map(int, raw_input().split())
    g1[a].append(b)
    g2[b].append(a)

for i in xrange(n):
    if g1[i] and not g2[i]:
        sources.append(i)

    if g2[i] and not g1[i]:
        sinks.append(i)
        dist[i] = 10**6

def paths(start):
    total = 0
    for child in g1[start]:
        if child in sinks:
            total += 1
        else:
            total += paths(child)

    return total

def shortest(starts, visited, count):
    new = set()
    for start in starts:
        for child in g1[start]:
            if child not in visited:
                if child in dist:
                    dist[child] = min(dist[child], count + 1)
                    
                new.add(child)
                visited.add(child)

    if not new:
        return

    return shortest(new, visited, count + 1)

ans = 0
for source in sources:
    ans += paths(source)
    shortest([source], set([source]), 1)

print ans
distances = [str(pair[1]) for pair in sorted(dist.items())]
print " ".join(distances)
