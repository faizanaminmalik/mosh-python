list1 = [1,2,3]
list2 = [10,20,30]

print(list(zip(list1, list2))) # zip will create tuples out of same-index elements from both lists (1, 10)
print(list(zip("abc", list1, list2))) # We can add any custom arg to get tuples combined ('a', 1, 10)