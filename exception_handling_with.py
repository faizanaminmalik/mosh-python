try:
    with open("for_loop.py") as file, open("dictionary.py") as file2:
        print ("File opened")
        # Using with, it ensures object is closed after opened
        # Methods starting with __ are called Magic methods
        # Any object with methods __enter , __exit supports context management protocol
        # On these objects python will automatically call __exit() method to release external resources
        # Thats the reason we dont need finally clause
        #file.__enter__()
        #file.__exit__()
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print ("you didn't enter a valid age")
    print(ex)
    print (type(ex))
else:
    print ("No exception")
print("Execution continues")