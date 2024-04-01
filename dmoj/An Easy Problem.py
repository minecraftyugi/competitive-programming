n = input()
l = map(int, raw_input().split())
ans = [0]*32
for i in l:
    num = bin(i)[2:][::-1]
    for j in xrange(len(num)):
        if num[j] == "1":
            ans[j] += 1

print max(ans)
    
