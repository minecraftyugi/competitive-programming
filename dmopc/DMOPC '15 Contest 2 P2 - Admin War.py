num = int(raw_input())
list1 = map(int, raw_input().split())
list2 = map(int, raw_input().split())
count1 = 0
count2 = 0

for i in xrange(num):
    if list1[i] > list2[i]:
        count1 += 1
    elif list2[i] > list1[i]:
        count2 += 1
    else:
        pass

print count1, count2

if count1 > count2:
    print "Xyene"
elif count2 > count1:
    print "FatalEagle"
else:
    print "Tie"
