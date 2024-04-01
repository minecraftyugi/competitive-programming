pink = int(raw_input())
green = int(raw_input())
red = int(raw_input())
orange = int(raw_input())
amount = int(raw_input())
count = 0
numList = []

for i in xrange(amount / pink + 1):
    for j in xrange(amount / green + 1):
        for k in xrange(amount / red + 1):
            for l in xrange(amount / orange + 1):
                if i * pink + j * green + k * red + l * orange == amount:
                    print "# of PINK is " + str(i) + " # of GREEN is " + str(j) + " # of RED is " + str(k) + " # of ORANGE is " + str(l)
                    count += 1
                    numList.append(i + j + k + l)

print "Total combinations is " + str(count) + "."
print "Minimum number of tickets to print is " + str(min(numList)) + "."
