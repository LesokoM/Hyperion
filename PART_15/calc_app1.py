'''
fits 2 numbers and an operation ( function takes 3 arguments)
    -if user enters a string instead of number
    -if user enters unknown operations
    -can store user input into a list then forces 




we need to create a file that we will write to 

num,num2, operation 
'''

userInput = []
acceptable_operations = ["+", "-","*","/"]

def userInput_validation(): 
    for i in range(0,3):
        if i <=1:
            userInput.append(int(input("Please enter a number:")))       
            i +=1
        elif i>1:
            operation = input("Please enter an operation ( +, - , * or /):")
            while operation not in acceptable_operations: 
                print(f"You have selected {operation}. This is incorrect!")
                operation = input("Please enter an operation ( +, - , * or /): ")
            else:
                print("Acceptable operation")
                userInput.append(operation)

    return userInput



def calculator_activate(userInput):
    #we know the pattern for input will be num1 num2 and operation 
    print("----------------Activating calculator--------------")
   
    for i in userInput:

        if userInput[len(userInput)-1] == "+":
            print("Doing additon")
            print(f"{userInput[0]} + {userInput[1]} = {userInput[0]+userInput[1] }")
            break
        elif userInput[len(userInput)-1] == "-":
            print("Doing subtraction")
            print(f"{userInput[0]} - {userInput[1]} = {userInput[0] - userInput[1] }")
            break
        elif userInput[len(userInput)-1] == "*":
            print("Doing multiplication")
            print(f"{userInput[0]} x {userInput[1]} = {userInput[0]*userInput[1] }")
            break
        elif userInput[len(userInput)-1] == "/":
            print("Doing division")
            print(f"{userInput[0]} ÷ {userInput[1]} = {userInput[0]/ userInput[1] }")
            break
            

def userMenu():
    calc_menu = {
        1: "Do a calculation",
        2: "Print previous calculations",
        3: "Quit the app"
    }
    counter = 0
    while counter <1: 
  
        for key, value in calc_menu.items():
            print(f"{key}:{value}")
        menu_selection = int(input(f"Welcome to FUN with CALC please select an option:"))

        if menu_selection == 1: 
            counter +=1
            userInput_validation()
            
        elif menu_selection ==2: 
            print("You havent done any calculations")

        elif menu_selection ==3: 
            print("Goodbye...")
            break
        

    



   



userMenu()

'''
my_input = userInput_validation()
print(f"You have inputted the following: {my_input}")
calculator_activate(my_input)

'''



