num = int(raw_input())

def switch(number):
    number = list(number)
    for i in xrange(len(number)):
        if number[i] == "I":
            number[i] = 1
        elif number[i] == "V":
            number[i] = 5
        elif number[i] == "X":
            number[i] = 10
        elif number[i] == "L":
            number[i] = 50
        elif number[i] == "C":
            number[i] = 100
        elif number[i] == "D":
            number[i] = 500
        else:
            number[i] = 1000
            
    return [0] + number

def translate(number):
    ans = 0
    for i in xrange(len(number)-1, 0, -1):
        ans += number[i]
        if number[i] == 1000 or number[i] == 500:
            if number[i-1] == 100:
                ans -= 200
        if number[i] == 100 or number[i] == 50:
            if number[i-1] == 10:
                ans -= 20
        if number[i] == 10 or number[i] == 5:
            if number[i-1] == 1:
                ans -= 2

    return ans

for i in xrange(num):
    thing = raw_input()
    num1, num2 = map(switch, thing[:-1].split("+"))
    total = translate(num1) + translate(num2)
    if total > 1000:
        print thing + "CONCORDIA CUM VERITATE"
    else:
        letters = []
        while 1:
            if total == 0:
                print thing + "".join(letters)
                break
            if len(str(total)) == 4:
                letters.append("M")
                total -= 1000
            elif len(str(total)) == 3:
                if total >= 900:
                    letters.append("CM")
                    total -= 900
                elif total >= 500:
                    letters.append("D"+"C"*(int(`total`[0])-5))
                    total -= int(`total`[0]*100)
                elif total >= 400:
                    letters.append("CD")
                    total -= 400
                else:
                    letters.append("C"*int(`total`[0]))
                    total -= int(`total`[0])*100
            elif len(str(total)) == 2:
                if total >= 90:
                    letters.append("XC")
                    total -= 90
                elif total >= 50:
                    letters.append("L"+"X"*(int(`total`[0])-5))
                    total -= int(`total`[0])*10
                elif total >= 40:
                    letters.append("XL")
                    total -= 40
                else:
                    letters.append("X"*int(`total`[0]))
                    total -= int(`total`[0])*10
            else:
                if total >= 9:
                    letters.append("IX")
                    total -= 9
                elif total >= 5:
                    letters.append("V"+"I"*(int(`total`[0])-5))
                    total -= int(`total`[0])*1
                elif total >= 4:
                    letters.append("IV")
                    total -= 4
                else:
                    letters.append("I"*int(`total`[0]))
                    total -= int(`total`[0])*1
