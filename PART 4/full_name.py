
response  = True 

if response:
    full_name  = input("Please enter full name: ")
    if full_name == "":
        print("You havent entered anything")
    elif len(full_name) <= 4: 
        print("You have entered less than 4 characters. Please make sure that you have entered your full name and surname.")
    elif len(full_name) >25: 
        print(" You have entered more than 25 characters. Please make sure that you have entered your full name")
    else: 
        print("Thank you for entering your name")
        response = False