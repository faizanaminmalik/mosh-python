cart = [
    ('Product10', 10),
    ('Product20', 9),
    ('Product30', 12)
]

def sort_item(item):
    return item[1] # We just return price to get this sorted on

cart.sort(key = sort_item) # we need to specify arg as function name as a keyword arg
print(cart)

#Better way to sort using lambda function
cart2 = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

#lambda is a short inline fuction that is used once, no need to define separate fuction for that.
cart2.sort(key=lambda item: item[1]) # lambda function needs parameter: expression
print(cart2)