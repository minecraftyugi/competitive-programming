n= input()
c = float(raw_input())

for i in xrange(n):
    price = float(raw_input())
    c -= price

if c < 0:
    print "Fardin's broke"
else:
    print "%.2f"%c
