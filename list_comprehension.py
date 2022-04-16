cart = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]
#Task1: To create a list of prices for all items in cart
#Task2: to create a list of cart items which are > 10


#Older way to use map and lambda function
#x= list(map (lambda item: item[1], cart))
#New way using List comprehension
# [expression for item in items]
x = [item[1] for item in cart]
print (x)

#Older way to use Filter and lambda function
#x = list(filter(lambda item: item[1] >= 10, cart))
#New way using List comprehension
# [expression for items in item if conition]
y = [item for item in cart if item[1] >= 10]
print(y)
