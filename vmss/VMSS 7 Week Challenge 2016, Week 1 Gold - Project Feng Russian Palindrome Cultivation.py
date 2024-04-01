import sys
n = raw_input()
length = len(n)
ans = list(n)

if length == 1:
    print int(n) + 1
    sys.exit()
    
for i in xrange(length/2+length%2):
    start = n[i]
    ans[length-i-1] = start

ans2 = "".join(ans)

if ans2 > n:
    print ans2
    
else:
    mid = length/2+length%2-1

    for i in xrange(mid,-1,-1):
        if ans[i] != "9":
            ans[i] = str(int(ans[i]) + 1)
            ans[length-i-1] = str(int(ans[length-i-1]) + 1)
            print`ans`[1::3]
            sys.exit()

    print "1"+"0"*(length-1)+"1"
