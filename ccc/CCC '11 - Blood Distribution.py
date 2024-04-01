a = map(int, raw_input().split())
o1,o2,a1,a2,b1,b2,ab1,ab2 = a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]
b = map(int,raw_input().split())
oo1,oo2,aa1,aa2,bb1,bb2,aab1,aab2 = b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]
amount = 0

if o1 >= oo1:
    amount += oo1
    o1 -= oo1
    oo1 = 0
else:
    amount += o1
    oo1 -= o1
    o1 = 0

if o2 >= oo2:
    amount += oo2
    o2 -= oo2
    oo2 = 0
else:
    amount += o2
    oo2 -= o2
    o2 = 0
    if o1 != 0:
        if o1 >= oo2:
            amount += oo2
            o1 -= oo2
            oo2 = 0
        else:
            amount += o1
            oo2 -= o1
            o1 = 0

if a1 >= aa1:
    amount += aa1
    a1 -= aa1
    aa1 = 0
else:
    amount += a1
    aa1 -= a1
    a1 = 0
    if o1 != 0:
        if o1 >= aa1:
            amount += aa1
            o1 -= aa1
            aa1 = 0
        else:
            amount += o1
            aa1 -= o1
            o1 = 0

if a2 >= aa2:
    amount += aa2
    a2 -= aa2
    aa2 = 0
else:
    amount += a2
    aa2 -= a2
    a2 = 0
    if a1 != 0:
        if a1 >= aa2:
            amount += aa2
            a1 -= aa2
            aa2 = 0
        else:
            amount += a1
            aa2 -= a1
            a1 = 0
    if o2 != 0:
        if o2 >= aa2:
            amount += aa2
            o2 -= aa2
            aa2 = 0
        else:
            amount += o2
            aa2 -= o2
            o2 = 0
    if o1 != 0:
        if o1 >= aa2:
            amount += aa2
            o1 -= aa2
            aa2 = 0
        else:
            amount += o1
            aa2 -= o1
            o1 = 0

if b1 >= bb1:
    amount += bb1
    b1 -= bb1
    bb1 = 0
else:
    amount += b1
    bb1 -= b1
    b1 = 0
    if o1 != 0:
        if o1 >= bb1:
            amount += bb1
            o1 -= bb1
            bb1 = 0
        else:
            amount += o1
            bb1 -= o1
            o1 = 0

if b2 >= bb2:
    amount += bb2
    b2 -= bb2
    bb2 = 0
else:
    amount += b2
    bb2 -= b2
    b2 = 0
    if b1 != 0:
        if b1 >= bb2:
            amount += bb2
            b1 -= bb2
            bb2 = 0
        else:
            amount += b1
            bb2 -= b1
            b1 = 0
    if o2 != 0:
        if o2 >= bb2:
            amount += bb2
            o2 -= bb2
            bb2 = 0
        else:
            amount += o2
            bb2 -= o2
            o2 = 0
    if o1 != 0:
        if o1 >= bb2:
            amount += bb2
            o1 -= bb2
            bb2 = 0
        else:
            amount += o1
            bb2 -= o1
            o1 = 0

remainder = o1 + a1 + b1 + ab1

if remainder >= aab1:
    amount += aab1
    remainder -= aab1
else:
    amount += remainder
    remainder = 0

remainder += o2 + a2 + b2 + ab2

if remainder >= aab2:
    amount += aab2
    remainder -= aab2
else:
    amount += remainder
    remainder = 0

print amount
