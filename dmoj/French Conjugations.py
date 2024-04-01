# -*- coding: cp1252 -*-
# ORDER {FSIMP/CPRES, FANT/CPASS/PQP, PPRES/GER/IMPF, PCOMP, PSIMP, PSIMP}

dict1 = {#VANDERTRAMP
        "DEVENIR" : ("DEVIENDR",2,"DEVEN","DEVENU","DEV",4),
        "RESTER" : ("RESTER",2,"REST","RESTÉ","REST",1),
        "MONTER" : ("MONTER",2,"MONT","MONTÉ","MONT",1),
        "REVENIR" : ("REVIENDR",2,"REVEN","REVENU","REV",4),
        "SORTIR" : ("SORTIR",2,"SORT","SORTI","SORT",2),
        "VENIR" : ("VIENDR",2,"VEN","VENU","V",4),
        "ALLER" : ("IR",2,"ALL","ALLÉ","ALL",1),
        "NAITRE" : ("NAÎTR",2,"NAISS","NÉ","NAQU",2),
        "DESCENDRE" : ("DESCENDR",2,"DESCEND","DESCENDU","DESCEND",2),
        "ENTRER" : ("ENTRER",2,"ENTR","ENTRÉ","ENTR",1),
        "RENTRER" : ("RENTRER",2,"RENTR","RENTRÉ","RENTR",1),
        "TOMBER" : ("TOMBER",2,"TOMB","TOMBÉ","TOMB",1),
        "RETOURNER" : ("RETOURNER",2,"RETOURN","RETOURNÉ","RETOURN",1),
        "ARRIVER" : ("ARRIVER",2,"ARRIV","ARRIVÉ","ARRIV",1),
        "MOURIR" : ("MOURIR",2,"MOUR","MORT","MOUR",3),
        "PARTIR" : ("PARTIR",2,"PART","PARTI","P",2),
        #new set of verbs
        "SOUVENIR" : ("SOUVIENDR",1,"SOUVEN","SOUVENU","SOUV",4),
        "OUVRIR" : ("OUVRIR",1,"OUVR","OUVERT","OUVR",2),
        "DORMIR" : ("DORMIR",1,"DORM","DORMI","DORM",2),
        "TENIR" : ("TIENDR",1,"TEN","TENU","T",4),
        "RESOUDRE" : ("RÉSOUDR",1,"RÉSOLV","RÉSOLU","RÉSOL",3),
        "CONNAITRE" : ("CONNAÎTR",1,"CONNAISS","CONNU","CONN",3),
        "ASSEOIR" : ("ASSIÉR",1,"ASSEY","ASSIS","ASS",2),
        "JOINDRE" : ("JOINDR",1,"JOIGN","JOINT","JOIGN",2),
        "SAVOIR" : ("SAUR",1,"SACH","SU","S",3),
        "AVOIR" : ("AUR",1,"AY","EU","E",3),
        "DEVOIR" : ("DEVR",1,"DEV","DÛ","D",3),
        "RECEVOIR" : ("RECEVR",1,"RECEV","REÇU","REÇ",3),
        "POUVOIR" : ("POURR",1,"POUV","POUVU","P",3,),
        "COURIR" : ("COURR",1,"COUR","COURU","COUR",3),
        "ETRE" : ("SER",1,"ÉT","ÉTÉ","F",3),
        "FAIRE" : ("FER",1,"FAIS","FAIT","F",2),
        "VOULOIR" : ("VIENDR",1,"VOUL","VOULU","VOUL",3),
        "ACHETER" : ("ACHÈTER",1,"ACHET","ACHETÉ","ACHET",1),
        "LEVER" : ("LÈVER",1,"LEV","LEVÉ","LEV",1),
        "ENVOYER" : ("ENVERR",1,"ENVOY","ENVOYÉ","ENVOY",1),
        "VOIR" : ("VERR",1,"VOY","VU","V",2),
        "METTRE" : ("METTR",1,"METT","MIS","M",2),
        "PERMETTRE" : ("PERMETTR",1,"PERMETT","PERMIS","PERM",2),
        "REMETTRE" : ("REMETTR",1,"REMETT","REMIS","REM",2),
        "PRENDRE" : ("PRENDR",1,"PREN","PRIS","PR",2),
        "BOIRE" : ("BOIR",1,"BUV","BU","B",3),
        "CROIRE" : ("CROIR",1,"CROY","CRU","CR",3),
        "LIRE" : ("LIR",1,"LIS","LU","L",3),
	"DIRE" : ("DIR",1,"DIS","DIT","D",2),
        "RIRE" : ("RIR",1,"RI","RI","R",2),
        "ECRIRE" : ("ÉCRIR",1,"ÉCRIV","ÉCRIT","ÉCRIV",2),
        "VAINCRE" : ("VAINCR",1,"VAINQU","VAINCU","VAINQU",2)
        }

end1 = ("AI","AS","A","A","ONS","EZ","ONT","ONT")
end2 = ("AIS","AIS","AIT","AIT","IONS","IEZ","AIENT","AIENT")
end2a = ("(E)","(E)","","E","(E)S","(E)(S)","S","ES")
end3 = "ANT"
end4 = ("AI","AS","A","A","ÂMES","ÂTES","ÈRENT","ÈRENT")
end5 = ("IS","IS","IT","IT","ÎMES","ÎTES","IRENT","IRENT")
end6 = ("US","US","UT","UT","ÛMES","ÛTES","URENT","URENT")
end7 = ("INS","INS","INT","INT","ÎNMES","ÎNTES","INRENT","INRENT") #VENIR

wordList1 = ("JE ","TU ","IL ","ELLE ","NOUS ","VOUS ","ILS ","ELLES ")
wordList2 = ("J'","TU ","IL ","ELLE ","NOUS ","VOUS ","ILS ","ELLES ")
wordList3 = ("JE ME ","TU TE ","IL SE ","ELLE SE ","NOUS NOUS ","VOUS VOUS ","ILS SE ","ELLES SE ")
wordList4 = ("JE M'","TU T'","IL S'","ELLE S'","NOUS NOUS ","VOUS VOUS ","ILS S'","ELLES S'")
wordList5 = ("JE ME ","TU T'","IL S'","ELLE S'","NOUS NOUS ","VOUS VOUS ","ILS SE ","ELLES SE ")

avoir = ("AI","AS","A","A","AVONS","AVEZ","ONT","ONT")
etre = ("SUIS","ES","EST","EST","SOMMES","ÊTES","SONT","SONT")
vowels = ("A","E","I","O","U","É","H")

def vowelCheck(word):
    global SE
    global vowels
    if SE == "TRUE":
        if word[0] in vowels:
            return wordList4
        else:
            return wordList3
    else:
        if word[0] in vowels:
            return wordList2
        else:
            return wordList1

print "MULTIPLE VERBS MUST BE SEPARATED BY ONLY A COMMA, NOT BY SPACES!"
words = raw_input("ENTER A WORD / WORDS TO BE CONJUGATED TO FRENCH: ")
print ""
words = words.split(",")

for word in words:
    word = word.upper()
    wordLen = len(word)
    if word[0 : 3] == "SE ": 
        word = word[3 : wordLen]
        wordLen = wordLen - 3
        SE = "TRUE"
    elif word[0 : 2] == "S'":
        word = word[2 : wordLen]
        wordLen = wordLen - 2
        SE = "TRUE"
    else:
        wordList = wordList1
        SE = "FALSE"
        
    verb = word[(wordLen - 2) : wordLen]
    print "------------------------------------------------------------"

    if word not in dict1:
        print ""
        print "FUTUR SIMPLE:"
        print ""
        if verb != "RE":
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + word + end1[i]
        else:
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + word[0 : (wordLen - 1)] + end1[i]
        print ""

        print ""
        print "FUTUR ANTÉRIEUR:"
        print ""
        if verb == "ER":
            infinitive = word[0 : wordLen - 2] + "É"
        if verb == "IR":
            infinitive = word[0 : wordLen - 1]
        if verb == "RE":
            infinitive = word[0 : wordLen - 2] + "U"
        for i in xrange(8):
            if SE == "FALSE":
                print wordList2[i] + dict1["AVOIR"][0] + end1[i] + " " + infinitive
            else:
                print wordList3[i] + dict1["ETRE"][0] + end1[i] + " " + infinitive + end2a[i]           
        print ""

        print ""
        print "CONDITIONNEL PRÉSENT:"
        print ""
        if verb != "RE":
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + word + end2[i]
        else:
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + word[0 : (wordLen - 1)] + end2[i]
        print ""

        print ""
        print "CONDITIONNEL PASSÉ:"
        print ""
        if verb == "ER":
            infinitive = word[0 : wordLen - 2] + "É"
        if verb == "IR":
            infinitive = word[0 : wordLen - 1]
        if verb == "RE":
            infinitive = word[0 : wordLen - 2] + "U"
        for i in xrange(8):
            if SE == "TRUE":
                print wordList3[i] + dict1["ETRE"][0] + end2[i] + " " + infinitive + end2a[i]
            else:
                print wordList2[i] + dict1["AVOIR"][0] + end2[i] + " " + infinitive
        print ""

        print ""
        print "PARTICIPE PRÉSENT:"
        print ""
        if verb != "IR":
            if SE == "TRUE":
                if word[0] in vowels:
                    print "S'" + word[0 : wordLen - 2] + end3
                else:
                    print "SE " + word[0 : wordLen - 2] + end3                    
            else:
                print word[0 : wordLen - 2] + end3
        else:
            if SE == "TRUE":
                if word[0] in vowels:
                    print "S'" + word[0 : wordLen - 2] + "ISS" + end3
                else:
                    print "SE " + word[0 : wordLen - 2] + "ISS" + end3                    
            else:                
                print word[0 : wordLen - 2] + "ISS" + end3
        print ""

        print ""
        print "GÉRONDIF:"
        print ""
        if verb != "IR":
            if SE == "TRUE":
                if word[0] in vowels:
                    print "EN " + "S'" + word[0 : wordLen - 2] + end3
                else:
                    print "EN " + "SE " + word[0 : wordLen - 2] + end3                    
            else:
                print "EN " + word[0 : wordLen - 2] + end3
        else:
            if SE == "TRUE":
                if word[0] in vowels:
                    print "EN " + "S'" + word[0 : wordLen - 2] + "ISS" + end3
                else:
                    print "EN " + "SE " + word[0 : wordLen - 2] + "ISS" + end3                    
            else:                
                print "EN " + word[0 : wordLen - 2] + "ISS" + end3
        print ""

        print ""
        print "PASSÉ COMPOSÉ"
        print ""
        if verb == "ER":
            infinitive = word[0 : wordLen - 2] + "É"
        if verb == "IR":
            infinitive = word[0 : wordLen - 1]
        if verb == "RE":
            infinitive = word[0 : wordLen - 2] + "U"
        for i in xrange(8):
            if SE == "TRUE":
                print wordList5[i] + etre[i] + " " + infinitive + end2a[i]
            else:
                print wordList2[i] + avoir[i] + " " + infinitive
        print ""        

        print ""
        print "PLUS QUE PARFAIT"
        print ""
        if verb == "ER":
            infinitive = word[0 : wordLen - 2] + "É"
        if verb == "IR":
            infinitive = word[0 : wordLen - 1]
        if verb == "RE":
            infinitive = word[0 : wordLen - 2] + "U"
        for i in xrange(8):
            if SE == "TRUE":
                print wordList4[i] + "ÉT" + end2[i] + " " + infinitive + end2a[i]
            else:
                print wordList2[i] + "AV" + end2[i] + " " + infinitive
        print ""

        print ""
        print "PASSÉ SIMPLE"
        print ""        
        for i in xrange(8):
            wordList = vowelCheck(word)
            if verb == "ER":
                print wordList[i] + word[0 : wordLen - 2] + end4[i]
            if verb == "IR" or verb == "RE":
                print wordList[i] + word[0 : wordLen - 2] + end5[i]
        print ""

        print ""
        print "IMPARFAIT"
        print ""
        for i in xrange(8):
            wordList = vowelCheck(word)
            if verb == "ER" or verb == "RE":
                print wordList[i] + word[0 : wordLen - 2] + end2[i]
            else:
                print wordList[i] + word[0 : wordLen - 2] + "ISS" + end2[i]
        print ""
        
    else:
        print ""
        print "FUTUR SIMPLE:"
        print ""
        for i in xrange(8):
            wordList = vowelCheck(dict1[word][0])
            print wordList[i] + dict1[word][0] + end1[i]
        print ""

        print ""
        print "FUTUR ANTÉRIEUR:"
        print ""
        if dict1[word][1] == 1:
            for i in xrange(8):
                if SE == "TRUE":
                    print wordList3[i] + dict1["ETRE"][0] + end1[i] + " " + dict1[word][3] + end2a[i]
                else:
                    print wordList2[i] + dict1["AVOIR"][0] + end1[i] + " " + dict1[word][3]
        else:
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + dict1["ETRE"][0] + end1[i] + " " + dict1[word][3] + end2a[i]
        print ""

        print ""
        print "CONDITIONNEL PRÉSENT:"
        print ""
        for i in xrange(8):
            wordList = vowelCheck(dict1[word][0])
            print wordList[i] + dict1[word][0] + end2[i]
        print ""

        print ""
        print "CONDITIONNEL PASSÉ:"
        print ""
        if dict1[word][1] == 1:
            for i in xrange(8):
                if SE == "TRUE":
                    print wordList3[i] + dict1["ETRE"][0] + end2[i] + " " + dict1[word][3] + end2a[i]
                else:
                    print wordList2[i] + dict1["AVOIR"][0] + end2[i] + " " + dict1[word][3]
        else:
            for i in xrange(8):
                wordList = vowelCheck(word)
                print wordList[i] + dict1["ETRE"][0] + end2[i] + " " + dict1[word][3] + end2a[i]
        print ""

        print ""
        print "PARTICIPE PRÉSENT:"
        print ""
        if SE == "TRUE":
            if word[0] in vowels:
                print "S'" + dict1[word][2] + end3
            else:
                print "SE " + dict1[word][2] + end3
        else:
            print dict1[word][2] + end3
        print ""

        print ""
        print "GÉRONDIF:"
        print ""
        if SE == "TRUE":
            if word[0] in vowels:
                print "EN " + "S'" + dict1[word][2] + end3
            else:
                print "EN " + "SE " + dict1[word][2] + end3
        else:
            print "EN " + dict1[word][2] + end3
        print ""

        print ""
        print "PASSÉ COMPOSÉ"
        print ""
        for i in xrange(8):
            if dict1[word][1] == 1:
                if SE == "TRUE":
                    print wordList5[i] + etre[i] + " " + dict1[word][3] + end2a[i]
                else:
                    print wordList2[i] + avoir[i] + " " + dict1[word][3]
            else:
                wordList = vowelCheck(word)
                print wordList[i] + etre[i] + " " + dict1[word][3] + end2a[i]
        print ""        

        print ""
        print "PLUS QUE PARFAIT"
        print ""
        for i in xrange(8):
            if dict1[word][1] == 1:
                if SE == "TRUE":
                    print wordList4[i] + "ÉT" + end2[i] + " " + dict1[word][3] + end2a[i]
                else:
                    print wordList2[i] + "AV" + end2[i] + " " + dict1[word][3]
            else:
                wordList = vowelCheck("ÉT")
                print wordList[i] + "ÉT" + end2[i] + " " + dict1[word][3] + end2a[i]
        print ""

        print ""
        print "PASSÉ SIMPLE"
        print ""        
        for i in xrange(8):
            wordList = vowelCheck(dict1[word][4])
            if dict1[word][5] == 1:
                print wordList[i] + dict1[word][4] + end4[i]
            if dict1[word][5] == 2:
                print wordList[i] + dict1[word][4] + end5[i]
            if dict1[word][5] == 3:
                print wordList[i] + dict1[word][4] + end6[i]
            if dict1[word][5] == 4:
                print wordList[i] + dict1[word][4] + end7[i]
        print ""

        print ""
        print "IMPARFAIT"
        print ""
        for i in xrange(8):
            wordList = vowelCheck(word)
            if word == "AVOIR":
                print wordList[i] + "AV" + end2[i]
            elif word == "SAVOIR":
                print wordList[i] + "SAV" + end2[i]
            else:
                print wordList[i] + dict1[word][2] + end2[i]
        print ""
