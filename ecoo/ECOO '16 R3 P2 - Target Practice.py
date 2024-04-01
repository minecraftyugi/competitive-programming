import sys

raw_input = sys.stdin.readline
#f = open("DATA21.TXT", "r")
#raw_input = f.readline
def line(y, x, m):
    b = y - m * x
    return b

def intersect(m, b, l):
    x = (l - b) * (1 / m)
    return x

for i in xrange(10):
    Aw, Ah, Bx, By, Sx, Sy = map(float, raw_input().strip().split())
    ans = ""
    for i in range(5):
        Th, Tx, Ty = map(float, raw_input().strip().split())
        if Sx == 0:
            ans += "M"
        elif Sy == 0:
            if Ty >= By >= (Ty - Th):
                ans += "H"
            else:
                ans += "M"
        else:
            m = Sy / Sx
            b = line(By, Bx, m)
            done = False
            while not done:
                l = 0
                if m > 0:
                    l = Ah
                    
                intersection = intersect(m, b, l)
                if intersection < Tx:
                    m = -m
                    b = line(l, intersection, m)
                else:
                    y = (m * Tx) + b
                    if Ty >= y >= (Ty - Th):
                        ans += "H"
                    else:
                        ans += "M"

                    done = True

    print ans
