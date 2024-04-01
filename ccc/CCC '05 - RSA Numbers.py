low = int(raw_input())
high = int(raw_input())
counter = 0

for i in xrange(low, high + 1):
    a = 0
    for j in xrange(i, 0, -1):
        if i % j == 0:
            a = a + 1
        if a > 4:
            break
    if a > 4 or a < 4:
        pass
    if a == 4:
        counter = counter + 1

print "The number of RSA numbers between "+str(low)+" and "+str(high)+" is "+str(counter)
        
