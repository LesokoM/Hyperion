def value_input():
    #validating user input
    while True:
        try: 
            list_length  = int(input("How many numbers do you wish to input: "))
            #checking for whole numbers only 
            break
        
        except ValueError:
            #handling any errors 
            print("Incorrect value entered")


    my_list = []
    
    for i in range(0,list_length):
        my_list.append(float(input(f"Please input num{i+1}: ")))
        #creating my list
  

    while True: 
        try: 
            #finding up to which index user wants to calculate 
            index_value = int(input("Up to which index do you wish to calculate to?: "))
            if index_value > len(my_list)-1:
                #ensuring correct index value is given cant be out of bounds 
                print("Your index value is greater than your list size. Please re-enter")
            else: 
                break #if correct value is given then move on 
        except:
            print("Incorrect value entered")

    
    
 
    return my_list, index_value

def add_up_to(user_input, index):

    if index == 0:
    
        return user_input[0]
    #adding up the list until the given index using recursion
    return  user_input[index] + add_up_to(user_input, index-1)




user_input, index = value_input()
my_total = add_up_to(user_input, index)

print(f"total is: {my_total}")# printing sum of numbers 




