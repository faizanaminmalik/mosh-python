car_start = False
while True:
    user_input = input(">").upper()
    if user_input == "START":
        if not car_start:
            print ("car Started ..")
            car_start = True
        else:
            print ("car is already started, Sir!!!")
    elif user_input == "STOP":
        if car_start:
            print ("car Stopped..")
            car_start = False
        else:
            print ("Car Already stopped, Sire!!")
    elif user_input == "QUIT":
        print ("Goodbyes..")
        break
    elif user_input == "HELP":
        print("START: To start the car\n STOP: To stop the car\n Quit: To Quit")
    else:
        print ("I don't understand that")
