import sys
raw_input = sys.stdin.readline
i = input()
n = input()
j = input()
ans = [0]*(i+1)
count = 0

for x in xrange(j):
    start, end, value = map(int, raw_input().split())
    ans[start-1] += value
    ans[end] -= value

num = 0

for x in xrange(i):
    ans[x] = num + ans[x]
    num = ans[x]

for x in xrange(i):
    if ans[x] < n:
        count += 1

print count
