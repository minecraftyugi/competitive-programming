import sys
input = sys.stdin.readline

n, d = map(int, input().split())
trolleys = list(map(int, input().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + trolleys[i])

start = 0
end = n
for i in range(d):
    idx = int(input())
    F = prefix[start+idx] - prefix[start]
    S = prefix[end] - prefix[start+idx]
    if F < S:
        end = start + idx
        print(S)
    else:
        start += idx
        print(F)
