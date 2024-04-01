n = int(raw_input())
powers = {}
start = [1, 1, 1, 0]
powers[1] = start
index = 2
m = 1000000007

while 1:
    if index <= n:
        a = start[0]
        b = start[1]
        c = start[3]
        start = [((a%m)*(a%m))%m + ((b%m)*(b%m))%m, ((b%m)*(a%m))%m + ((c%m)*(b%m))%m, ((b%m)*(a%m))%m + ((c%m)*(b%m))%m, ((b%m)*(b%m))%m + ((c%m)*(c%m))%m]    
        powers[index] = start
        index *= 2
    else:
        ans = powers[index/2]
        n -= index/2
        index = 1
        break

while 1:
    if n == 0:
        break
    while 1:
        if index <= n:
            index *= 2
        else:
            ans2 = powers[index/2]
            a = ans[0]
            b = ans[1]
            c = ans[2]
            d = ans[3]
            e = ans2[0]
            f = ans2[1]
            g = ans2[2]
            h = ans2[3]
            ans = [((a%m)*(e%m))%m + ((b%m)*(g%m))%m, ((a%m)*(f%m))%m + ((b%m)*(h%m))%m, ((c%m)*(e%m))%m + ((d%m)*(g%m))%m, ((c%m)*(f%m))%m + ((d%m)*(h%m))%m]
            n-= index/2
            index = 1
            break

print ans[1]

"""
n = int(raw_input())
a = 0
b = 1
m = 1000000007
if n > 2:
    for i in xrange(n - 1):
        c = (a%m) + (b%m)
        a = b
        b = c
    print c % m
elif n == 0:
    print "0"
else:
    print "1"
"""
