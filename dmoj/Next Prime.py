import math
number = int(raw_input())

if number == 1 or number == 2:
    print "2"
elif number == 3:
    print "3"
elif number == 4 or number == 5:
    print "5"
else:
    num = number
    while True:
        checker = 0
        if num % 2 == 0:
            num += 1
            continue
        if num % 3 == 0:
            num += 1
            continue
        factors = [i for i in range(6, int(math.ceil(math.sqrt(num)))+6, 6)]
        for i in factors:
            if num % (i - 1) == 0 or num % (i + 1) == 0:
                checker = 1
                break
        if checker == 1:
            num += 1
            continue
            
        print num
        break
