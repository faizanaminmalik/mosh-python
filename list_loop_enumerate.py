my_list = ["a", "b", "c", "d"]

for item in my_list:
    print (item)

# If we need index to be printed also, we can use enumerate. it returns a tuple (index, value) eg (0, 'a')
for item in enumerate(my_list):
    print(item)

# To use enumerate to print index and item cleanly
for index, item in enumerate(my_list):
    print(index, item)
