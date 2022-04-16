secret_num = 9
i=0
while i < 3:
    user_num = int(input('Guess:'))
    i += 1
    if user_num == secret_num:
        print ('You Won')
        break
else:
    print ('You lost in 3 tries!')

