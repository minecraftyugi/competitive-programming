while 1:
    num = int(raw_input())
    if num == 0:
        break
    count = 4 * num + 1
    for i in xrange(1, num + 1):
        count += 4 * int((num**2 - i**2)**0.5)

    print count
