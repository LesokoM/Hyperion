import sys # importing this package so we can use exit function for when user decides to quit the program 

def do_calculation(num1, num2, operation):
 #this functions takes in the user inputs and does the requested calculation 
 #the input entered here is already accurate
    if operation ==  "+":
        print("Doing addition...")
        print(f"{num1} + {num2} = {num1 + num2 }")
        write_to_file(f"{num1} + {num2} = {num1 + num2 }")

            
    elif operation ==  "-":

        print("Doing subtraction...")
        print(f"{num1} - {num2} = {num1 - num2}")
        write_to_file(f"{num1} - {num2} = {num1 - num2 }")
        
    elif operation ==  "*":
        print("Doing multiplication...")
        print(f"{num1} x {num2} = {num1 * num2}")
        write_to_file(f"{num1} x {num2} = {num1 * num2 }")
 
    elif operation == "/":
        print("Doing division...")
        try:
            print(f"{num1} ÷ {num2} = {num1 / num2}")
        except:
            #if we try to do illegal division 
            print("This operation will not work. Please re-enter your values")
            num1  = int(input("Please re-enter value 1: "))
            num2  = int(input("Please re-enter value 2: "))
            print(f"{num1} ÷ {num2} = {num1 / num2}")

        write_to_file(f"{num1} ÷ {num2} = {num1 / num2 }")


    calc_menu() #calling out menu function again as we might want to redo the value



    
       
def input_values(): 

    #here we have to input the values
    #and we also have to ensure the correct values are inputed 
    #nums must be int values
    #if negative number is inputed cant be seen as a string
    #operations must be strings +,-,/or * ONLY 
    acceptable_operations = ["+", "-","*","/"]
    num1_incomplete = True
    num2_incomplete = True
    operation_incomplete = True 
    # the above is to ensure we continue to ask user for input until we get the correct user input

    while num1_incomplete: 
        try:
            num1 = int(input("Please enter your first number: "))
            num1_incomplete = False 
        except ValueError: 
            print("You have not entered a number")
            # if user does not enter a number
            
    

    while num2_incomplete: 
        try:
            num2 = int(input("Please enter your second number: "))
            num2_incomplete = False 
        except ValueError: 
            print("You have not entered a number")
            # if user does not enter a number
        

    while operation_incomplete:
        operation = input("Please enter your operation( *,/,- or +): ")
        while operation not in acceptable_operations: 
            operation = input("Incorrect operation. Please enter your operation again ie( *,/,- or +): ")
            # making sure user is entering an operation our calculator can handle 
        else:
            operation_incomplete = False 

    
    return num1, num2, operation 

def create_file():
    ofile = open("equations.txt", "w") 
    # creating a file we can write to

def write_to_file(line):
    #this function takes in the operation being done and adds it to the file 
     
    ofile = open("equations.txt", "a") # using a here so that we dont overwrite but add/grow the file 
    ofile.write( line  + "\n")
   

def print_menu():
    #printing menu so user knows the options available to them 


    menu = {
        1: "Do a calculation",
        2: "Print calculation history",
        3: "Quit program"
    }

    for key,value in menu.items():

        print(f"{key} {value}")
    


def calc_menu():
    #this filters the users choice 

    
        
    print_menu() # printing user options 

    user_entry = True
    while user_entry: 
        try: 
            user_choice = int(input("Please select an option: "))
            while user_choice >= 4 or user_choice <= 0:
                print("You have selected an item not on the menu. Please try again ")
                print_menu()
                user_choice = int(input("Please select an option: "))
            else:
                print("Correct option selected")
                user_entry = False 

        except ValueError: 
            print("You have not entered a number. Please try again ")
            print_menu()

    if user_choice ==3:
        
        print("Goodbye...")
        exit()
        # idea from https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/



    elif user_choice == 1:
        my_num1, my_num2, my_operation = input_values()
        do_calculation(my_num1, my_num2, my_operation)
        calc_menu()




    elif user_choice ==2: 
        #we have to be sure that previous cal has been made 
        check_file = open("equations.txt", "r")
        check_file = check_file.read()

        if len(check_file) ==0:
            print("You have not done any calculations. There is nothing to print")
            calc_menu()
        else: 
            print(check_file)
        
   

        
    
create_file()
calc_menu()
