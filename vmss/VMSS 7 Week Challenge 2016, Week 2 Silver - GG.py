import sys
raw_input = sys.stdin.readline
word = raw_input()
ans = [0]

for letter in word:
    if letter == "G":
        ans += [1+ans[-1]]
    else:
        ans += [ans[-1]]

n = int(raw_input())

for i in xrange(n):
    a, b = map(int, raw_input().split())
    print ans[b+1] - ans[a]
