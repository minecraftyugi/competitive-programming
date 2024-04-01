x = input()
m = input()

for i in xrange(1, m):
    if (x*i)%m == 1:
        print i
        raise SystemExit

print "No such integer exists."
