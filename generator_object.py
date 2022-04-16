# Generator object are used when we need to deal with huge data sets
# Generator objects dont store all item data in memeory rather generate them at each iteration
# no len function available in generator, we dont know anything abt size of generator object
from sys import getsizeof
gen_values = (x * 2 for x in range(10))
print(gen_values)  # This is a generator object
for x in gen_values:
    print(x)
print("gen 10:", getsizeof(gen_values)) # returns size of gen_values as 112 bytes
gen_values = (x * 2 for x in range(1000)) # will make gen_values bigger to 1000
print("gen 1000:", getsizeof(gen_values)) # returns size of gen_values still as 112 bytes

# compare with size of a list
list_values = [x *2 for x in range(10)] # take a list of range 10
print("List 10:", getsizeof(list_values)) # returned size of 184 bytes
list_values = [x *2 for x in range(1000)] # take a list of range 1000
print("List 1000:", getsizeof(list_values)) # returned size of 8856 bytes