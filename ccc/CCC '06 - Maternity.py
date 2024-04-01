import string
par1 = raw_input()
par2 = raw_input()
num = int(raw_input())
dict1 = { "a" : "a",
          "b" : "b",
          "c" : "c",
          "d" : "d",
          "e" : "e",
          "A" : "A",
          "B" : "B",
          "C" : "C",
          "D" : "D",
          "E" : "E"
        }
for i in xrange(num):
    word = raw_input()
    for j in range(5):
        value = dict1[word[j]]
        if value in string.ascii_uppercase:
            if value in par1 or value in par2:
                check = 0
                continue
            else:
                check = 1
                print "Not their baby!"
                break
        else:
            if value in par1 and value in par2:
                check = 0
                continue
            else:
                check = 1
                print "Not their baby!"
                break
    if check == 0:
        print "Possible baby."
