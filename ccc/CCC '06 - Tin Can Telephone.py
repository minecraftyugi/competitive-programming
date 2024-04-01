rX, rY, jX, jY = map(int, raw_input().split())

try:
    m = float(jY - rY) / (jX - rX)
    b = rY - (m * rX)
except ZeroDivisionError:
    x = rX
    
num = int(raw_input())
count = 0

for i in xrange(num):
    numbers = map(int, raw_input().split())
    times = numbers.pop(0)
    check = 0
    
    for j in xrange(times-1):
        x2 = 0
        del x2

        X1 = numbers[j*2]
        Y1 = numbers[j*2+1]
        X2 = numbers[j*2+2]
        Y2 = numbers[j*2+3]

        try:
            n = float(Y2 - Y1) / (X2 - X1)
            c = Y2 - (n * X2)
        except ZeroDivisionError:
            x2 = X2 

        try:
            x
        except NameError:
            try:
                x2
            except NameError:
                if m == n:
                    continue
                xint = float(c - b) / (m - n)
                yint = n * xint + c
            else:
                xint = x2
                yint = m * xint + b
        else:
            try:
                x2
            except NameError:
                xint = x
                yint = n * xint + c
            else:
                xint = 10000
                yint = 10000

        if X1 > X2 and Y1 > Y2:
            if xint > X1 or xint < X2 or yint > Y1 or yint < Y2:
                continue
        elif X1 > X2 and Y1 < Y2:
            if xint > X1 or xint < X2 or yint < Y1 or yint > Y2:
                continue
        elif X1 > X2 and Y1 == Y2:
            if xint > X1 or xint < X2 or yint > Y1 or yint < Y2:
                continue
        elif X1 < X2 and Y1 > Y2:
            if xint < X1 or xint > X2 or yint > Y1 or yint < Y2:
                continue
        elif X1 < X2 and Y1 < Y2:
            if xint < X1 or xint > X2 or yint < Y1 or yint > Y2:
                continue
        elif X1 < X2 and Y1 == Y2:
            if xint < X1 or xint > X2 or yint > Y1 or yint < Y2:
                continue
        elif X1 == X2 and Y1 > Y2:
            if xint > X1 or xint < X2 or yint > Y1 or yint < Y2:
                continue
        elif X1 == X2 and Y1 < Y2:
            if xint > X1 or xint < X2 or yint < Y1 or yint > Y2:
                continue
        else:
            if xint > X1 or xint < X2 or yint > Y1 or yint < Y2:
                continue
        
        if jX > rX and jY > rY:
            if xint <= jX and xint >= rX and yint <= jY and yint >= rY:
                check = 1
                break
        elif jX > rX and jY < rY:
            if xint <= jX and xint >= rX and yint >= jY and yint <= rY:
                check = 1
                break
        elif jX > rX and jY == rY:
            if xint <= jX and xint >= rX and yint == jY and yint == rY:
                check = 1
                break
        elif jX < rX and jY > rY:
            if xint >= jX and xint <= rX and yint <= jY and yint >= rY:
                check = 1
                break
        elif jX < rX and jY < rY:
            if xint >= jX and xint <= rX and yint >= jY and yint <= rY:
                check = 1
                break
        elif jX < rX and jY == rY:
            if xint >= jX and xint <= rX and yint == jY and yint == rY:
                check = 1
                break
        elif jX == rX and jY > rY:
            if xint == jX and xint == rX and yint <= jY and yint >= rY:
                check = 1
                break
        elif jX == rX and jY < rY:
            if xint == jX and xint == rX and yint >= jY and yint <= rY:
                check = 1
                break
        else:
            if xint == jX and xint == rX and yint == jY and yint == rY:
                check = 1
                break

    if check == 1:
        count += 1

print count
