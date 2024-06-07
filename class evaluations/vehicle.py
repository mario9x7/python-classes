print("welcome to my code, this function is used to calculate the number of people using a paricular vehicle")
no_of_passangers = int(input("enter a number to determine the type of vehicle you drive"))

def vehicle(no_of_passangers):
    if 1 <= no_of_passangers <= 2:
        return "bike"
    elif 3 <= no_of_passangers <= 4:
        return "tricycle"
    elif 5 <= no_of_passangers <= 6:
        return "car"
    elif 7 <= no_of_passangers <= 8:
        return "korope"
    elif 9 <=no_of_passangers <= 14:
        return "danfo"
    else:
        return "Maybe you drive a Coaster Bus or Input a valid Bus "
    
print(f'You drive a {vehicle(no_of_passangers)}')
   