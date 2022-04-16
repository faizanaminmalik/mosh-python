def multiply(*numbers): #*numbers is a collection of all arguments in the form of tuple (1,2,3)
    total =1
    for item in numbers:
        total *= item
    return total
print(multiply(1,2,3)) # We can pass any number of arguments to a function