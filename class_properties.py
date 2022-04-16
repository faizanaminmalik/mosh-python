# Task: we have a product class, but price cannot be negative
class Product:
    def __init__(self, price):
        self.setPrice(price)

    def setPrice(self, price):
        if price < 0:
            raise ValueError("price cannot be less than 0")
        self.__price = price

    def getPrice(self):
        return self.__price
    # PYTHONIC WAY OF DOING THIS USING PROPERTIES
    # Propert is an object which sits in front of an attribute and allows us to set or get values of an attribute
    # We need to define a class attribute with an ideal name like price
    # Property functions:   --> property(fget, fset, fdel, doc)
    price = property(getPrice, setPrice)


product = Product(10)
print(product.price) # price can be accessed as normal attribute but under the hood it used functions to get or set
product.price = 25
print(product.price)
#product.price = -25 # Will throw exception as its negative value


#######################################################################################
# 2nd implementation
class Product2:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    #If we remove setter, out object attribute will be read-only
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price cannot be less than 0")
        self.__price = price

product2 = Product2(99)
print(product2.price) # price can be accessed as normal attribute but under the hood it used functions to get or set
product2.price = 111
print(product2.price)
#product.price = -25 # Will throw exception as its negative value

