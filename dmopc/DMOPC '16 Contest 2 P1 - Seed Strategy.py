n = input()
k = input()

for i in xrange(k):
    num = input()
    if num == 1:
        n -= 0.5
    elif num == 2:
        n -= 1
    else:
        n -= 5

if n < 0:
    print "Return"
else:
    print "Continue"
