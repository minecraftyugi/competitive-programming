num1 = int(raw_input())
num2 = int(raw_input())
num3 = num2 - num1

if num3 >=1 and num3 <= 20:
    print "You are speeding and your fine is $100."
elif num3 >= 21 and num3 <= 30:
    print "You are speeding and your fine is $270."
elif num3 >= 31:
    print "You are speeding and your fine is $500."
else:
    print "Congratulations, you are within the speed limit!"
