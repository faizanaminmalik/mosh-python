# Use array if dealing with large set of numbers
# Arrays have more performance than lists

from array import array
my_array = array("i", [1,2,3]) # i is a typecode for integer. see python doc for typecodes
print(my_array)
for items in my_array:
    print(items)

my_array.append(4)
my_array.append(99)
my_array.pop()
my_array.remove(1)
print(my_array)