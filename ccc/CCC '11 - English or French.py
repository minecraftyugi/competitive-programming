num = int(raw_input())
countS = 0
countT = 0

for i in xrange(num):
    string = raw_input()
    string = string.lower()
    t = string.count("t")
    s = string.count("s")
    countS = countS + s
    countT = countT + t
    
if countS >= countT:
    print "French"
else:
    print "English"
