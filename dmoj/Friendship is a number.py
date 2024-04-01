num = int(raw_input())
ans = []

for i in xrange(1, num+1):
    product = reduce(lambda x, y: x*y, map(int, raw_input().split())[1:])
    ans += (product, i),

ans.sort(key = lambda x: x[0], reverse = True)
print ans[0][1]
print ans[1][1]
print ans[2][1]
