num = int(raw_input())

for i in xrange(num):
    thing = raw_input()
    number = list(bin(int(thing,16)))[2:]
    index = len(number) - 21
    if index < 0:
        print thing
    else:
        if number[index] == "0":
            print thing
            continue
        number[index] = "0"
        number = list(hex(int("".join(number),2))[2:].upper())
        number = ["0" for i in xrange(8 - len(number))] + number
        print "".join(number), thing
