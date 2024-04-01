n = input()
pyramid = []
dp = []
for i in xrange(1, n+1):
    pyramid.append(map(int, raw_input().split()))
    dp.append([-1]*i)

def max_sum(row, col):
    if row == 0:
        dp[0][0] = pyramid[0][0]
    elif dp[row][col] == -1:
        base = pyramid[row][col]
        if col == 0:
           dp[row][col] = base + max_sum(row-1, 0)
        elif row == col:
            dp[row][col] = base + max_sum(row-1, col - 1)
        else:
            dp[row][col] = base + max(max_sum(row-1, col-1), max_sum(row-1, col))

    return dp[row][col]

ans = 0
for i in xrange(n):
    ans = max(ans, max_sum(n-1, i))

print ans
