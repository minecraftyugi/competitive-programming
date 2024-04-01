import sys
n,m = map(int, raw_input().split())
dict1 = {i:[] for i in xrange(1,n+1)}
nums = [i for i in xrange(n+1)]

for i in xrange(m):
    x,y = map(int, raw_input().split())
    dict1[x].append(y)
    #dict1[y].append(x)

def paths(start, start2, visited, steps, graph):
    print start, start2, steps
    if steps > 6:
        return "NO"
    new = set()
    for num in start2:
        for neighbour in graph[num]:
            if neighbour not in visited:
                new.add(neighbour)
                visited.add(neighbour)
                print steps
                if neighbour == start and steps == 6:
                    return "YES"
                
    return paths(start, new, visited, steps + 1, graph)

for i in xrange(1,2):
    ans = paths(i, [i], set(), 1, dict1)
    if ans == "YES":
        print "YES"
        sys.exit()

print "NO"
