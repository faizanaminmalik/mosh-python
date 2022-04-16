fname = 'John'
lname = 'Smith'
message = fname + ' [' + lname + '] is a coder.'
print (message)
# The above method works but its hard to visualize and we can make mistakes in typing

msg = f'{fname} [{lname}] is a coder..'
print (msg)

#formatted string starts with f'<string>'
#places in between {} contain variables