MAX_N = 1_000_000
NEEDED_PRIME = 10_001

primes = [1] * MAX_N
primes[0] = 0
primes[1] = 0

for i in range(3, int(MAX_N ** 0.5) + 1, 2):
    if primes[i] == 1:
        for j in range(i * i, MAX_N, i):
            primes[j] = 0

prime_count = 1
prime = 0
for i in range(3, MAX_N, 2):
    if prime_count == NEEDED_PRIME:
        print(prime)
        break

    if primes[i] == 1:
        prime_count += 1
        prime = i


    
