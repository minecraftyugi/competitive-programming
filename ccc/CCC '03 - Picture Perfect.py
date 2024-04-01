number = ""
while number != 0:
    number = int(raw_input())
    if number == 0:
        break
    numList = []
    for i in xrange(1,number + 1):
        dim = number % i
        if dim == 0:
            numList.append(number / i)
    if len(numList) % 2 != 0:
        length = numList[len(numList) / 2]
        print "Minimum perimeter is " + str(length * 4) + " with dimensions " + str(length) + " x " + str(length)
    else:
        length1 = numList[len(numList) / 2]
        length2 = numList[len(numList) / 2 - 1]
        print "Minimum perimeter is " + str(length1 * 2 + length2 * 2) + " with dimensions " + str(length1) + " x " + str(length2)
        
