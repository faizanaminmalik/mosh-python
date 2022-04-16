# Task: to create dictionary for multiples of 2
values ={}
for x in range(5):
    values[x] = x * 2  # will create {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
print(values)

#Better method using dictionary comprehension in just 1 line
print("***************************************")
#{expression for item in items}
values = {x:x * 2 for x in range(5)}
print(values)