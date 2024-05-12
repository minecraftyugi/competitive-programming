BOUND = 501

total = 1
for i in range(1, BOUND):
    n = 2*i+1
    total += n**2
    total += n**2 - n + 1
    total += n**2 - 2*n + 2
    total += n**2 - 3*n + 3

print(total)
