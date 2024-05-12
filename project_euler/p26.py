def get_cycle_length(n):
    numerator = 1
    numerator_positions = {}
    curr_pos = 0
    while True:
        while numerator < n:
            numerator *= 10
            curr_pos += 1

        decimal = numerator // n
        numerator = numerator % n
        if numerator % n == 0:
            return 0
        if numerator in numerator_positions:
            return curr_pos - numerator_positions[numerator]

        numerator_positions[numerator] = curr_pos
        numerator = numerator % n

max_cycle_length = 0
max_cycle_num = 0
for i in range(2, 1000):
    cycle_length = get_cycle_length(i)
    if cycle_length > max_cycle_length:
        max_cycle_length = cycle_length
        max_cycle_num = i

print(max_cycle_num)
        
