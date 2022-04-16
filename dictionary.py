customer = {
    "name": "John Smith",
    "age": 20,
    "isVerified": True
}


print (customer)
print (customer["name"])
#print (customer["Name"]) # if specified key not present, it will throw KeyError

#Better way to avoid keyvalue Error in program is to use get method

print (customer.get("name"))
print (customer.get("Name")) # will return None as no key "Name" present in dictionary
print (customer.get("Name", "John-DOE")) # instead of returning none, will return a default value we mention

# We can add a key/value pair to dictionary
customer["dob"] = "20/04/1991"

print (customer)
print (customer["dob"])

print("************************************")
my_dict = dict(x=1, y=2, z=3)

for key, value in my_dict.items():
    print(key, value)

