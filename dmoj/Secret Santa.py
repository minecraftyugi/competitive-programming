import itertools
n = int(raw_input())
options = []
best = []
total = 0

for i in xrange(n):
    floor, weight = map(int, raw_input().split())
    total += weight
    options.append([floor, weight])
    
ways = list(itertools.permutations(options, r=n))

for i in xrange(len(ways)):
    maxWeight = total
    floor = 101
    stress = 0
    for j in xrange(n):
        currentFloor = ways[i][j][0]
        multiplier = abs(floor - currentFloor) + 1
        stress += maxWeight * multiplier
        maxWeight -= ways[i][j][1]
        floor = currentFloor

    best.append(stress)

print min(best)
