num = int(raw_input())
line1 = raw_input()
line2 = raw_input()
line1 = line1.split()
line2 = line2.split()
dict1 = {}
test = 0

for i in xrange(num):
    dict1.update({line1[i] : line2[i]})

for i in xrange(num):
    if line1[i] == line2[i]:
        test = 1
        print "bad"
        break

if test == 0:
    for i in dict1:
        if i != dict1[dict1[i]]:
            test = 1
            print "bad"
            break

if test == 0:
    print "good"
