num = int(raw_input())

for i in xrange(num):
    number = int(raw_input())
    ans = 0
    for j in xrange(number / 2, 0, -1):
        if number % j == 0:
            ans += j
    if ans == number:
        print number, "is a perfect number."
    elif ans < number:
        print number, "is a deficient number."
    else:
        print number, "is an abundant number."
