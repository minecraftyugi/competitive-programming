prime = [0, 1] * 500_000
prime[1] = 0
prime[2] = 1
for i in range(3, int(1_000_000**0.5) + 1, 2):
    if prime[i] == 1:
        for j in range(i*i, 1_000_000, i):
            prime[j] = 0

max_consecutive_primes = 0
max_a = 0
max_b = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        consecutive_primes = 0
        not_prime = False
        while not not_prime:
            num = consecutive_primes ** 2 + a * consecutive_primes + b
            if num < 2 or prime[num] != 1:
                not_prime = True
            else:
                consecutive_primes += 1

        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            max_a = a
            max_b = b

print(max_a * max_b)
