import sys

raw_input = sys.stdin.readline
n, q = map(int, raw_input().split())
lines = []
d = {}
def intersect(m1, b1, m2, b2):
    return (b2-b1)*1.0 / (m1-m2)

def calc(m, x, b):
    return m*x + b

for i in xrange(n):
    s, m = map(int, raw_input().split())
    d[m] = max(s, d.get(m, 0))

for m, b in sorted(d.items()):
    lines.append((m, b))

stack = []
for m, b in lines:
    if len(stack) < 3:
        stack.append((m, b))
    else:
        pop = True
        while len(stack) > 2 and pop:
            m2, b2 = stack[-1]
            m3, b3 = stack[-2]
            if intersect(m, b, m3, b3) < intersect(m, b, m2, b2):
                stack.pop()
            else:
                pop = False

        stack.append((m, b))

for i in xrange(q):
    x = int(raw_input())
    lower = 0
    upper = len(lines)
    while lower < upper:
        mid = (lower+upper) / 2
        
