names = ['John', 'Adam', 'George', 'Lena']
print (names)
print (names[1])
print (names[1:3])

names[0] = 'johny'
print (names)

#*******************************************
# Some various ways of defining lists

letters = ["a", "e", "i", "o", "u"]
matrix = [[1,2,3], [4,5,6]]
zeros = [0] * 10
combined = zeros + letters
twenty_numbers = list(range(20))
chars = list("Hello World")

print(letters)
print(matrix)
print(zeros)
print(combined)
print(twenty_numbers)
print(chars)

print(twenty_numbers[::2]) # ::2 means we want to retreive every second element from the list