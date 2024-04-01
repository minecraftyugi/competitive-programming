import sys
raw_input = sys.stdin.readline
n, m, k = map(int, raw_input().split())
ans = [0]*(n+1)
num = m

for i in xrange(m):
    x, y = map(int, raw_input().split())
    ans[x-1] -= 1
    ans[y] += 1

for i in xrange(n+1):
    num += ans[i]
    ans[i] = num

ans = [0]*4
n = 4
k = 0

if sum(ans[:-1]) < k:
    print -1
elif k == 0:
    print 1
else:
    answer = ans[0]
    start = 0
    end = 0
    length = n
    while 1:
        if end == n-1:
            break

        while 1:
            if answer >= k or end == n-1:
                break
            else:
                end += 1
                answer += ans[end]
                
        while 1:
            if answer < k or start == n-1:
                break
            if end - start + 1 < length:
                length = end - start + 1
                
            answer -= ans[start]
            start += 1

    print length
