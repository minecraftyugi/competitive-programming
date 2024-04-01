def max_subset_sum(lst):
    curr_max = 0
    curr_sum = 0
    for i in range(len(lst)):
        num = lst[i]
        curr_sum = max(curr_sum + num, num)
        curr_max = max(curr_max, curr_sum)

    return curr_max

print max_subset_sum([2,-5,8,-6,10])
print max_subset_sum([4,-5,6,-7])
print max_subset_sum([4,5,6,7])
