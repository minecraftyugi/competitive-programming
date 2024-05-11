COUNTS = {}
COUNTS[1] = 1
UPPER_BOUND = 1_000_000

def collatz(n):
    if n in COUNTS:
        return COUNTS[n]

    if n % 2 == 0:
        count = 1 + collatz(n // 2)
        COUNTS[n] = count
        return count

    count = 1 + collatz(3 * n + 1)
    COUNTS[n] = count
    return count

max_chain = 0
max_number = 0
for i in range(1, UPPER_BOUND):
    count = collatz(i)
    if count > max_chain:
        max_chain = count
        max_number = i
        print(i, max_chain)

print(max_number)

