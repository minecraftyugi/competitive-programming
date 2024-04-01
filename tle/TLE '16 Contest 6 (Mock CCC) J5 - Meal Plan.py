n = input()
b, l, d = map(int, raw_input().split())
b_list = map(int, raw_input().split())
l_list = map(int, raw_input().split())
d_list = map(int, raw_input().split())
meals = [b_list, l_list, d_list]
dp = [[0]*(n+1) for i in range(3)]
MOD = 10**9 + 7

for meal in b_list:
    if meal <= n:
        dp[0][meal] += 1

for i in range(n+1):
    for j in range(3):
        if dp[j][i]:
            for meal in meals[(j+1) % 3]:
                if meal + i <= n:
                    dp[(j+1) % 3][meal + i] += dp[j][i]

index = n + 1
found = False
while not found and index >= 0:
    index -= 1
    if dp[0][index] or dp[1][index] or dp[2][index]:
        found = True

if not found:
    print 0, n
else:
    print (dp[0][index] + dp[1][index] + dp[2][index]) % MOD, n - index
