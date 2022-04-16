nums = [30,34,57,78,5,89,19]
large_num = nums[0]
for item in nums:
    if item > large_num:
        large_num = item
print("largest number in list is ", large_num)
