student_count  = int(input("How many students will be in attendance?: "))

student_register = open("reg_form.txt", "w")

for i in range(0,student_count):
    correct_code = False 

    while correct_code == False:
        ID = input("Please enter your 6 digit student number: ")

        while len(ID) != 6 or any(x.isalpha() for x in ID)  == True :
             #error handling if the user puts in less than 6 digits or if the user enters something that is not an int
             # source for assitance with any statement - https://stackoverflow.com/questions/9072844/how-can-i-check-if-a-string-contains-any-letters-from-the-alphabet
            ID = input("Incorrect! Missing numbers. Please enter your 6 digit student number again: ")
            correct_code = False 
        else: 
            correct_code = True 

    student_register.write(ID +"..............." +  "\n")
    

    

student_register.close()
