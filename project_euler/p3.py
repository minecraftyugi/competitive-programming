PRIME = 600851475143

has_factors = True
largest = 0
while has_factors:
    has_factors = False
    for i in range(2, int(PRIME ** 0.5) + 1):
        if PRIME % i == 0:
            largest = max(largest, i)
            PRIME //= i
            has_factors = True
            break

largest = max(largest, PRIME)
print(largest)

    
    
