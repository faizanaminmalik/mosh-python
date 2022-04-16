weight = float(input('Enter your weight:'))
unit = input ('Entered weight is (K)kg or (L)lbs :')
if unit.upper() == 'K':
    print(f'Your weight is {weight * 2.205} lbs')
elif unit.upper() == "L":
    print(f'Your weight is {weight / 2.205} kgs')
else:
    print ("Incorrect option")