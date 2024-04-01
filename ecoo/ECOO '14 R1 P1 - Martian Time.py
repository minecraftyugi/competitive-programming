import math
earth = 60 * 60 * 24
mars = 24*60*60 + 37*60 + 22.663
RATIO = mars / earth

for i in xrange(10):
    d, h, m = map(int, raw_input().split())
    seconds = ((d-1) * 24 * 60 * 60) + (h * 60 * 60) + (m * 60)
    marsSeconds = seconds / RATIO

    mDays = int(math.floor(marsSeconds / earth))

    marsSeconds -= earth * mDays
    
    hDays = int(math.floor(marsSeconds / (60 * 60)))

    marsSeconds -= (60 * 60) * hDays

    sDays = int(marsSeconds / (60))

    marsSeconds -= (60) * sDays
    
    if sDays < 10:
        sDays = "0" + str(sDays)
    if hDays < 10:
        hDays = "0" + str(hDays)
        
    print "Day {}, {}:{}".format(mDays+1, hDays, sDays)
