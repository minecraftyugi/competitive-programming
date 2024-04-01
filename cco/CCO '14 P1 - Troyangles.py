n = input()
dp = [0]*n
ans = 0
for i in xrange(n):
    grid = raw_input()
    counter = 0
    dp2 = [0]*n
    for j in xrange(n):
        if grid[j] == "#":
            counter += 1
            if counter < 3:
                dp2[j] = 1
                ans += 1
            else:
                base = (counter + 1) / 2
                dp2[j] = min(dp[j-1] + 1, base)
                ans += dp2[j]
        else:
            counter = 0
    
    dp = dp2[:]

print ans
