n = input()
print n / 2
if n%2 == 0:
    a = "2 " * (n/2)
    print  a[:-1]
else:
    a = "2 " * (n/2 - 1)
    print a + "3"
