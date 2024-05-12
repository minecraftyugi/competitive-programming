def is_valid(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 5
        n //= 10

    return total == original

total = 0
for i in range(2, 1_000_000):
    if is_valid(i):
        total += i

print(total)
