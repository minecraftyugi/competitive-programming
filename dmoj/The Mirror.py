import bisect
n = int(raw_input())
numbers = [False, False] + [i for i in xrange(2,1000001)]
primes = []

for i in xrange(2, 1000001):
    if numbers[i] is not False:
        primes.append(numbers[i])
        for j in xrange(i*2, 1000001, i):
            numbers[j] = False

for i in xrange(n):
    a, b = map(int, raw_input().split())
    start = bisect.bisect_left(primes, a)
    end = bisect.bisect_left(primes, b)
    print end - start if a != b else 0
