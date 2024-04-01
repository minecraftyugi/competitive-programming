r = input()
l = input()
rows = []
possible = []
for i in xrange(r):
    lights = int("".join(raw_input().split()), 2)
    rows.append(lights)
    possible.append(set([lights]))

table = [[0]*256 for i in xrange(256)]
for i in xrange(256):
    for j in xrange(256):
        table[i][j] = i ^ j

for i in xrange(1, r):
    orig = rows[i]
    for config in possible[i-1]:
        possible[i].add(table[orig][config])

print len(possible[-1])
