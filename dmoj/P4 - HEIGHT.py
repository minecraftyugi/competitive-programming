n = input()
numbers = [0]*n
ans = [0]*n
for i in xrange(n):
    num = input()
    numbers[i] = num
    ans[i] = num
    for j in xrange(i-1, -1, -1):
        if num > numbers[j]:
            ans[i] = max(ans[i], num + ans[j])

print max(ans)
