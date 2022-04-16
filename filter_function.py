cart = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

#Task: to create a list of cart items which are > 10

x = list(filter(lambda item: item[1] >= 10, cart)) # Filter needs item and condition and returs filter object which is iteratable
print(x)