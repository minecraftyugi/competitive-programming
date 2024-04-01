dist = input()
num = input()
lengths = []
ans = [0]*(dist+1)
ans[0] = 1

for i in xrange(num):
    length = input()
    lengths.append(length)

for length in lengths:
    for i in xrange(length, dist+1):
        if i == length:
            ans[i] = 1
        elif ans[i-length] == 0:
            continue         
        elif ans[i] == 0:
            ans[i] = 1+ans[i-length]     
        else:
            ans[i] = min(ans[i], 1+ans[i-length])

if ans[-1] == 0:
    print "Roberta acknowledges defeat."
else:
    print "Roberta wins in "+str(ans[-1])+" strokes."

