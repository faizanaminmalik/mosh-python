def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age

try:
    print(calculate_xfactor(0))
except ValueError as ex:
    print (ex)
