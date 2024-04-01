import math
recruits = int(raw_input())
groups = int(raw_input())
num = int(math.ceil(float(recruits) / groups))
remaining = recruits % groups


if remaining == 0:
    print str(groups) + " group(s) of " + str(num)
else:
    count = 0
    while 1:
        if recruits % groups == 0:
            print str(count) + " group(s) of " + str(num)
            print str(groups) + " group(s) of " + str(recruits / groups)
            break
        recruits -= num
        count += 1
        groups -= 1
