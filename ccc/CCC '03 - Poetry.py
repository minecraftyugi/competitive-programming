number = int(raw_input())

for i in xrange(number):
    line1 = raw_input()
    line2 = raw_input()
    line3 = raw_input()
    line4 = raw_input()
    list1 = line1.split()
    list2 = line2.split()
    list3 = line3.split()
    list4 = line4.split()
    rhyme1 = list1[len(list1) -1].lower()
    rhyme2 = list2[len(list2) -1].lower()
    rhyme3 = list3[len(list3) -1].lower()
    rhyme4 = list4[len(list4) -1].lower()
    rhyme1 = list(rhyme1)
    rhyme2 = list(rhyme2)
    rhyme3 = list(rhyme3)
    rhyme4 = list(rhyme4)

    for i in xrange(len(rhyme1) - 1, 0, -1):
        if rhyme1[i] == "a" or rhyme1[i] == "e" or rhyme1[i] == "i" or rhyme1[i] == "o" or rhyme1[i] == "u":
            a = i
            for j in xrange(a):
                rhyme1.pop(0)
            rhyme1 = "".join(rhyme1)
            break
    for i in xrange(len(rhyme2) - 1, 0, -1):
        if rhyme2[i] == "a" or rhyme2[i] == "e" or rhyme2[i] == "i" or rhyme2[i] == "o" or rhyme2[i] == "u":
            a = i
            for j in xrange(a):
                rhyme2.pop(0)
            rhyme2 = "".join(rhyme2)
            break
    for i in xrange(len(rhyme3) - 1, 0, -1):
        if rhyme3[i] == "a" or rhyme3[i] == "e" or rhyme3[i] == "i" or rhyme3[i] == "o" or rhyme3[i] == "u":
            a = i
            for j in xrange(a):
                rhyme3.pop(0)
            rhyme3 = "".join(rhyme3)
            break
    for i in xrange(len(rhyme4) - 1, 0, -1):
        if rhyme4[i] == "a" or rhyme4[i] == "e" or rhyme4[i] == "i" or rhyme4[i] == "o" or rhyme4[i] == "u":
            a = i
            for j in xrange(a):
                rhyme4.pop(0)
            rhyme4 = "".join(rhyme4)
            break

    x = 0
    if rhyme1 == rhyme2 == rhyme3 == rhyme4:
        x = 2
        print "perfect"
    if rhyme1 == rhyme2 and rhyme3 == rhyme4 and x != 2:
        x = 1
        print "even"
    if rhyme1 == rhyme3 and rhyme2 == rhyme4 and x != 2:
        x = 1
        print "cross"
    if rhyme1 == rhyme4 and rhyme2 == rhyme3 and x != 2:
        x = 1
        print "shell"
    if x == 0:
        print "free"
