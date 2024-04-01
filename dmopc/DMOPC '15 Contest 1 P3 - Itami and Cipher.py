import sys
encrypt = list(raw_input())
word = raw_input()
count = 0
check = "".join(encrypt)

if word in check:
    print 0
    print check
    sys.exit()
    
while 1:
    count += 1
    encrypt2 = []
    for i in xrange(len(encrypt)):
        letter = ord(encrypt[i])
        if letter == 97:
            encrypt2.append("z")
        else:
            encrypt2.append(chr(letter - 1))
    check = "".join(encrypt2)
    encrypt = check
    if word in check:
        print count
        print check
        break
                
