def validate(i):
    count = 0
    number = str(i)[::-1]
    for j in xrange(1, len(number), 2):
        count += sum(map(int, list(str(int(number[j]) * 2))))

    for j in xrange(0, len(number), 2):
        count += int(number[j])
                     
    if count % 10 == 0:
        return True
    else:
        return False

for i in xrange(5):
    numbers = map(int, raw_input().strip().split())
    ans = ""
    for number in numbers:
        for j in xrange(10):
            num = number * 10
            num += j
            check = validate(num)
            if check:
                ans += str(j)
                break

    print ans
