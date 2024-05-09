N = 1000

def is_pythagorean_triplet(a, b):
    num = a * a + b * b
    return int(num ** 0.5) * int(num ** 0.5) == num

for a in range(1, N):
    for b in range(1, N):
        if is_pythagorean_triplet(a, b):
            c = int((a * a + b * b) ** 0.5)
            if a + b + c == N:
                print(a * b * c)
