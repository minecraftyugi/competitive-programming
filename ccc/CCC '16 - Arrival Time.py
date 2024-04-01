hour, minute = map(int, raw_input().split(":"))
ans = 0

if hour < 5:
    print "0"+`hour+2`+":"+"0"*(2-len(`minute`))+`minute`
elif hour == 5 and minute == 0:
    print "07:00"
elif hour >= 22:
    print "0"+`(hour+2)%24`+":"+"0"*(2-len(`minute`))+`minute`
elif hour >= 19:
    print `hour+2`+":"+"0"*(2-len(`minute`))+`minute`
elif hour >= 10 and hour < 13:
    print `hour+2`+":"+"0"*(2-len(`minute`))+`minute`
elif hour == 13 and minute == 0:
    print "15:00"
else:
    while 1:
        if ans == 24:
            print "0"*(2-len(`hour`))+`hour`+":"+"0"*(2-len(`minute`))+`minute`
            break
        else:
            if hour >= 7 and hour <= 9:
                ans += 1
                minute += 10
            elif hour >= 15 and hour <= 18:
                ans += 1
                minute += 10
            else:
                ans += 2
                minute += 10
            if minute == 60:
                minute = 0
                hour += 1
