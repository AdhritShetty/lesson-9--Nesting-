vehicle_of_choice=str(input("Choose a vehicle:"))
if vehicle_of_choice=="bike":
    print ("your options are either a scooter or motorcycle")
    two_wheeler=str(input("choose a two wheeler:"))
    if two_wheeler=="scooter":
        print("let's pack the scooter")
    else:
        print("let's pack the motorcycle")
else:
    print("yourr options are a manual or automatic")
    four_wheeler=str(input("choose a four wheeler:"))
    if four_wheeler=="manual":
        print("let's pack the car")
    else:
        print("let's pack the automatic one then")
