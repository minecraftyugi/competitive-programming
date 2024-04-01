import sys
raw_input = sys.stdin.readline
n = int(raw_input())
logs = []
sums = [0]

for i in xrange(n):
    log = int(raw_input())
    logs.append(log)

for i in xrange(n):
    sums.append(logs[i] + sums[i])
    
q = int(raw_input())

for i in xrange(q):
    thing = map(int, raw_input().split())
    a = thing[0]
    b = thing[1]
    print sums[b+1] - sums[a]
