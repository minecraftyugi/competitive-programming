num = int(raw_input())

for i in xrange(num):
    date = raw_input()
    date = date.split(" ")
    if int(date[0]) > 1989:
        print "No"
        continue
    if (int(date[0]) > 1989 or int(date[0]) == 1989) and int(date[1]) > 2:
        print "No"
        continue
    if (int(date[0]) > 1989 or int(date[0]) == 1989) and (int(date[1]) > 2 or int(date[1]) == 2) and int(date[2]) > 27:
        print "No"
        continue

    print "Yes"
    
