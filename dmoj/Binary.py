number = int(raw_input())

for i in xrange(number):
    num = int(raw_input())
    convert = bin(num)
    convertList = list(convert)
    convertList.pop(0) and convertList.pop(0)
    if len(convertList) > 4:
        for j in xrange(len(convertList)-4,0,-4):
            convertList.insert(j,' ')
    if len(convertList) < 4:
        for i in xrange(len(convertList),4):
            convertList = ['0'] + convertList
    convert = "".join(convertList)
    if " " in convert[0:4]:
        lists = convert.find(" ")
        for i in xrange(lists,4):
            convert = "0" + convert
    print convert
