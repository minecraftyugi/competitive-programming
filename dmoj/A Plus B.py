number = int(raw_input())

for i in xrange(number):
    add = raw_input()
    addList = add.split()
    addList[0] = int(addList[0])
    addList[1] = int(addList[1])
    answer = addList[0] + addList[1]
    print answer
