import sys, math
raw_input = sys.stdin.readline

n, m, h = map(int, raw_input().split())
times = [0]*n
breaks = 0

for i in range(n):
    times[i] = int(raw_input())

for i in range(n-2, -1, -1):
    if times[i+1] - times[i] > h:
        amount = int(math.ceil((times[i+1] - times[i] - h) / (m*1.0)))
        breaks += amount
        times[i] += amount * m

print breaks
