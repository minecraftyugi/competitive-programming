d = int(raw_input())

for i in xrange(1, d + 1):
    t = int(raw_input())
    count = 0
    for j in xrange(t):
        num = int(raw_input())
        count += num

    if count == 0:
        print "Weekend"
    else:
        print "Day {}: {}".format(i, count)
