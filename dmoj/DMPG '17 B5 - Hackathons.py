import sys, bisect

raw_input = sys.stdin.readline
n = input()
best = [0]*(10**6+1)
for i in xrange(n):
    t, w = map(int, raw_input().split())
    best[t] = max(best[t], w)
        
ans = [0]
max_wow = 0
for time in xrange(10**6 + 1):
    if best[time] > max_wow:
        ans.append(time)
        max_wow = best[time]

q = input()
for i in xrange(q):
    max_t = int(raw_input())
    index = bisect.bisect_right(ans, max_t)
    print best[ans[index-1]]
