a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if a == b == c and a + b + c == 180:
    print "Equilateral"
elif (a == b or b == c or a == c) and a + b + c == 180:
    print "Isosceles"
elif a != b and a != c and b != c and a + b + c == 180:
    print "Scalene"
else:
    print "Error"
