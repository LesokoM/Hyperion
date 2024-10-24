#=====importing libraries===========
from datetime import datetime
from prettytable import PrettyTable
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

def find_usernames_and_passwords():
     
    user_login_details = open("PART_17\\user.txt", "r")
    usernames = []
    passwords = []

    #creating usable copies of my code
    for line in user_login_details:
        #removing white space and removing \n character
        print(line)
        line = line.replace(" ", "").strip() # getting line in workable format
        print(line)
        for i in range(0, len(line)):
            if line[i] == ",":

                usernames.append(line[:i])
                passwords.append(line[i+1:])
    user_login_details.close()
    print(f"Usernames: {usernames}")
    print(f"Passwords: {passwords}")
    print("------------------------------------")
    return usernames, passwords

def login(database_usernames, database_passwords):
    input_username = input("Please enter username: ")
    number_of_tries = 5
  
    while True:


        if number_of_tries == 0:
                #this ensures that user has only 5 tries before they have to re-enter username and start process again
                #this ensures that if they entered the wrong username but a valid one they have the chance to fix it
                number_of_tries = 5
                print("You have exceeded the number of tries. Restarting login process...")
                input_username = input("Please enter username: ")



        if input_username  in database_usernames:
             #if we find the username in the database get its index and compare it to the password database 
            index  = database_usernames.index(input_username) # idea comes from https://www.geeksforgeeks.org/python-list-index/


            while number_of_tries > 0: #ensures thetre is a limit to the number of password tries 
                input_password = input("Please enter password: ")

                if input_password == database_passwords[index]: #if username/password pair is correct quit the login loop 
                    print("Correct username and password")
                    menu(input_username)
                else:
                    number_of_tries-=1
                    print(f"Incorrect password. Number of tries left: {number_of_tries}")     
        else:
            input_username = input("Incorrect!. Please re-enter username: ")
    
def validate_date():
       #this function is to ensure the correct date is entered
    #it will user the package call datettime 
    #assistance from https://stackoverflow.com/questions/44808807/how-to-ensure-user-input-date-is-in-correct-format
    #assistance from https://www.geeksforgeeks.org/python-datetime-strptime-function/
    current_date = datetime.today()

    
    while True:
        date = input("Please enter due date in the following format dd/mm/yyyy: ") #getting user date 
        try: 
            date = datetime.strptime(date, "%d/%m/%Y") #converting entry into day, month and year 
            

            if date < current_date:
                print("Invalid date entered. Due date needs to be ahead of time") #making sure due date is ahead not behind current date
            else:
                new_date = date.strftime('%d %B %Y') #changing month to the month name not value
                return new_date 

        except ValueError: 
            print("Invalid date entered please try again") #if numbers that are not correct date or incorrect format is entered except will deal with it 





 

def menu(active_user):

    while True:
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

        if menu == 'r':
            pass
            '''This code block will add a new user to the user.txt file
            - You can use the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same
                - If they are the same, add them to the user.txt file,
                otherwise present a relevant message'''
            while True:
                new_username = input("Please enter a new username: ")

                if new_username not in database_usernames:
                    #checking that the username is not already in use 
                    while True:
                        new_password = input("Please enter a new password: ")
                        temp_password  = input("Please confirm the password: ")
                        #creating a password and the comparison password 
                        if new_password == temp_password:
                            print("Creating new username....")
                            break 
                            #if passowrd and username is correct we can now move on to adding them to the file 
                        else: 
                            print("Passwords do not match!")
                            #telling user that passwords dont match and prompting them to re-enter them 

                    print(f"Your new username is {new_username} and new password is {new_password}") #displaying new logins to users
                    break   
                    
                else:
                    print("That username is already taken. Please enter a different one.")
                    #if username already made user prompted to enter a different one 


            write_to_file = open("PART_17\\user.txt", "a")

            write_to_file.write(f"{new_username}, {new_password}\n")
            write_to_file.close()






        elif menu == 'a':
            #saving todays day in variable 
            current_date = datetime.today()
            pass
            '''This code block will allow a user to add a new task to task.txt file
            - You can use these steps:
                - Prompt a user for the following: 
                    - the username of the person whom the task is assigned to,
                    - the title of the task,
                    - the description of the task, and 
                    - the due date of the task.
                - Then, get the current date.
                - Add the data to the file task.txt
                - Remember to include 'No' to indicate that the task is not complete.'''
            #creating option menu for available usernames to assign task 
            for i in range(0, len(database_usernames)):
                print(f"{i+1}: {database_usernames[i]}")

            while True:
                try:
                    #asking which username user wants to chose
                    task_to_which_user  = int(input("Please select which user to assign the task to: "))
                    #ensuring they choose a value that is actually listed
                    if task_to_which_user > len(database_usernames) or task_to_which_user <= 0:
                        print("You have selected a number not on the list. Please try again")
                    else: 
                        task_to_which_user-=1#getting the index number
                      
                        break
                except ValueError:#if user enters something that is not a number catch the error
                    print("You have not selected a number. Please try again")
            #displaying which user was selected
            print(f"You have selected {database_usernames[task_to_which_user]} ")

            while True: 
                try:
                    #getting title and desciption 
                    task_title = input("Please enter task title: ")
                    task_description = input("Please enter a short description of the task: ")

                        #making sure title and description arent too long or short
                    if len(task_description) <10:
                        print("The description is too short. Please try again.")
                    elif len(task_description) > 60 or len(task_title) > 15:
                        print("The description or title is too long. Please try again.") 
                    else:
                        break
                        #catching any errors if they only put int values
                except ValueError:
                    print("You have not entered an adequate description")

            #using separate function to get date (make sure its correct)
            due_date = validate_date()

            print(f"Due date is {due_date}")
            
            now_date  = f"{current_date.day} {current_date.strftime('%b')} {current_date.year}" #reforamtting current time so it follows the instructed format. using %b to get month in words
            
            #opening file
            write_to_taskfile = open("PART_17\\tasks.txt", "a")

            #writing to file
            write_to_taskfile.write(f"{database_usernames[task_to_which_user]}, {task_title}, {task_description}, {now_date}, {due_date}, No\n")
            #closing file 
            write_to_taskfile.close()
           

        elif menu == 'va':
            pass
            '''This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the PDF
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 in the PDF
                - It is much easier to read a file using a for loop.'''
            task_contents = open("PART_17\\tasks.txt", "r")

            task_contents = task_contents.read()
            
            task_contents = task_contents.strip() #removing spaces
            task_contents = task_contents.replace("\n",",") #removing \n and replacing it with ,
            contents = task_contents.split(",") #splitting it up based on , 

            
            #idea to use prettytables to make it readeable https://www.geeksforgeeks.org/printing-lists-as-tabular-data-in-python/

            print(len(contents))

            #more formatting options idea from https://github.com/prettytable/prettytable/issues/130
            headers  = PrettyTable(["User","Title", "Description", "Upload Date", "Due Date","Completion Status"], align= "c", max_width = 60)
            
            for i in range(0,len(contents),6):
                print(i)
                headers.add_row([contents[i],contents[i+1],contents[i+2],contents[i+3],contents[i+4],contents[i+5]])
                headers.add_row(['','','','','','']) #space after each entry 
            print(headers)








        elif menu == 'vm':
            pass
            '''This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in the PDF
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the 
                username you have read from the file.
                - If they are the same you print the task in the format of Output 2
                shown in the PDF '''
           
            vm_task_contents = open("PART_17\\tasks.txt", "r")

            vm_task_contents = vm_task_contents.read()
            
            vm_task_contents = vm_task_contents.strip() #removing spaces
            vm_task_contents = vm_task_contents.replace("\n",",") #removing \n and replacing it with ,
            vm_task_contents = vm_task_contents.split(",") #splitting it up based on , ]
            

            my_tasks =[]
            for i in range(0,len(vm_task_contents)):
                if vm_task_contents[i] == active_user:
                    my_tasks.append(vm_task_contents[i:i+6])
                
       

            vm_headers  = PrettyTable(["User","Title", "Description", "Upload Date", "Due Date","Completion Status"], align= "c", max_width = 60)

            print(my_tasks)

            for i in my_tasks:

                vm_headers.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

            print(vm_headers)

                    
            


        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")




database_usernames, database_passwords = find_usernames_and_passwords()
my_username, my_password = login(database_usernames, database_passwords)
