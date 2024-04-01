n,m = map(int, raw_input().split())
total = 0

for i in xrange(n):
    w = input()
    total += w if w <= m else 0

print total
