def get_prime_factorization(n):
    d = {}
    while n > 1:
        found_prime = False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                d[i] = d.get(i, 0) + 1
                n //= i
                found_prime = True
                break

        if not found_prime:
            d[n] = 1
            n = 1

    return d

def get_total_divisors(prime_factors):
    divisors = 1
    for count in prime_factors.values():
        divisors *= count + 1

    return divisors

DIVISOR_COUNT_MIN = 500
total = 1
i = 1
while get_total_divisors(get_prime_factorization(total)) <= DIVISOR_COUNT_MIN:
    i += 1
    total += i

print(total)
