day = int(raw_input())
night = int(raw_input())
wknd = int(raw_input())

day1 = (day - 100)
if day1 < 0:
    day1 = 0
else:
    day1 = day1 * 0.25

day2 = (day - 250)
if day2 < 0:
    day2 = 0
else:
    day2 = day2 * 0.45

night1 = night * 0.15
night2 = night * 0.35
wknd1 = wknd * 0.20
wknd2 = wknd * 0.25

plana = day1 + night1 + wknd1
planb = day2 + night2 + wknd2

print "Plan A costs " + str(plana)
print "Plan B costs " + str(planb)

if str(plana) == str(planb):
    print "Plan A and B are the same price."
elif plana < planb:
    print "Plan A is cheapest."
else:
    print "Plan B is cheapest."
