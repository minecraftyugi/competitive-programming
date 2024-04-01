dice1 = int(raw_input())
dice2 = int(raw_input())
count = 0

for i in xrange(1, dice1 + 1):
    if i > 10:
        break
    for j in xrange(1, dice2 + 1):
        if i + j == 10:
            count += 1

if count == 1:
    print "There is 1 way to get the sum 10."
else:
    print "There are "+str(count)+" ways to get the sum 10."
