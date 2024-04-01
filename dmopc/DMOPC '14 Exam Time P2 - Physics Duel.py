import math

n = input()
h = 0
rate = math.pi / 180
for i in xrange(n):
    s, x, t = map(float, raw_input().split())
    h += t * s * math.sin(rate * x)

print int(round((2 * 9.8 * h)**.5))
