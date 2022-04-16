try:
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print ("you didn't enter a valid age")
    print(ex)
    print (type(ex))
else:
    print ("No exception")
print("Execution continues")