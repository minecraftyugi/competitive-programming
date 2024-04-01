num = int(raw_input())

while True:
    num += 1
    lists = list(str(num))
    check = 0
    for i in xrange(len(lists)):
        if lists.count(lists[i]) > 1:
            check = 1
            break
    if check == 1:
        continue
    else:
        print num
        break
