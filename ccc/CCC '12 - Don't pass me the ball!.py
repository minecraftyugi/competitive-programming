import itertools
num = int(raw_input())

if num < 4:
    print 0
else:
    numbers = [x for x in range(1, num + 1)]
    options = [x for x in itertools.combinations(numbers, 4) if num in x]
    print len(options)
