n = int(input())
for i in range(n):
    line = input()
    math = False
    cs = False
    for ch in line:
        if ch == "M":
            math = True
        if ch == "C":
            cs = True

    if math and cs:
        print("NEGATIVE MARKS")
    elif math or cs:
        print("FAIL")
    else:
        print("PASS")
