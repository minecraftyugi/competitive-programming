line = map(int, raw_input().split())
n = line[0]
x = line[1]
primes = [False, False] + [i for i in xrange(2, n + 1)]
count = 0

for i in xrange(2, n + 1):
    if primes[i] is not False:
        for j in xrange(i*2,n+1,i):
            primes[j] = False

for i in primes:
    if i is not False:
        remainder = n - i
        count += 2 * (remainder / x) + 1
        if remainder % x != 0:
            count += 1
    else:
        pass

print count
