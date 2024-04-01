num = int(raw_input())

for i in xrange(num):
    x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())
    a = ((x2-x1)**2 + (y2-y1)**2)**0.5
    b = ((x3-x1)**2 + (y3-y1)**2)**0.5
    c = ((x2-x3)**2 + (y2-y3)**2)**0.5
    perimeter = a + b + c
    s = perimeter / float(2)
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print "{0:.4f}".format(round(area,4)), "{0:.4f}".format(round(perimeter,4))
