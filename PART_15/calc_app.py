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

            print(operation)
        
            while operation not in acceptable_operations: 
                print(f"You have selected {operation}. This is incorrect!")
                operation = input("Please enter an operation ( +, - , * or /): ")
            else:
                print("Acceptable operation")
                userInput.append(operation)

    return userInput



def calculator_activate( userInput):
    #we know the pattern for input will be num1 num2 and operation 
    print("Activating calculator...../n")
    for i in range(0, len(userInput)):

        if userInput[len(userInput-1)] == "+":
            print("Doing additon")
        elif userInput[len(userInput-1)] == "-":

            print("Doing subtraction")
        elif userInput[len(userInput-1)] == "*":
            print("Doing multiplication")
        
        elif userInput[len(userInput-1)] == "/":
            print("Doing division")

            




   






my_input = userInput_validation()
print(f"You have inputted the following: {my_input}")

calculator_activate(my_input)



