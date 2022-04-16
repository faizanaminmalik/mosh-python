#Sets contain unique elements
# Sets are unordered collection, items in set r not in sequence and we cannot access them using an idex
# To remove duplicates from alist, we can convert to set
numbers = [1,2,2,3,3,4,5,5,6,6]
print(list(set(numbers)))
my_set = {1,2,3}
my_set.add(4)
my_set.remove(2)
print(my_set)

my_set_2 = {1,3,5}
print ("*****************************")
print(my_set | my_set_2) # Union of 2 sets
print(my_set & my_set_2) # Intersection of 2 sets
print(my_set - my_set_2) # Difference between 2 sets
print(my_set ^ my_set_2) # Symmetric difference, either in 1st or 2nd set but not both

print ("******************************")
if 1 in my_set:
    print("Yes")