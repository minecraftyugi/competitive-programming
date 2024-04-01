while True:
    try:
        line = raw_input()
        numList = []
        tempList = []
        find = []
        if line == "0":
            break
        line = line.split()
        if line[0] == "1":
            print 0
            continue
        line = map(int, line)
        line.pop(0)
        end = len(line)
        for i in xrange(len(line)):
            numList.append(line[i])
        for i in xrange(end - 1):
            tempList.append(numList[i + 1] - numList[i])
        if len(tempList) >= 1:
            test = tempList[0]
        for i in xrange(end - 1):
            if tempList[i] == test:
                find.append(i)
        if len(find) == 1:
            print len(tempList)
            continue
        if len(find) >= 1:
            find.pop(0)
        for i in find:
            test = 0
            #print i
            for j in xrange(len(tempList) - 1, 0, -1):
                if (j - i) == 0:
                    if tempList[j] == tempList[j - i]:
                        print i
                        test = 1
                        break
                    else:
                        if i == find[len(find) - 1]:
                            print len(tempList)
                            break
                        else:
                            break
                if tempList[j] == tempList[j - i]:
                    continue
                else:
                    if i == find[len(find) - 1]:
                        print len(tempList)
                        break
                    else:
                        break
            if test == 1:
                break
    except EOFError:
        break
"""
Your output (clipped) good OUTPUT 5,7
6 1 4 7 12 43 -31
10 100 99 88 9

Your output (clipped) good OUTPUT 1,19,2,2
20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

Your output (clipped) good OUTPUT 0,1,1,2
1 0
2 10 11
3 10 11 12
3 10 -9 1

Your output (clipped) good OUTPUT 2,4
7 1 -9 1 -9 1 -9 1
11 1 10 13 45

Your output (clipped) 17
18 -10 1 3 4 6 7 9 10 12 13 15 1 ... 19 21 22 24 25
"""
