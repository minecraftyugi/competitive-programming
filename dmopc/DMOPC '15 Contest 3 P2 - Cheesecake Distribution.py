num = input()
list1 = map(int, raw_input().split())
total = sum(list1)
ans = 0

if total%num != 0:
    print "Impossible"
else:
    avg = total/num
    for i in list1:
        ans += abs(i-avg)

    print ans/2
