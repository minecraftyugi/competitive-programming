import collections, sys
sys.setrecursionlimit(100000)
num = input()
right = {}
left = {}
distances = {}
points = []
rSwitch = 0
lSwitch = 0
rightCount = 1
leftCount = 1

for i in xrange(num):
    x, h = map(int, raw_input().split())
    right[x] = x
    left[x] = x
    points += [(x, h)]

points.sort(key = lambda x:x[0])

for i in points:
    distances[i[0]] = ([], [])

for i in points:
    i0, i1 = i
    for j in points:
        j0, j1 = j
        if i != j:
            if i0 < j0 and i0 + i1 >= j0:
                distances[i0][1].append(j0)
            if i0 > j0 and i0 - i1 <= j0:
                distances[i0][0].append(j0)

print distances

def parent(start, graph, visited):
    end = graph[start]
    if start == end:
        for i in visited:
            graph[i] = end
        return end

    visited.add(end)
    return parent(end, graph, visited)

for i in left:
    parent1 = parent(i, left, set())
    for j in distances[i][0]:
        parent2 = parent(j, left, set())
        if parent1 != parent2:
            left[j] = parent1

for i in right:
    parent1 = parent(i, right, set())
    for j in distances[i][1]:
        parent2 = parent(j, right, set())
        if parent1 != parent2:
            right[j] = parent1

print left
print right
rightCurrent = right[points[0][0]]
leftCurrent = left[points[0][0]]

for point, height in points:
    r = right[point]
    l = left[point]
    if rSwitch and lSwitch:
        r, l = l, r
    elif rSwitch:
        r = l
    elif lSwitch:
        l = r
    else:
        pass
    if r != rightCurrent:
        rightCurrent = r
        rightCount += 1
    if l != leftCurrent:
        leftCurrent = l
        leftCount += 1
rightCurrent = right[points[0][0]]
leftCurrent = left[points[0][0]]
rightCount = 1
leftCount = 1
for point, height in points:
    r = right[point]
    l = left[point]
    if r != rightCurrent:
        rightCurrent = r
        rightCount += 1
    if l != leftCurrent:
        leftCurrent = l
        leftCount += 1

print min(rightCount, leftCount)
        
