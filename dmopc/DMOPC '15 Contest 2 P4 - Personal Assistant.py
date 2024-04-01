import sys, bisect
raw_input = sys.stdin.readline
num = int(raw_input())
lists = sys.stdin.read().strip().split("\n")
lists = [map(int, i.split()) for i in lists]
lists = [(x[0], x[0] + x[1], x[2]) for x in lists]
lists.sort(key = lambda x: x[1])
weights = [0] + [x[2] for x in lists]
ends = [0] + [x[1] for x in lists]
pre = [0]
maximums = [0]
currentMax = 0

for i in xrange(num):
    start = lists[i][0]
    index = bisect.bisect(ends, start, hi = i + 1)
    if index == 0:
        pre.append(0)
    else:
        pre.append(index - 1)

for i in xrange(1,num+1):
    maximums.append(max(weights[i] + maximums[pre[i]], maximums[i-1]))

print maximums[num]
