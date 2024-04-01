numerator = int(raw_input())
denominator = int(raw_input())
answer = numerator / denominator
answer = str(answer)

if numerator % denominator == 0:
    print answer
else:
    remainder = numerator % denominator
    for i in xrange(remainder,0,-1):
        if denominator % i == 0 and remainder % i == 0:
            denominator = denominator / i
            remainder = remainder / i
            break
    denominator = str(denominator)
    remainder = str(remainder)
    if answer == "0":
        print remainder + "/" + denominator
    else:
        print answer + " " + remainder + "/" + denominator
