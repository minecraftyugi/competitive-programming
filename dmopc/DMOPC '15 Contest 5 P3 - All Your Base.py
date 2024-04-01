e, n = map(int, raw_input().split())
list1 = [e] + map(int, raw_input().split())

start = list1[-1]

for i in xrange(n - 1, -1, -1):
    num = str(list1[i])
    index = 0
    ans = 0
    for j in xrange(len(num)-1, -1, -1):
        ans += int(num[j]) * start**index
        index += 1

    start = ans

print ans
