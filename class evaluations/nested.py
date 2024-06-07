#problem statement
#you are hired as a software engineer to write a script that will help calculate the total price after several discount for every customer
#the conditions are 
#1 every new customer earns a 10% discount 
#2 every new customer with purchased items over 50,000 earns a 15% discount
#3 every existing customer earn a 3% discount
#4 every existing customer with purchased item over 50,000 earns a 10% discount
#5 every staff of the supermarket earn 5% discount 
# you are to ask for client name, status and total purchased item

print("welcome to this supermarket..... \n where you can get affordable items")
client_name = input("please enter your name  ")
print("please select your status from the options available ")
client_status = int(input("New customer == 1\n Existing customer == 2\n supermarket staffs == 3\n"))
# total_purchase_value = float(input("enter the total amount of the goods you bought "))
if client_status == 1:
    print("hello,welcome new client")
    total_purchase_value = float(input("enter the total amount of the goods you bought "))
    fifteenpercent = 0.15
    discounted_value = float(total_purchase_value * fifteenpercent)
    payable_amount = float(total_purchase_value - discounted_value)

    if total_purchase_value > 50000:
        print(f"you are paying {payable_amount} as a new customer")
    elif total_purchase_value < 50000:
        tenpercent= 0.1
        discounted_value2 = float(total_purchase_value * tenpercent)
        payable_amount2 = float(total_purchase_value - discounted_value2)
        print(f"you are paying 10% {payable_amount2} as a new customer")

elif client_status == 2:
    print("welcome back existing customer")   
    total_purchase_value = float(input("enter the total amount of the goods you bought "))
    """tenpercent = 0.1
    discounted_value = float(total_purchase_value * tenpercent)
    payable_amount = float(total_purchase_value - discounted_value)
    """

    if total_purchase_value > 50000:
        tenpercent = 0.1
        discounted_value3 = float(total_purchase_value * tenpercent)
        payable_amount3 = float(total_purchase_value - discounted_value3 )
        print(f"you are paying {payable_amount3} as an existing customer")

    elif total_purchase_value < 50000:
        threepercent = 0.03
        discounted_value3 = float(total_purchase_value * threepercent)
        payable_amount3 = float(total_purchase_value - discounted_value3 )
        print(f"you are paying {payable_amount3} as an existing customer")

elif client_status == 3:
    print("Youre a staff ")
    total_purchase_value = float(input("enter the total amount of the goods you bought "))
    fivepercent = 0.05
    discounted_value4 = float(total_purchase_value * fivepercent)
    payable_amount4 = float(total_purchase_value - discounted_value4 )
    print(f"you are paying {payable_amount4} as a staff")
else: 
    print("enter a valid status my friend")    