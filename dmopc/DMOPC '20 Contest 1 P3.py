n = int(input())
nums = list(map(int, input().split()))

to_add = [0]*n
curr_max = nums[-1]
curr_max_idx = n-1
for i in range(n-1, -1, -1):
    if nums[i] < curr_max:
        to_add[i] = curr_max - nums[i]
    else:
        curr_max = nums[i]
        curr_max_idx = i

curr_max = nums[0]
for i in range(curr_max_idx):
    if nums[i] < curr_max:
        to_add[i] = curr_max - nums[i]
    else:
        to_add[i] = 0
        curr_max = nums[i]

print(sum(to_add))
