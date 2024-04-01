n, l = map(int, raw_input().split())
dict1 = {}
lists = []

for i in xrange(1, n+1):
    line = raw_input().split()[1:]
    dict1[i] = line

def gen(prev, loops, ans):
    new = set()
    for i in prev:
        ans.add(i)
        
    if loops == l:
        return ans
    
    for i in prev:
        pos = i[-1]
        for j in xrange(pos+1, n+1):
            newNum = i + (j,)
            new.add(newNum)
    
    return gen(new, loops + 1, ans)

def word(words, index, currentIndex):
    new = set()
    if currentIndex == len(index):
        return words
    for thing in words:
        for letter in dict1[index[currentIndex]]:
            build = thing + letter
            new.add(build)
            
    return word(new, index, currentIndex + 1)

indexes = gen([(1,)], 1, set())

for tup in indexes:
    for letter in dict1[1]:
        possible = word(letter, tup, 1)
        for thing in possible:
            lists.append(thing)

lists.sort()

for i in lists:
    print i
