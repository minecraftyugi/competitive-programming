N = 2_000_000

primes = [1] * (N+1)
primes[0] = 0
primes[1] = 0
for i in range(3, int(N ** 0.5) + 1, 2):
    if primes[i] == 1:
        for j in range(i * i, N + 1, i):
            primes[j] = 0

total = 2
for i in range(3, N+1, 2):
    if primes[i] == 1:
        total += i
        
print(total)
