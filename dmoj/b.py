h = int(raw_input())
m = int(raw_input())

for i in xrange(1, m + 1):
    a = -6*(i**4) + h*(i**3) + 2*(i**2) + i
    if a <= 0:
        print "The balloon first touches ground at hour:"
        print i
        break
    if i == m and a > 0:
        print "The balloon does not touch ground in the given time."
