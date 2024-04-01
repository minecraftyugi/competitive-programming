n = input("Number in front of t: ")*1.0
m = input("Other number: ")*1.0
b = input("Upper bound: ")*1.0
a = input("Lower bound: ")*1.0
intermediate = m / n
print "Displacement =", n/2 * b**2 - m*b - (n/2 * a**2 - m*a)
print "Distance =", -1 * (n/2 * intermediate**2 - m*intermediate - (n/2 * a**2 - m*a)) \
      + n/2 * b**2 - m*b - (n/2 * intermediate**2 - m*intermediate)
