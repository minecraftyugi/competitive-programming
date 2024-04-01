trout = int(raw_input())
pike = int(raw_input())
pickerel = int(raw_input())
amount = int(raw_input())
count = 0

for i in xrange(amount / trout + 1):
    for j in xrange(amount / pike + 1):
        for k in xrange(amount / pickerel + 1):
            if i * trout + j * pike + k * pickerel <= amount and i + j + k != 0:
                print str(i) + " Brown Trout, " + str(j) + " Northern Pike, " + str(k) + " Yellow Pickerel"
                count += 1

print "Number of ways to catch fish: " + str(count)                
