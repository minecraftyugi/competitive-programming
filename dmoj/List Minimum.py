number = int(raw_input())
numList = []

for i in xrange(number):
    num = int(raw_input())
    numList.append(num)

numList.sort()

for i in xrange(number):
    print min(numList)
