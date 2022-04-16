sample_tuple = (1,2,3)
x,y,z = sample_tuple
print (x)

sample_list = [7,8,9]
a,b,c = sample_list
print(b)

another_list = [1,2,3,55,66,77,88,99,100,122]
first, second, *other = another_list # If we're interested in only 2 elements, we cr8 sep vars for then and evrythng else in a list other
print(first)
print(second)
print(other)

first, *other, last = another_list # When we need only 1st and last item from args rest evrything will be packed in list other
print(first)
print(last)
print(other)