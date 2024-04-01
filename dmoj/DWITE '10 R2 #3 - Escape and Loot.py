def process(grid, dp, x, y):
    if grid[x][y] == "#":
        return 0
    
    max_val = int(grid[x][y])
    left = 0
    if x-1 >= 0:
        if dp[x-1][y] == -1:
            left = process(grid, dp, x-1, y)
        else:
            left = dp[x-1][y]

    bottom = 0
    if y+1 <= 7:
        if dp[x][y+1] == -1:
            bottom = process(grid, dp, x, y+1)
        else:
            bottom = dp[x][y+1]

    max_val += max(bottom, left)
    dp[x][y] = max_val
    return max_val

for i in xrange(5):
    grid = []
    best = [[-1]*8 for i in xrange(8)]
    for j in xrange(8):
        grid.append(raw_input().replace(".", "0"))

    print process(grid, best, 7, 0)
    _ = raw_input()
