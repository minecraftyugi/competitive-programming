import sys

lists = sys.stdin.read().strip().split("\n")
dict1 = {}
start = map(int, lists[0].split())
size = start[0]
num = start[1]
people = map(int, lists[-1].split())
p1 = people[0]
p2 = people[1]

for i in xrange(1, size + 1):
    dict1[i] = []

for i in xrange(1, num + 1):
    thing = map(int, lists[i].split())
    tall = thing[0]
    small = thing[1]
    dict1[tall].append(small)

def height(startList, endList, start, end, graph):
    newStart = []
    newEnd = []
    if end in startList:
        return "yes"
    if start in endList:
        return "no"
    for i in startList:
        try:
            numbers = graph[i]
            for j in numbers:
                newStart.append(j)
            del graph[i]
        except KeyError:
            pass

    for i in endList:
        try:
            numbers = graph[i]
            for j in numbers:
                newEnd.append(j)
            del graph[i]
        except KeyError:
            pass

    newStart = sorted(set(newStart))
    newEnd = sorted(set(newEnd))
    if newStart == startList and newEnd == endList:
        return "unknown"
    
    return height(newStart, newEnd, start, end, graph)

print height(dict1[p1], dict1[p2], p1, p2, dict1)
