msg = "static data" # Global variable same across the whole file
def print_message(txt):
    msg = txt   # local variable anly exists in this function scope
    print(msg)

def modify_mesage(txt):
    global msg  # using global keyword, we tell python we will be accessing a global variable named msg, but this is  a bad practice
    msg = txt
    print(msg)
print_message("I am Good!")
print(msg)

print ("****************************")

modify_mesage("Updated data")
print(msg)