time = int(raw_input())
timeLen = len(str(time))
timeList = list(str(time))
timeList = map(int, timeList)

print str(time) + " in Ottawa"

if time >= 300:
    print str(time - 300) + " in Victoria"
else:
    print str(2400 - 300 + time) + " in Victoria"

if time >= 200:
    print str(time - 200) + " in Edmonton"
else:
    print str(2400 - 200 + time) + " in Edmonton"

if time >= 100:
    print str(time - 100) + " in Winnipeg"
else:
    print str(2400 - 100 + time) + " in Winnipeg"

print str(time) + " in Toronto"

if time < 2300:
    print str(time + 100) + " in Halifax"
else:
    print str(100 + time - 2400) + " in Halifax"

if time < 2230:
    if timeList[timeLen - 2] < 3:
        print str(time + 130) + " in St. John's"
    else:
        print str(time + 170) + " in St. John's" 
else:
    if timeList[timeLen - 2] < 3:
        print str(130 + time - 2400) + " in St. John's"
    else:
        print str(170 + time - 2400) + " in St. John's"
