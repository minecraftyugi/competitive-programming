a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())
s = int(raw_input())

Bpos = 0
Npos = 0
Bstep = 0
Nstep = 0

for i in xrange(s):
    if Bstep == s and Nstep == s:
        break
    for i in xrange(a):
        if Nstep == s:
            break
        Npos += 1
        Nstep += 1

    for i in xrange(b):
        if Nstep == s:
            break
        Npos -= 1
        Nstep += 1

    for i in xrange(c):
        if Bstep == s:
            break
        Bpos += 1
        Bstep += 1
    for i in xrange(d):
        if Bstep == s:
            break
        Bpos -= 1
        Bstep += 1
    #print "NIKKY :"+str(Npos)
    #print "BYRON :"+str(Bpos)
if Bpos > Npos:
    print "Byron"
elif Bpos < Npos:
    print "Nikky"
else:
    print "Tied"
