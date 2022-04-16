sample_tuple = (1,2,3)
print (sample_tuple)
# Tuples are immutables, we cannot change/modify a tuple or its contents
print(sample_tuple.count(1))
print(sample_tuple.index(3))
print(len(sample_tuple))

x = tuple([4,5,6]) # use tuple() function to convert iterable to tuple
print(x)