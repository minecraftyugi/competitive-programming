import sys, bisect
lists = sys.stdin.read().strip().split('\n')
#lists = ["7 2", "5 4 5 2 3 1 5", "2 4", "1 6"]
#lists = ['10 5', '2 2 9 5 2 2 10 4 3 8', '2 4', '2 7', '3 10', '6 6', '10 10']
shows = map(int, lists[1].split())
first = map(int, lists[0].split())
listLen = first[0]
times = first[1]
dict1 = {}
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]

for i in xrange(listLen):
    if shows[i] == 1:
        list1.append(i)
    elif shows[i] == 2:
        list2.append(i)
    elif shows[i] == 3:
        list3.append(i)
    elif shows[i] == 4:
        list4.append(i)
    elif shows[i] == 5:
        list5.append(i)
    elif shows[i] == 6:
        list6.append(i)
    elif shows[i] == 7:
        list7.append(i)
    elif shows[i] == 8:
        list8.append(i)
    elif shows[i] == 9:
        list9.append(i)
    else:
        list10.append(i)

if list1 != []:
    dict1[1] = list1
if list2 != []:
    dict1[2] = list2
if list3 != []:
    dict1[3] = list3
if list4 != []:
    dict1[4] = list4
if list5 != []:
    dict1[5] = list5
if list6 != []:
    dict1[6] = list6
if list7 != []:
    dict1[7] = list7
if list8 != []:
    dict1[8] = list8
if list9 != []:
    dict1[9] = list9
if list10 != []:
    dict1[10] = list10

for i in xrange(2, times+2):
    tup = map(int, lists[i].split())
    start = tup[0]
    stop = tup[1]

    for j in xrange(10, 0, -1):
        if j not in dict1:
            continue
        else:
            if dict1[j][0] < start - 1 or dict1[j][-1] >= stop:
                startIndex = bisect.bisect_left(dict1[j], start - 1)
                stopIndex = bisect.bisect_left(dict1[j], stop, lo=startIndex)
                maximum = j
                count = startIndex + len(dict1[j]) - stopIndex
                break
            else:
                continue
          
    print str(maximum) + " " + str(count)
