num = int(raw_input())
a = 1
b = 1
for i in range(num):
    strA = []
    strB = []
    if a % 7 == 0:
        strA.append("Fizz")
    if a % 13 == 0:
        strA.append("Fuzz")
    if b % 7 == 0:
        strB.append("Fizz")
    if b % 13 == 0:
        strB.append("Fuzz")
    if strA == []:
        strA.append(str(a))
    if strB == []:
        strB.append(str(b))
    print " ".join(strA) + " " + " ".join(strB)
    a += 1
    b += 2
