import random
import string

print(random.random()) # generate any random floating point number like 0.2324242424322
print(random.randint(1, 5)) # generates a random nu between 1 and 5
print(random.choice([11, 12, 13])) # picks any random number from specified list of numbers
print(random.choices([11, 22, 33, 44,55,66,77,88], k=3)) # picks 3 random numbers (numbers can repeat) from list specified
print(random.choices("abcdefghijklmnopqrstuvwxyz", k=7)) # generates 7 random chars. but result is in list ['a', 'f', d']
print("".join(random.choices("abscefrgm", k=4))) # generated 4 char string in proper form
print("".join(random.choices(string.ascii_letters + string.digits, k=8))) # generated a random text of 8 chars long

nums = [1,2,3,4,5]
random.shuffle(nums)
print(nums)