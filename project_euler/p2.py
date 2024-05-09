MAX_N = 4_000_000

total = 0
a = 1
b = 2
while a <= MAX_N:
    if b <= MAX_N and b % 2 == 0:
        total += b

    c = a + b
    a = b
    b = c

print(total)
