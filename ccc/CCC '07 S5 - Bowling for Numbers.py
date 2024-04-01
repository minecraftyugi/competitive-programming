import sys

input = sys.stdin.readline
t = int(input())
#_ = raw_input()

for i in xrange(t):
    n, k, w = map(int, raw_input().strip().split())
    #_ = raw_input()
    pins = []
    points = []
    prefix = [0]
    for j in xrange(n):
        pins.append(int(input()))
        #_ = raw_input()
        prefix.append(pins[-1] + prefix[-1])

    for j in xrange(1, n+1):
        if j - w < 0:
            points.append(prefix[j])
        else:
            points.append(prefix[j] - prefix[j-w])
    
    dp = [0]*n
        
    for x in xrange(k):
        dp2 = []
        for y in xrange(n):
            if y < w:
                dp2.append(points[y])
            else:
                maximum = max(dp2[-1], dp[y-w] + points[y])
                dp2.append(maximum)

        dp = dp2[:]

    print dp[-1]
