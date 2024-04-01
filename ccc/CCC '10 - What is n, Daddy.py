num = int(raw_input())
count = 0

if num <= 5:
    for i in xrange(num):
        if i > (num - i):
            break
        count += 1
    print count
else:
    for i in xrange(num):
        if i <= 5 and (num - i) <= 5 and i <= (num - i):
            count += 1
    print count
