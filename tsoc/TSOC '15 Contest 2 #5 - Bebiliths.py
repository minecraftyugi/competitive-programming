import sys
raw_input = sys.stdin.readline
s = int(raw_input())
n = int(raw_input())
fast = []
slow = []

for i in xrange(1, n+1):
    b, d, c = map(int, raw_input().split())
    if b >= s:
        fast.append((i, b, c))
    else:
        slow.append((i, b, d))

fast.sort(key = lambda x:(x[1], x[2]), reverse = True)
slow.sort(key = lambda x:(x[1], x[2]), reverse = True)
final = [0]+fast+slow

q = int(raw_input())

for i in xrange(q):
    num = int(raw_input())
    print final[num][0]
