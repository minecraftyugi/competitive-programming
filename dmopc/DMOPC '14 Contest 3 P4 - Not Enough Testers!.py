import sys, collections, bisect
raw_input = sys.stdin.readline

t = input()
primes = [0] + [1]*100000
dict1 = collections.defaultdict(list)

for i in xrange(2, 100001):
    for j in xrange(i, 100001, i):
        primes[j] += 1

for i in xrange(1, 100001):
    dict1[primes[i]].append(i)

for i in xrange(t):
    k, a, b = map(int, raw_input().split())
    low = bisect.bisect_left(dict1[k], a)
    high = bisect.bisect_right(dict1[k], b)
    print high - low
