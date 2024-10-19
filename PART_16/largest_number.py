def value_input():
    while True:
        try: 
            #validating user input
            list_length  = int(input("How many numbers do you wish to input: "))
            break
        
        except ValueError:
            #handling any errors
            print("Incorrect value entered")


    my_list = []


    for i in range(0,list_length):
        #creating out list

        my_list.append(float(input(f"Please input num{i+1}: ")))

  
    
 
    return my_list




def largest_number(my_list, len):


    if len == 1:
        #if only 1 value is given then its the biggest
        
        return my_list[0]
    
        #got some assistance from https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/
        
    return max(my_list[len] , largest_number(my_list, len-1))
    #finding the biggest value using max function and recursion 





my_list  = value_input()

biggest_num = largest_number(my_list, len(my_list)-1)
print("-----------------------")
print(f"=> {biggest_num}")