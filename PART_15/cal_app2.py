



'''
def userInput():
    user_input = []
    input_incomplete = True
    
    while input_incomplete:
        for i in range(0,2):
            num = input(int("Please enter a number"))
            user_input.append(num)

     
        operation = input("Please enter an operation ie +,-,* or / ")
        user_input.append(operation)
        input_incomplete = False

'''
def menu_options():
    acceptable_operations = ["+", "-","*","/"]
    def user_input():
        print("Inside userInput ")
        user_input = []
        input_incomplete = True
        
        while input_incomplete:
            for i in range(0,2):
                num = int(input("Please enter a number"))
                user_input.append(num)

        
            operation = input("Please enter an operation ie +,-,* or / ")
            user_input.append(operation)
            input_incomplete = False

    def menu_selection(option_chose):


    calc_menu = {
        1: ["Do a calculation", user_input], #storing function by reference so that it doesnt run when i try to print the list 
        2: ["Print previous calculations"],
        3: ["Quit the app"]
    }
    print("Calc menu created")
    for key, value in calc_menu.items():
        print(f"{key} {value[0]}")

    option_chose = int(input("Please select an option:"))

    menu_selection(option_chose)




menu_options()

