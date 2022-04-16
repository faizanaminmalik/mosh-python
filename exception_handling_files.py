try:
    file = open("for_loop.py") # file is opened and we need to close this after we're done even if theres exception
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print ("you didn't enter a valid age")
    print(ex)
    print (type(ex))
else:
    print ("No exception")
#finally block will be executed everytime with or without exception
#Finally block is perfect place to close files, AWS connections, network connections etc
finally:
    file.close()
print("Execution continues")