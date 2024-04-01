thing = raw_input()
clubs = []
diamonds = []
hearts = []
spades = []
suit = ""
cCount = dCount = hCount = sCount = 0

for i in thing:
    if i == "C":
        suit = "C"
    elif i == "D":
        suit = "D"
    elif i == "H":
        suit = "H"
    elif i == "S":
        suit = "S"
    else:
        if i == "J":
            new = 1
        elif i == "Q":
            new = 2
        elif i == "K":
            new = 3
        elif i == "A":
            new = 4
        else:
            new = 0
            
        if suit == "C":
            cCount += new
            clubs.append(i)
        elif suit == "D":
            dCount += new
            diamonds.append(i)
        elif suit == "H":
            hCount += new
            hearts.append(i)
        else:
            sCount += new
            spades.append(i)

if len(clubs) < 3:
    cCount += 3 - len(clubs)
if len(diamonds) < 3:
    dCount += 3 - len(diamonds)
if len(hearts) < 3:
    hCount += 3 - len(hearts)
if len(spades) < 3:
    sCount += 3 - len(spades)

clubs.insert(0, "Clubs")
diamonds.insert(0, "Diamonds")
hearts.insert(0, "Hearts")
spades.insert(0, "Spades")

print "Cards Dealt Points"
print " ".join(clubs), cCount
print " ".join(diamonds), dCount
print " ".join(hearts), hCount
print " ".join(spades), sCount
print "Total", sum([cCount, dCount, hCount, sCount])
