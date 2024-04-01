a, b = map(int, raw_input().split())
num1 = 5 * a
num2 = 5 * (b+1)
if num1 == 0:
    print num2 - 1
else:
    print num2 - num1

#1234 6789
#5^13 > 10^9
