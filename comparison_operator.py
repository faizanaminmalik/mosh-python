name = input("Enter Name: ")
name_length = len(name)

if name_length < 3:
    print ("Name should be atlease 3 characters long")
elif name_length > 10:
    print ("name should be less than 10 characters long")
else:
    print (f'Name {name} is a valid name of {name_length} characters.')