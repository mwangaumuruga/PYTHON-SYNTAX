try:
    temperature_outside=int(input("enter temperature outside"))
    if temperature_outside>=20 and temperature_outside<=40:
        print("its a warm day no need to carry a sweater" )
        print("you can go outside")
    elif temperature_outside<=19 and temperature_outside>=10:
        print("its a cold day and we have a probability of it raining")
        sky_status=input("is it cloudy?....use <y>or <no>")
        if sky_status=="y":
            check_umbrella=input("can i find my umbrella ?use <y>or <no>")
            if check_umbrella=="y":
               print("YOU CAN PUT ON A SWEATER AND CARRY YOUR UMBRELLA!!!")
            else:
               print("PUT ON A SWEATER AND A RAIN COAT!!! PREPARE COZ IT MIGHT RAIN")
        else:
            print("PUT ON A SWEATER AND GO OUTSIDE THE SKY IS CLEAR")
    else:
         print("DUE TO CLIMATE CHANGE YOUR WEATHER IS MESSED UP YOU MAY BE FORCED TO LIVE IN BUNKERS LATER  PLEASE PLANT A  TREE AND REDUCE CARBON EMISSINS!!!!")

    



except ValueError:
    print("please enter valid  temperature in degrees")
    
