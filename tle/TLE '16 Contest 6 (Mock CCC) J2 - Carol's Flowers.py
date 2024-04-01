f, n = map(int, raw_input().split())
flowers = []
for i in xrange(f):
    flowers.append(input())

flowers.sort()
total = 0
power = n
for i in xrange(n):
    total += flowers[i]**power % (10**9 + 7)
    power -= 1

print total % (10**9 + 7)
