n, m = map(int, raw_input().split())
word1 = raw_input()
word2 = raw_input()
dp = [[0]*(m+1) for i in xrange(n+1)]

for i in xrange(n + 1):
    for j in xrange(m + 1):
        if i == 0:
            if j == 0:
                dp[i][j] = 0
            elif j <= 2:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-3] + 1
        elif j == 0:
            if i == 0:
                dp[i][j] = 0
            elif i <= 2:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-3][j] + 1
        elif word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            moves = []
            moves.append(dp[i-1][j])
            moves.append(dp[i][j-1])
            moves.append(dp[i-1][j-1])
            if i >= 2:
                moves.append(dp[i-2][j])
            if i >= 3:
                moves.append(dp[i-3][j])
            if j >= 2:
                moves.append(dp[i][j-2])
            if j >= 3:
                moves.append(dp[i][j-3])

            dp[i][j] = min(moves) + 1

print dp[n][m]
