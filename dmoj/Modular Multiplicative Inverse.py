n, mod = map(int, raw_input().split())
dict1 = {}
dict1[1] = n
index = 2
ans = n
m = mod - 2 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        print g, y, x
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

ans = modinv(n, mod)
print "ANS", ans

if mod < 3:
    pass
    if (1 * n) % mod == 1:
        print 1 % mod
    else:
        print 2 % mod
else:
    while 1:
        if index <= m:
            ans = ans**2 % mod
            dict1[index] = ans
            index *= 2
        else:
            ans = dict1[index/2]
            m -= index / 2
            index = 1
            break

    while 1:
        if m == 0:
            break
        while 1:
            if index <= m:
                index *= 2
            else:
                ans *= dict1[index/2] % mod
                m -= index / 2
                index = 1
                break

    print ans % mod
