n = input()
ans = 0

for i in xrange(n):
    ans += float(raw_input())
    ans %= 360

ans %= 360
print float(ans) 
