import math

for i in xrange(10):
    x, xp, y, yp, s, sp, n = map(float, raw_input().split())
    n = int(n)
    x = round(x * 10 ** xp, n)
    y = round(y * 10 ** yp, n)
    s = round(s * 10 ** sp, n)
    p1 = (x, y)
    p2 = (x - s/6, y + 1.0/3*math.sqrt(s**2 - s**2/4))
    p3 = (x + s/6, y + 1.0/3*math.sqrt(s**2 - s**2/4))
    p4 = (x - s/3, y + 2.0/3*math.sqrt(s**2 - s**2/4))
    p5 = (x, y + 2.0/3*math.sqrt(s**2 - s**2/4))
    p6 = (x + s/3, y + 2.0/3*math.sqrt(s**2 - s**2/4))
    p7 = (x - s/2, y + math.sqrt(s**2 - s**2/4))
    p8 = (x - s/6, y + math.sqrt(s**2 - s**2/4))
    p9 = (x + s/6, y + math.sqrt(s**2 - s**2/4))
    p10 = (x + s/2, y + math.sqrt(s**2 - s**2/4))
    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    answer = []
    
    for j in xrange(5):
        X, Xp, Y, Yp = map(float, raw_input().split())
        X = round(X * 10 ** Xp, n)
        Y = round(Y * 10 ** Yp, n)
        ans = []
        for value in points:
            a, b = value
            ans += [math.sqrt((a-X)**2 + (b-Y)**2)]

        answer += [ans.index(min(ans)) + 1]

    print " ".join(map(str, answer))
