import sys

raw_input = sys.stdin.readline
n = input()
k = input()
j = input()
targets = [[0]*(n+1) for i in xrange(3)]
for i in xrange(j):
    start, end, amount, index = map(int, raw_input().split())
    targets[index-1][start-1] += amount
    targets[index-1][end] -= amount

for i in xrange(3):
    counter = targets[i][0]
    for j in xrange(1, n+1):
        num = targets[i][j]
        targets[i][j] += counter
        counter += num

    ans = 0
    for j in xrange(n):
        if targets[i][j] < k:
            ans += 1

    print ans
