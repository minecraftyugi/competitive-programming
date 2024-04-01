n = input()
nums = map(int, raw_input().split())

print " ".join(map(str, nums))
for i in range(n):
    for j in range(n-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print " ".join(map(str, nums))
