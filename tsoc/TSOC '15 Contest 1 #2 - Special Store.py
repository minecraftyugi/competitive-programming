import sys
raw_input = sys.stdin.readline
r, c = map(int, raw_input().split())
w, l = map(int, raw_input().split())
num = int(raw_input())
dict1 = {}
ans = {0:set()}

for i in xrange(1, num+1):
    x, y = map(int, raw_input().split())
    ans[i] = ans[i-1] | {(x, y)}
    dict1[i] = []
    #Area
    dict1[i] += set((a, b) for a in xrange(x, x+w) for b in xrange(y-l+1, y+1)),
    dict1[i] += set((a, b) for a in xrange(x, x+w) for b in xrange(y, y+l)),
    dict1[i] += set((a, b) for a in xrange(x-w+1, x+1) for b in xrange(y-l+1, y+1)),
    dict1[i] += set((a, b) for a in xrange(x-w+1, x+1) for b in xrange(y, y+l)),
    #Perimeter
##    dict1[i] += set((a, y) for a in xrange(x, x+w)) | set((a, y-l+1) for a in xrange(x, x+w)) | set((x, a) for a in xrange(y-l+1, y+1)) | set((x+w-1, a) for a in xrange(y-l+1, y+1)),
##    dict1[i] += set((a, y) for a in xrange(x, x+w)) | set((a, y+l-1) for a in xrange(x, x+w)) | set((x, a) for a in xrange(y, y+l)) | set((x+w-1, a) for a in xrange(y, y+l)),
##    dict1[i] += set((a, y) for a in xrange(x-w+1, x+1)) | set((a, y-l+1) for a in xrange(x-w+1, x+1)) | set((x, a) for a in xrange(y-l+1, y+1)) | set((x-w+1, a) for a in xrange(y-l+1, y+1)),
##    dict1[i] += set((a, y) for a in xrange(x-w+1, x+1)) | set((a, y+l-1) for a in xrange(x-w+1, x+1)) | set((x, a) for a in xrange(y, y+l)) | set((x-w+1, a) for a in xrange(y, y+l)),
    for j in xrange(1, i+1):
        for group in dict1[j]:
            if group <= ans[i]:
                print "Special store was found on:", i
                sys.exit()

print "Special store was not located"

