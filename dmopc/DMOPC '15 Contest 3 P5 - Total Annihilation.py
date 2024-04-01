n, m = map(int, raw_input().split())
total = map(int, raw_input().split()) + [-i for i in map(int, raw_input().split())]
half = (m + n) / 2
cache = {}

def total_sum(count, total, length, num_list):
    if count == length:
        cache[total] = cache.get(total, 0) + 1
        return

    total_sum(count + 1, total + num_list[count], length, num_list)
    total_sum(count + 1, total, length, num_list)

def total_sum2(count, total, length, num_list):
    ans = 0
    if count == length:
        return cache.get(-total, 0)

    ans += total_sum2(count + 1, total + num_list[count], length, num_list)
    ans += total_sum2(count + 1, total, length, num_list)
    return ans

total_sum(0, 0, half, total[:half])
ans = total_sum2(0, 0, n + m - half, total[half:])
print ans - 1 #subtract the empty subset case
