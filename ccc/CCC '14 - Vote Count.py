num = int(raw_input())
line = raw_input()
if line.count("A") > line.count("B"):
    print "A"
elif line.count("A") < line.count("B"):
    print "B"
else:
    print "Tie"
