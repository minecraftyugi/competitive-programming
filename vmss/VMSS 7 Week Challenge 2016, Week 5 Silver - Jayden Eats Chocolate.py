n = input()
x, y, z = map(int, raw_input().split())
ans = [0]*(n+1)

for i in xrange(x, n+1):
    if i == x:
        ans[i] = max(ans[i], ans[i-x] + 1)
        continue
    if ans[i-x] != 0:
        ans[i] = max(ans[i], ans[i-x] + 1)

for i in xrange(y, n+1):
    if i == y:
        ans[i] = max(ans[i], ans[i-x] + 1)
        continue
    if ans[i-y] != 0:
        ans[i] = max(ans[i], ans[i-y] + 1)

for i in xrange(z, n+1):
    if i == z:
        ans[i] = max(ans[i], ans[i-x] + 1)
        continue
    if ans[i-z] != 0:
        ans[i] = max(ans[i], ans[i-z] + 1)

print ans[-1]
