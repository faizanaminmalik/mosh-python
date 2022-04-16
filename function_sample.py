def greet_user(fname,lname):
    print (f'Welcome aboard, {fname} {lname}')
    print ("Nice to have you")

print ("Start")
greet_user("faizan", "malik") #positioned arguments
greet_user(lname="jahan", fname="seerat") #Keyword arguments

# positional args should come before keywork args
greet_user("doe",lname="jane")
print("Finish")