import sys

#lists = map(int, sys.stdin.read().strip().split('\n'))
#lists = [6,4,2,3,1,4,4,4,1,3,2,4,2,4,1,3,2,1,2,2,2,1,1,1]
#lists = [2,4,2,3,1,4,4,4,1,3,2]
#num = lists.pop(0)
numList = []
num = input()
lists = [int(input()) for i in range(num)]

for i in range(num):
    trains = lists[1:lists[0]+1]
    trains.reverse()
    numList.append(trains)
    lists = lists[lists[0]+1:]

for group in numList:
    check = 0
    
    for i in range(len(group) - 1):
        if group[i] > 1:
            if group[i] < group[i + 1] and group.index(group[i] - 1) > i:
                check = 1
                break

        if i < (len(group) - 2) and group[i] == 1:
            if group[i + 1] > group[i] and group[i + 1] - group[i + 2] >= 2:
                check = 1
                break
        
    if check == 1:
        print "N"
    else:
        print "Y"
