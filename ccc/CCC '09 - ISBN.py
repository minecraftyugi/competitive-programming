num = [9,7,8,0,9,2,1,4,1,8]
num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

num.append(num1)
num.append(num2)
num.append(num3)

ans = 0

for i in xrange(13):
    if i % 2 == 0:
        ans = ans + (num[i] * 1)
    else:
        ans = ans + (num[i] * 3)

print "The 1-3-sum is " +str(ans)
