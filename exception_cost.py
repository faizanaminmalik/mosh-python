from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age

try:
    calculate_xfactor(0)
except ValueError as ex:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None # Just by using simple if statement, we save cost on exceptions
    return 10/age

calculate_xfactor(0)
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))