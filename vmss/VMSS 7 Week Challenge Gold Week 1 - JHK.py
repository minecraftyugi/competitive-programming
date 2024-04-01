n, k = map(int, raw_input().split())
prime = [1]*(n+1)
for i in xrange(3, n+1, 2):
    if prime[i]:
        for j in xrange(i*i, n+1, 2*i):
            prime[j] = 0

if n < 2:
    ans = 0
elif k == 1:
    ans = 1
    for i in xrange(3, n+1, 2):
        if prime[i]:
            ans += 1
elif k == 2:
    ans = n / 2 - 1
    for i in xrange(3, n+1, 2):
        if not prime[i]:
            if prime[i-2]:
                ans += 1
elif k == 3:
    ans = 0
    for i in xrange(3, n+1, 2):
        if not prime[i]:
            if not prime[i-2]:
                ans += 1
else:
    ans = 0

print ans
