import sys

raw_input = sys.stdin.readline
n = int(raw_input().strip())
x, y = map(int, raw_input().strip().split())
tc = ""
bc = ""
lr = ""
rr = ""
tld = ""
trd = ""
bld = ""
brd = ""

for i in xrange(n):
    piece, X, Y = raw_input().strip().split()
    X = int(X)
    Y = int(Y)
    if abs(X-x) == abs(Y-y):
        if X > x and Y > y:
            if trd == "":
                trd = (piece, X, Y)
            else:
                if X < trd[1] and Y < trd[2]:
                    trd = (piece, X, Y)
        elif X < x and Y > y:
            if tld == "":
                tld = (piece, X, Y)
            else:
                if X > tld[1] and Y < tld[2]:
                    tld = (piece, X, Y)
        elif X > x and Y < y:
            if brd == "":
                brd = (piece, X, Y)
            else:
                if X < brd[1] and Y > brd[2]:
                    brd = (piece, X, Y)
        else:
            if bld == "":
                bld = (piece, X, Y)
            else:
                if X > bld[1] and Y > bld[2]:
                    bld = (piece, X, Y)
    elif X == x:
        if Y > y:
            if tc == "":
                tc = (piece, X, Y)
            else:
                if Y < tc[2]:
                    tc = (piece, X, Y)
        else:
            if bc == "":
                bc = (piece, X, Y)
            else:
                if Y > bc[2]:
                    bc = (piece, X, Y)
    elif Y == y:
        if X > x:
            if rr == "":
                rr = (piece, X, Y)
            else:
                if X < rr[1]:
                    rr = (piece, X, Y)
        else:
            if lr == "":
                lr = (piece, X, Y)
            else:
                if X > lr[1]:
                    lr = (piece, X, Y)                  
    else:
        pass

if tc != "":
    if tc[0] == "Q" or tc[0] == "R":
        print "Yes"
        raise SystemExit

if bc != "":
    if bc[0] == "Q" or bc[0] == "R":
        print "Yes"
        raise SystemExit

if lr != "":
    if lr[0] == "Q" or lr[0] == "R":
        print "Yes"
        raise SystemExit

if rr != "":
    if rr[0] == "Q" or rr[0] == "R":
        print "Yes"
        raise SystemExit

if trd != "":
    if trd[0] == "Q" or trd[0] == "B":
        print "Yes"
        raise SystemExit

if tld != "":
    if tld[0] == "Q" or tld[0] == "B":
        print "Yes"
        raise SystemExit

if brd != "":
    if brd[0] == "Q" or brd[0] == "B":
        print "Yes"
        raise SystemExit

if bld != "":
    if bld[0] == "Q" or bld[0] == "B":
        print "Yes"
        raise SystemExit

print "No"
