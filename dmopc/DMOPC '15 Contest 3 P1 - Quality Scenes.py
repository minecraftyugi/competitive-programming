a,b,c,d = input(),input(),input(),input()
range1 = set([i for i in xrange(a,b)])
range2 = set([i for i in xrange(c,d)])
test = range1.union(range2)
if len(test) < len(range1) + len(range2):
    print "YES"
else:
    print "NO"
