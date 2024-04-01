c, m = map(int, raw_input().split())
dp = [0]*(m+1)
for i in xrange(c):
    princesses, time = map(int, raw_input().split())
    for j in xrange(m, -1, -1):
        if dp[j] and j + time <= m and princesses + dp[j] > dp[j+time]:
            dp[j+time] = princesses + dp[j]

    if time <= m:
        dp[time] = max(dp[time], princesses)
   
print max(dp)
