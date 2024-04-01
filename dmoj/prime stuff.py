import math
a = input()
b = input()
ans = b - a
values = [1] * 20000000

def sieve(number):
    root = int(math.sqrt(number))
    primes = [1] * 100000
    primeNumbers = [2,3,5]
    spaces = [7,11,13,17,19,23,29,31]

    for i in xrange(0, root, 30):
        for j in spaces:
            num = i + j
            if num > root:
                break

            if primes[num]:
                primeNumbers.append(num)
                for k in xrange(num*num, root, num):
                    primes[k] = 0

    return primeNumbers

primes = sieve(b)

for prime in primes:
    start = a / prime
    start *= prime
    start -= a

    for i in xrange(start, b - a, prime):
        if i < 0:
            continue
        if values[i]:
            ans -= 1
            values[i] = 0

print ans
