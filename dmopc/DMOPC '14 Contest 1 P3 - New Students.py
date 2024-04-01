import sys
raw_input = sys.stdin.readline

i = int(raw_input())
ans = 0

for x in xrange(i):
    num = int(raw_input())
    ans += num

s = int(raw_input())

for x in xrange(s):
    num = int(raw_input())
    ans += num
    print ans/(i+x+1.0)
