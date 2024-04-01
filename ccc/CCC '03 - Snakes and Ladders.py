number = ""
pos = 1

while number != 0:
    number = int(raw_input())
    if number == 0:
        print "You Quit!"
        break
    land = number + pos
    a = 0
    if land == 9:
        pos = 34
        a = 1
        print "You are now on square " + str(pos)
    if land == 40:
        pos = 64
        a = 1
        print "You are now on square " + str(pos)
    if land == 67:
        pos = 86
        a = 1
        print "You are now on square " + str(pos)
    if land == 54:
        pos = 19
        a = 1
        print "You are now on square " + str(pos)
    if land == 90:
        pos = 48
        a = 1
        print "You are now on square " + str(pos)
    if land == 99:
        pos = 77
        a = 1
        print "You are now on square " + str(pos)
    if land > 100:
        a = 1
        print "You are now on square " + str(pos)
    if land == 100:
        print "You are now on square 100"
        print "You Win!"
        break
    if a == 0:
        pos = land
        print "You are now on square " + str(pos)
