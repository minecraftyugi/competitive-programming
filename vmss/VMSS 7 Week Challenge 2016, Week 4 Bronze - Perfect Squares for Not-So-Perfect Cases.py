import math, sys
a, b = map(int, raw_input().split())
count = 0

if a > b:
    a, b = b, a

if b < 0:
    print 0
    sys.exit()
    
root = int(math.ceil(math.sqrt(b)))

for i in xrange(root + 1):
    if i * i <= b and i * i >= a:
        count += 1

print count
