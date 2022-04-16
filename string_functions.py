str = 'Python is a programing language'
print (len(str))
#len returns length of string
# apart from strings, len can also be used for other datastructures like lists etc.

print (str.upper())
print (str)
#upper() method does not update the actual variable, but creates a temporary string with all UPERCASE

print (str.lower())

#sometimes we want to look for a specific character or a specific sub-string then we can use find() method
print (str.find('o'))
print (str.find('p'))
print (str.find('P'))
print (str.find('is'))
print (str.find('O')) # We don't have O in string, returned index of any character not matching is -1

#we can replace a character or a string with another.
print (str.replace('programing', 'scripting'))

#use in operator to check if a substring is present. Returns True or False

print ('Python' in str)