weight = raw_input("Enter a number")
height = raw_input("Enter a number")
weight = float(weight)
height = float(height)
bmi = float(weight / (height * height))

if bmi > 25:
    print "Overweight"
if bmi < 25 or bmi == 25:
    if bmi == 18.5 or bmi > 18.5:
        print "Normal weight"
    else:
        print "Underweight"
