import math, sys
thing = map(int, raw_input().split())
n = thing[0]
k = thing[1]

if n == 1:
    print 0
    sys.exit()
if k == 1:
    print n - 1
    sys.exit()
    
if n <= k:
    count = [2**(i) for i in xrange(1,int(math.ceil(math.log(n*2)/math.log(2))) + 1)]
else:
    count = [2**(i) for i in xrange(1,int(math.ceil(math.log(k*2)/math.log(2))) + 1)]
    
while 1:
    if count[-1] > 2*k:
        count.pop(-1)
    else:
        break

if count[-1] > n:
    cuts = len(count) - 1
else:
    cuts = len(count)
    
n -= count[-1]

if n >= 0:   
    cuts += int(math.ceil(float(n) / k))
print cuts
