import collections
n = input()
s1 = raw_input()
s2 = raw_input()
dict1 = collections.defaultdict(list)

for index, value in enumerate(s2):
    dict1[value].append(index)

def checker1(possible, count):
    remove = []
    
    if count == n:
        return min(possible)

    for place in possible:
        position = possible[place] % n
        if s1[count] == s2[position]:
            possible[place] += 1
        else:
            remove.append(place)

    for possibility in remove:
        del possible[possibility]

    if len(possible) == 0:
        return -1
    
    return checker1(possible, count + 1)

def checker2(possible, count):
    remove = []
    
    if count == -1:
        return max(possible)

    for place in possible:
        position = possible[place] % n
        if s1[count] == s2[position]:
            possible[place] -= 1
        else:
            remove.append(place)

    for possibility in remove:
        del possible[possibility]

    if len(possible) == 0:
        return -1
    
    return checker2(possible, count - 1)

if s1[0] not in dict1:
    print -1
else:
    start = dict1[s1[0]]
    dict2 = {i:i for i in start}
    answer1 = checker1(dict2, 0)
    start = dict1[s1[-1]]
    dict2 = {i:i for i in start}
    answer2 = checker2(dict2, n-1)
    if answer1 == -1:
        print -1
    elif answer1 == n-1-answer2:
        print "L"+str(answer1)
    elif answer1 > n-1-answer2:
        print "L"+str(n-1-answer2)
    else:
        print "R"+str(answer1)
