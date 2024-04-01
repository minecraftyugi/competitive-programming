n, r, s = map(int, raw_input().split())
grid = [[0]*(r+1) for i in xrange(s+1)]
grid2 = [[0]*(r+1) for i in xrange(s+1)]
grid[0][0] = 1
apples = []
for i in xrange(n):
    apple, val, cost, vol = raw_input().split()
    val, cost, vol = int(val), int(cost), int(vol)
    apples.append((apple, val, cost, vol))
    for j in xrange(vol, s+1):
        for k in xrange(cost, r+1):
            prev = grid[j-vol][k-cost]
            if prev and val + prev > grid[j][k]:
                grid[j][k] = val + prev
                grid2[j][k] = i

count = [0]*n
maximum = 0
for i in xrange(s+1):
    for j in xrange(r+1):
        if grid[i][j] > maximum:
            maximum = grid[i][j]
            pos = (i, j)

print grid[pos[0]][pos[1]] - 1
while pos != (0, 0):
    apple = grid2[pos[0]][pos[1]]
    count[apple] += 1
    pos = (pos[0] - apples[apple][3], pos[1] - apples[apple][2])

for i in xrange(n):
    print apples[i][0], count[i]
