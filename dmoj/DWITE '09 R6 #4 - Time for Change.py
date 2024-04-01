for i in xrange(5):
    m = input()
    dp = [101]*(m+1)
    c = input()
    for j in xrange(c):
        amount = input()
        dp[amount] = 1
        for index in range(m+1):
            if dp[index] != 101 and amount + index <= m:
                dp[amount+index] = min(dp[amount+index], 1 + dp[index])

    print dp[m]
