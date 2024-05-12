a = 1
b = 1
count = 1
while len(str(a)) < 1000:
    c = a + b
    a = b
    b = c
    count += 1

print(count)
