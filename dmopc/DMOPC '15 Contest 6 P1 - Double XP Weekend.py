current = input()
want = input()
bonus = input()
base = input()
coins = input()
want -= current
limit = bonus / base

if want <= 0:
    print 0
    print 0
elif 3 * limit * base <= want:
    ans = limit
    want -= 3 * limit * base
    bonus -= limit * base

    if bonus != 0:
        ans += 1
        want -= 2 * base + bonus

    num = want / (2 * base)
    ans += num
    want -= 2 * num * base
    
    if want != 0:
        ans += 1
        want -= 2 * base
        
    print ans
    print ans * coins
else:
    limit = want / (3 * base)
    ans = limit
    want -= 3 * limit * base
    
    if want != 0:
        ans += 1
        want -= 2 * base + want

    print ans
    print ans * coins
