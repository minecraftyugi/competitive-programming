houseX, houseY, schoolX, schoolY = map(int, raw_input().split())

try:
    m = (schoolY - houseY)/ float(schoolX - houseX)
    b = float(houseY - m * (houseX))
except ZeroDivisionError:
    x = houseX

count = 0
roads = int(raw_input())

for i in range(roads):
    A, B, C = map(int, raw_input().split())

    if A == 0 and B == 0:
        continue
    elif B == 0:
        x2 = -1 * float(C)/A
    else:
        n = -1 * float(A)/B
        c = -1 * float(C)/B

    try:
        m
    except NameError:
        try:
            n
        except NameError:
            xint = float(1000000000)
            yint = float(1000000000)
        else:
            xint = float(x)
            yint = float(n * xint + c)
    else:
        try:
            n
        except NameError:
            xint = float(x2)
            yint = float(m * xint + b)
        else:
            xint = float(c - b) / (m - n)  
            yint = float(m * xint + b)
    
    if houseX < schoolX and houseY < schoolY:
        if xint >= houseX and xint <= schoolX and yint >= houseY and yint <= schoolY:
            count += 1
    elif houseX > schoolX and houseY < schoolY:
        if xint >= schoolX and xint <= houseX and yint >= houseY and yint <= schoolY:
            count += 1
    elif houseX < schoolX and houseY > schoolY:
        if xint >= houseX and xint <= schoolX and yint >= schoolY and yint <= houseY:
            count += 1
    elif houseX > schoolX and houseY > schoolY:
        if xint >= schoolX and xint <= houseX and yint >= schoolY and yint <= houseY:
            count += 1
    elif houseX == schoolX and houseY > schoolY:
        if xint == float(schoolX) and xint == float(houseX) and yint >= schoolY and yint <= houseY:
            count += 1
    elif houseX == schoolX and houseY < schoolY:
        if xint == float(schoolX) and xint == float(houseX) and yint >= houseY and yint <= schoolY:
            count += 1
    elif houseX > schoolX and houseY == schoolY:
        if xint >= schoolX and xint <= houseX and yint == float(houseY) and yint == float(schoolY):
            count += 1
    elif houseX < schoolX and houseY == schoolY:
        if xint >= houseX and xint <= schoolX and yint == float(houseY) and yint == float(schoolY):
            count += 1
    else:
        if xint == float(schoolX) and xint == float(houseX) and yint == float(houseY) and yint == float(schoolY):
            count += 1

    n = 0
    del n
            
print count
