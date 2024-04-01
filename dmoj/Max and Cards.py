import itertools, math
n = input()
q = input()
lists = list(itertools.permutations(range(1, n+1)))
indexes = []

for i in xrange(n):
    change = math.factorial(n-i) / (n-i)
    indexes += [change]

print indexes
    
for i in xrange(q):
    num = input()
    numbers = range(1,n+1)
    ans = []
    for i in lists[num]:
        ans += [str(i)]

    print " ".join(ans)

    #num = input() + 1
    ans = ""
    for i in xrange(n):
        index = num / indexes[i]
        diff = num % indexes[i]
        num = diff
        print "INDEX", index
        last = index
        if index > 0:
            last = n - 1 if index > n - 1 else index

            while numbers[last] == 0:
                last -= 1
            else:
                number = numbers[last]
        else:
            while numbers[last] == 0:
                last -= 1
            else:
                number = numbers[last]
        ans += str(number)+" "
        numbers[last] = 0
        #print numbers

    print ans
