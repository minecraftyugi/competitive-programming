import collections, sys

n = input()
total = set()
dict1 = collections.defaultdict(int)
raw_input = sys.stdin.readline
maximum = (n**2 - n) / 2

for i in xrange(n):
    m, b = map(int, raw_input().split())
    total.add((m, b))
    dict1[m] += 1

if len(total) < n:
    print "Infinity"
    sys.exit()

for i in dict1:
    count = dict1[i]
    if count > 1:
        maximum -= (count**2 - count) / 2

print maximum
    
