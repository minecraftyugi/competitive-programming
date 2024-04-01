n = int(input())
lights = ""
for i in range(n):
    lights += input()

dp = [100]*(n+1)
dp[0] = 0
for i in range(3):
    if lights[i] == "0":
        dp[i+1] = dp[i]

for i in range(3, n):
    if lights[i] == "0":
        dp[i+1] = max(dp[i], 1 + lights[i-3:i].count("0") + dp[i-3])
    else:
        dp[i+1] = lights[i-3:i].count("0") + dp[i-3]

print(dp[n])
