import sys
raw_input = sys.stdin.readline

p, n, v, r = map(int, raw_input().split())
r2 = r**2
points = []
constants = [0]*10
total = 0

for i in xrange(p):
    x, y = map(int, raw_input().split())
    points.append((x, y))

for i in xrange(n):
    constants[i] = input()

def calcY(x):
    y = 0
    for i in xrange(n, 0, -1):
        exponent = x**i
        y += constants[n-i]*exponent

    return y

explode = (v, calcY(v))

for x, y in points:
    if (y - explode[1])**2 + (x - explode[0])**2 <= r2:
        total += 1
    elif x <= v:
        if y == calcY(x):
            total += 1
    else:
        pass

print total
