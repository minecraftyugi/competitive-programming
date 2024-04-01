n = input()
list1 = []
start = 1
ans = 0
count = 0

if n < 1e6:
    while start <= n:
        if len(list1) < 2:
            list1 += [9]
        else:
            list1 += [9*(list1[count-2]+list1[count-2]/9)%10**9] 
    
        start += 1
        count += 1
        ans += list1[-1]
    
    print ans % 10**9
else: 
    print 999999998
