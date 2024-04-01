street = ""
turnList = []
streetList = []

while street != "SCHOOL":
    turn = raw_input()
    street = raw_input()
    turnList.append(turn)
    if street == "SCHOOL":
        break
    streetList.append(street)

for i in xrange(len(turnList) - 1, -1, -1):
    if i == 0 and turnList[0] == "R":
        print "Turn LEFT into your HOME."
        break
    if i == 0 and turnList[0] == "L":
        print "Turn RIGHT into your HOME."
        break
    if turnList[i] == "R":
        print "Turn LEFT onto "+streetList[i-1]+" street."
    if turnList[i] == "L":
        print "Turn RIGHT onto "+streetList[i-1]+" street."
