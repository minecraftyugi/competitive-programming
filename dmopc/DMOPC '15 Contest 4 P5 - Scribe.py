import sys
raw_input = sys.stdin.readline

t = input()

for i in xrange(t):
    x, y = map(int, raw_input().split())
    ans = [0 for i in xrange(10)]
    multiplier = [10**i for i in xrange(10)]

    for i in xrange(len(str(y))):
        numbers = list(str(x))
        numbers = map(int, numbers)
        add = 10**(i+1) - numbers[-1-i]*10**(i)
        if x + add <= y:
            x += add
            thing = str(add)
            for j in xrange(len(thing)):
                number = (10**(j+1) - int(thing[j])) % 10**(j+1)
                print "number", number
                for k in xrange(number, 10):
                    ans[k] += 1 * multiplier[j]
                    
        else:
            break

        print x, ans

    for i in xrange(len(str(y))):
        numbers = list(str(y))
        numbers = map(int, numbers)
        minus = numbers[-1-i]*10**(i)
        print minus
        if y - minus > x:
            y -= minus
            thing = str(minus)
            for j in xrange(len(thing)):
                number = int(thing[j]) % 10**(j+1)
                if number == 0: number += 9
                print "number", number
                for k in xrange(number, -1, -1):
                    ans[k] += 1 * multiplier[j]
                    
        else:
            break

        print y, ans

    #for i in xrange
        
    for i in xrange(1, 101):
        i = list(str(i))
        for num in i:
            ans[int(num)] += 1

    ans = map(str, ans)
    print " ".join(ans)
