import math
num = int(raw_input())
string = "WELCOME TO CCC GOOD LUCK TODAY"
newNum = num
numRange = []
ans = []

if num <= 29:
    for h in xrange(int(math.ceil(30 / float(num)))):
        signList = []
        dotList = []
        dotTest = 0
        if h == 0:
            start = 0
            stop = num
            step = 1
        else:
            if (newNum + num) <= 29:
                start = newNum
                stop = newNum + num
                step = 1
                pass
            else:
                start = newNum
                stop = 30
                step = 1
                pass
        #print "START: "+str(start)+" STOP: "+str(stop)
        for i in xrange(start, stop, step):
            signList.append(string[i])
            #print signList
            if i == stop - 1:
                for j in xrange(stop - 1, 0, -1):
                    if h == (int(math.ceil(30 / float(num)) - 1)) or string[j + 1] == " ":
                        dotCount = signList.count(" ") + num - len(signList)
                        newStr = "".join(signList)
                        numRange.append(newStr)
                        newStr = newStr.split(" ")
                        if len(newStr) >= 2:
                            dotLen = int(math.ceil(float(dotCount) / (len(newStr) - 1)))
                        preAns = []
                        for k in xrange(len(newStr) - 1):
                            if k == 0:
                                dotList.append("." * dotLen)
                                dotTest = dotCount - dotLen
                                continue
                            if dotCount % dotLen == 0 and dotCount % (len(newStr) - 1) == 0:
                                dotList.append("." * dotLen)
                                continue
                            if dotTest == "stop":
                                dotList.append("." * (dotLen - 1))
                                continue
                            if dotTest % (len(newStr) - 1 - k) != 0:
                                dotList.append("." * dotLen)
                                dotTest = dotTest - dotLen
                            else:
                                dotList.append("." * (dotLen - 1))
                                dotTest = "stop"
                        for l in xrange(len(newStr)):
                            if len(newStr) == 1:
                                preAns = newStr[0] + "." * dotCount
                                ans.append(preAns)
                            else:
                                if l != len(newStr) - 2:
                                    preAns.append(newStr[l] + dotList[l])
                                else:
                                    preAns.append(newStr[l] + dotList[l] + newStr[l + 1])
                                    preAns = "".join(preAns)
                                    ans.append(preAns)
                                    break   
                        break
                    else:
                        signList.pop(len(signList) - 1)
                else:
                    pass
        newNum = " ".join(numRange)
        #print newNum
        newNum = len(newNum) + 1
        #print newNum
        #print numRange
            
#print dotList
#print preAns
#print newNum
    for i in xrange(len(ans)):
        print ans[i]

else:
    ans = []
    dotList = []
    dotTest = 0
    newStr = string.split(" ")
    newNum = num - len(string)
    dotCount = string.count(" ") + newNum
    dotLen = int(math.ceil(float(dotCount) / string.count(" ")))
    #print "DOTCOUNT: "+str(dotCount)
    #print "DOTLEN: "+str(dotLen)
    for h in xrange(string.count(" ")):
        if h == 0:
            dotList.append("." * dotLen)
            dotTest = dotCount - dotLen
            continue
        if dotCount % dotLen == 0 and dotCount % (string.count(" ")) == 0:
            dotList.append("." * dotLen)
            continue
        if dotTest == "stop":
            dotList.append("." * (dotLen - 1))
            continue
        if dotTest % (string.count(" ") - h) != 0:
            dotList.append("." * dotLen)
            dotTest = dotTest - dotLen
        else:
            dotList.append("." * (dotLen - 1))
            dotTest = "stop"
    for i in xrange(len(dotList)):
        ans.append(newStr[i])
        ans.append(dotList[i])
        if i == (len(dotList) - 1):
            ans.append(newStr[len(newStr) - 1])
    ans = "".join(ans)
    print ans
