a = [2,3,5,7,11,13,17,19,23,29]

for i in range(1, 6):
    size = reduce(lambda x,y:x*y, a[:i])
    group = [1]*size
    primeList = [1]
    
    for j in xrange(2, len(group)):
        if group[j]:
            primeList.append(j)
            
            for k in xrange(j, len(group), j):
                group[k] = 0

    for remove in a[:i]:
        if i != 1:
            primeList.remove(remove)

    initial = int(5000 / size)
    ans = len(primeList)*initial
    print ans, "\n"
    start = size*initial
    
    for number in primeList:
        if start + number < 5000:
            ans += 1
        else:
            break

    print ans
    
