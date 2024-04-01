import collections, sys
dict1 = collections.defaultdict(list)
word = list(enumerate(list(raw_input())))

for index, letter in word:
    dict1[letter]+=[index]

list1 = [sorted([x,y])for z in dict1.values()for x in z for y in z]
list1.sort(key = lambda x:abs(x[0]-x[1]), reverse=True)

for x, y in list1:
    start = x
    end = y
    while 1:
        if word[start][1]==word[end][1]:
            start += 1
            end -= 1
            if start > end:
                print abs(y-x)+1
                sys.exit()
        else:
            break
