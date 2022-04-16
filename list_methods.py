nums = [5,2,4,7,9,60,55]
nums.append(33)
print (nums)

nums.insert(0,11)
print (nums)

nums.remove(55) # removes first occurence of 55, to remove all 55 use loop
print (nums)

nums.pop() # removes last number in list
print (nums)

print (nums.index(2)) # returns index of number specified, if number not in list, throws error

print (50 in nums) # Will print true or false if number is present/absent in list

nums.insert(0,11) # inserted another 11 in list, so we have 11 two times in list
print (nums.count(11)) # check how many times 11 is in list

nums.sort() # sorts list
print (nums)

nums.sort(reverse=True) # Sorts in descending order
print(nums)

nums.reverse() # reverses list
print(nums)

new_sotred_list = sorted(nums) # This function returns a new sorted list
new_reverse_sotred_list = sorted(nums, reverse=True)
copy_nums = nums.copy() # will have copy of all items in list, but any changes on old list will not be reflected here.
del nums[0:3] # removes items from index 0-2 from list
nums.clear()
print (nums)