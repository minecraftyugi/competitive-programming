#get rid of sys in case of error reading input
#time complexity O(n)
#runs faster in pypy2, code compiles in python 2.7.8

import sys
raw_input = sys.stdin.readline

num = int(raw_input())
group = [int(raw_input()) for i in xrange(num)]
group.reverse()

check = 0

for i in range(num - 1):
    if group[i] > 1:
            if group[i] < group[i + 1] and group.index(group[i] - 1) > i:
                check = 1
                break

    if i < (len(group) - 2) and group[i] == 1:
        if group[i + 1] > group[i] and group[i + 1] - group[i + 2] >= 2:
            check = 1
            break
        
if check == 1:
    print "no"
else:
    print "yes"

