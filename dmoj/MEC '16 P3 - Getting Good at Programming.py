n, t = map(int, raw_input().split())
dp = [0]*(t+1)
for i in xrange(n):
    numbers = map(int, raw_input().split())
    level = numbers[0]
    dp2 = [[0]*(t+1) for i in range(level)]
    time = numbers[1]
    exp = numbers[2]
    if time <= t:
        dp2[0][time] = exp
    for j in xrange(1, t+1-time):
        if dp[j]:
            dp2[0][j+time] = dp[j] + exp
            
    for j in xrange(1, level):
        time = numbers[j*2+1]
        exp = numbers[j*2+2]
        for k in xrange(t+1-time):
            if dp2[j-1][k]:
                dp2[j][k+time] = dp2[j-1][k] + exp

    for j in xrange(level):
        for k in xrange(t+1):
            dp[k] = max(dp[k], dp2[j][k])
    
print max(dp)
