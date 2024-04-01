num = int(raw_input())
dict1 = {1:100, 2:500, 3:1000, 4:5000, 5:10000, 6:25000, 7:50000, 8:100000,
         9:500000, 10:1000000}

for i in xrange(num):
    case = int(raw_input())
    del dict1[case]

offer = int(raw_input())
average = sum(dict1.values()) / len(dict1)

if offer > average:
    print "deal"
else:
    print "no deal"
