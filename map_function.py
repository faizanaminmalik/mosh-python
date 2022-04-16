cart = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

#Task: To create a list of prices for all items in cart
# Suppose we want to retreive only prices from cart
#we have a choice to iterate over the cart list and get prices, but we will use map and lanmda function

x= list(map (lambda item: item[1], cart)) # map function supports lambda, we call list fuction over map to save values in list.
print(x)