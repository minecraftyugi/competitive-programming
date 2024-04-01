import collections

for i in xrange(10):
    dict1 = collections.defaultdict(int)
    count = 0
    
    while 1:
        color = raw_input()
        if color == "end of box":
            break
        else:
            dict1[color] += 1

    for color in dict1:
        if color == "red":
            count += dict1[color] * 16
        else:
            count += dict1[color] / 7 * 13
            if dict1[color] % 7:
                count += 13

    print count
