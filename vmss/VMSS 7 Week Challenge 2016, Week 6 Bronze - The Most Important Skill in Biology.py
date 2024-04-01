import math
n = input()
points = []
ans = 0

for i in xrange(n):
    x, y = map(int, raw_input().split())
    points += [(x, y)]

for i in xrange(n):
    a1 = points[i][0]
    b1 = points[i][1]
    if i == n-1:
        a2 = points[0][0]
        b2 = points[0][1]
    else:
        a2 = points[i+1][0]
        b2 = points[i+1][1]

    ans += a1 * b2
    ans -= b1 * a2

print int(math.ceil(0.5*abs(ans)))
