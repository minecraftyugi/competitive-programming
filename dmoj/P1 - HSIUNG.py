a, b, c = map(int, raw_input().split())
dp = [1] + [0]*c
for i in xrange(c+1):
    if dp[i]:
        if i + a <= c:
            dp[i+a] = 1

        if i + b <= c:
            dp[i+b] = 1

found = False
index = c
while not found:
    if dp[index]:
        print index
        found = True

    index -= 1
