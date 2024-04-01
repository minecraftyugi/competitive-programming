n = input()

for i in xrange(n):
    l, a, b, f = map(int, raw_input().split())
    diff = l - f
    if diff >= a and diff <= b:
        print "Yes"
    else:
        print "No"
