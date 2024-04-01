from collections import deque

n, k, t, c = map(int, input().split())
MOD = 10**9 + 7

adults = c
babies = deque()
for i in range(1, n+1):
    if i > t + 1:
        adults += babies.popleft()
        adults %= MOD

    if i == n:
        break
    
    babies.append((adults * k) % MOD)

ans = (((adults * 2) % MOD) + (sum(babies) % MOD)) % MOD
print(ans)
