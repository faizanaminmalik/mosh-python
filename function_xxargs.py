def save_user(**usr): # with double ** will save data as dictionary
    print(usr)
    print(usr.keys())
    print(usr.values())
    print(usr["name"])

save_user(id=101, name="faizan Malik", dob = "20/04/1991") # we can pass keywork arguments to fuction
save_user(id=102, name="Jahan Seerat", dob = "18/12/1991")