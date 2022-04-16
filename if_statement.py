is_hot = False
is_cold = False

if is_hot:
    print ("It's a hot day")
    print ("Drink plenty of water")
elif is_cold:
    print ("It's a cold day")
    print ("Wear warm clothes")
else:
    print ("Its a wonderful day")

##################################################
house_price = 1000000
buyer_credit = 4

if buyer_credit >= 7:
    print ("You have a good credit score")
    print ("You need to pay a 10 % downpayment of USD ",house_price * 0.1)
else:
    print ("You don't have a good credit score")
    print ("You need to pay a 20 % downpayment of USD ",house_price * 0.2)