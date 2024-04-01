import sys
num = int(raw_input())
if num == 0:
    sys.exit()
prefName = []
prefScore = []
for i in xrange(num):
    cpu = raw_input()
    cpu = cpu.split(" ")
    name = str(cpu[0])
    r = int(cpu[1])
    s = int(cpu[2])
    d = int(cpu[3])
    score = (2*r) + (3*s) + d
    prefName.append(name+" "+str(score))
    prefScore.append(score)

prefName.sort()
prefName = " ".join(prefName)
prefName = prefName.split(" ")

if num == 1:
    print prefName[0]
else:
    best1 = max(prefScore)
    best1 = prefName.index(str(best1))
    print prefName[best1 - 1]
    prefName.pop(best1)
    prefName.pop(best1 - 1)
    prefScore.pop(prefScore.index(max(prefScore)))
    best2 = max(prefScore)
    best2 = prefName.index(str(best2))
    print prefName[best2 - 1]

