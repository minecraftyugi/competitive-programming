m, n = map(int, raw_input().split())
MIN = float("-inf")
while (m, n) != (0, 0):
    grid = []
    for i in range(m):
        grid.append(raw_input().replace(".", "0"))

    dp1 = [[MIN]*n for i in range(m)] #going up
    dp2 = [[MIN]*n for i in range(m)] #going down
    for j in range(n):
        zero = 0
        #traverse up a column
        for i in range(m-1, -1, -1):
            if j == 0:
                if i == m-1:
                    if grid[i][j].isdigit():
                        dp1[i][j] = int(grid[i][j])
                    else:
                        zero = 1
                else:
                    if not zero:
                        if grid[i][j].isdigit():
                            dp1[i][j] = int(grid[i][j]) + dp1[i+1][j]
                        else:
                            zero = 1

            else:
                if i == m-1:
                    if grid[i][j].isdigit():
                        dp1[i][j] = int(grid[i][j]) + dp1[i][j-1]
                else:
                    if grid[i][j].isdigit():
                        dp1[i][j] = int(grid[i][j]) + max(dp1[i][j-1], dp1[i+1][j])

        #traverse down a column
        for i in range(m):
            if j > 0:
                if i == 0:
                    if grid[i][j].isdigit():
                        dp2[i][j] = int(grid[i][j]) + dp1[i][j-1]
                        dp1[i][j] = max(dp1[i][j], dp2[i][j])
                else:
                    if grid[i][j].isdigit():
                        dp2[i][j] = int(grid[i][j]) + max(dp1[i][j-1], dp2[i-1][j])
                        dp1[i][j] = max(dp1[i][j], dp2[i][j])


    print max(dp1[m-1][n-1], 0)
    m, n = map(int, raw_input().split())
