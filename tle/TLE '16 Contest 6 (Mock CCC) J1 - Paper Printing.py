n, m = map(int, raw_input().split())
a = input()
prev_time = 0
ans = n
found = False

for i in xrange(a):
    x, y = map(int, raw_input().split())
    n -= x - prev_time
    if n < 0:
        found = True
        print "The printer melts at {} second(s).".format(ans + 1)
        break
    else:
        n += y

    if n > m:
        found = True
        print "The printer jams at {} second(s).".format(x)
        break

    ans = n + x
    prev_time = x

if not found:
    print "The printer melts at {} second(s).".format(ans + 1)
