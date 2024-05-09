N = 100

def get_sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i * i

    return total

def get_square_of_sum(n):
    return sum(range(1, n+1)) ** 2

print(get_square_of_sum(N) - get_sum_of_squares(N))
