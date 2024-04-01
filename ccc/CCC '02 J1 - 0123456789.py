n = input()
horizontal = " * * *"
both = "*"+" "*5+"*"
left = "*"
right = " "*6+"*"

if n in [0,2,3,5,6,7,8,9]:
    print horizontal
    if n in [0,8,9]:
        for i in xrange(3):
            print both
            
        if n == 0:
            print ""
            for i in xrange(3):
                print both
        else:
            print horizontal
            if n == 8:
                for i in xrange(3):
                    print both
            else:
                for i in xrange(3):
                    print right

        print horizontal
    elif n in [2,3,7]:
        for i in xrange(3):
            print right
            
        if n == 7:
            for i in xrange(3):
                print right
        else:
            print horizontal
            if n == 2:
                for i in xrange(3):
                    print left
            else:
                for i in xrange(3):
                    print right

            print horizontal
    else:
        for i in xrange(3):
            print left
            
        print horizontal
        if n == 5:
            for i in xrange(3):
                print right
        else:
            for i in xrange(3):
                print both

        print horizontal
elif n == 1:
    for i in xrange(6):
        print right
else:
    for i in xrange(3):
        print both
        
    print horizontal
    for i in xrange(3):
        print right
