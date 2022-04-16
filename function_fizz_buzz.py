def fizz_buzz(num):
    return_msg = ''
    if num % 3 == 0:
        return_msg += "Fizz"
    if num % 5 ==0:
        return_msg += "Buzz"
    if return_msg == '':
        return_msg = num
    return return_msg
print(fizz_buzz(18))

print ("***********************************")
#**********************************************************
# Method 2
def fizz_buzz2(num):
    if (num % 3 == 0) and (num % 5 == 0): # make sure to have most significant condition at top
        return ("FizzBuzz")
    if num % 3 == 0:
        return ("Fizz")
    if (num % 5 ==0):
        return ("Buzz")
    return num
print(fizz_buzz2(13))