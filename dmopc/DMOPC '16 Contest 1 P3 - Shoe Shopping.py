n = input()
list1 = map(int, raw_input().split())
list2 = []
list3 = []
dp = [0]

for i in xrange(n):
    dp.append(dp[-1] + list1[i])
   
for i in xrange(n):
    if i == 0:
        list2.append(list1[0])
        list3.append(list1[0])
    elif i == 1:
        list2.append(dp[2] - dp[0] - min(list1[:2])/2.0)
        list3.append(list1[0] + list1[1])
    else:
        list2.append(dp[i+1] - dp[i-1] - min(list1[i-1:i+1])/2.0)
        list3.append(dp[i+1] - dp[i-2] - min(list1[i-2:i+1]))

dp2 = [0]
for i in xrange(n):
    if i == 0:
        dp2.append(list1[i] + dp2[i])
    elif i == 1:
        min1 = list1[i] + dp2[i]
        min2 = list2[i] + dp2[i-1]
        dp2.append(min(min1, min2))
    else:
        min1 = list1[i] + dp2[i]
        min2 = list2[i] + dp2[i-1]
        min3 = list3[i] + dp2[i-2]
        dp2.append(min(min1, min2, min3))
    
print float(dp2[-1])
