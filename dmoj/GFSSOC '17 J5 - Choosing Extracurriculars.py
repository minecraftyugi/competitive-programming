import sys

input = sys.stdin.readline

n = int(input())
prev = [0]*4
for _ in range(n):
    scores = list(map(int, input().split()))
    curr = [0]*4
    for i in range(4):
        if i == 0:
            curr[i] = max(prev[i], scores[i])
        else:
            curr[i] = max(prev[i], scores[i] + prev[i-1], curr[i-1])

    print(prev)
    print(curr)
    print()
    prev = curr[:]

print(curr[-1])


    

    

