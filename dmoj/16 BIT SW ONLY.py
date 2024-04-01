number = int(raw_input())
for i in xrange(number):
    abp = raw_input()
    abpList = abp.split()
    abpList[0] = int(abpList[0])
    abpList[1] = int(abpList[1])
    abpList[2] = int(abpList[2])
    if abpList[0] * abpList[1] == abpList[2]:
        print "POSSIBLE DOUBLE SIGMA"
    else:
        print "16 BIT S/W ONLY"
