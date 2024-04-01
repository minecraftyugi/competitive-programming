num = int(raw_input())
boxList = []

for i in xrange(num):
    box = sorted(map(int, raw_input().split()))
    boxList.append(box)
    
boxList = sorted(boxList, key = lambda mul: mul[0] * mul[1] * mul[2])
num2 = int(raw_input())

for i in xrange(num2):
    item = sorted(map(int, raw_input().split()))
    check = 0 
    for j in xrange(len(boxList)):
        if item[0] <= boxList[j][0] and item[1] <= boxList[j][1] and item[2] <= boxList[j][2]:
            check = 1
            break
    if check == 1:
       ans = boxList[j][0] * boxList[j][1] * boxList[j][2]
       print ans
    else:
        print "Item does not fit."
