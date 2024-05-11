import math

N = 100
num = math.factorial(N)
total = 0
while num > 0:
    total += num % 10
    num //= 10

print(total)
