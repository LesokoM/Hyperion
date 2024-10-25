from datetime import datetime
from tabulate import tabulate
from prettytable import PrettyTable
def validate_date():
    #this function is to ensure the correct date is entered
    #it will user the package call datettime 
    #assistance from https://stackoverflow.com/questions/44808807/how-to-ensure-user-input-date-is-in-correct-format
    #assistance from https://www.geeksforgeeks.org/python-datetime-strptime-function/
    current_date = datetime.today()
    print(current_date.day ,current_date.month, current_date.year)

    
    while True:
        date = input("Please enter due date in the following format dd/mm/yyyy: ") #getting user date 
        try: 
            date = datetime.strptime(date, "%d/%m/%Y") #converting entry into day, month and year 
            print(f"you have entered: {date.strftime('%d %B %Y')}")

            if date < current_date:
                print("Invalid date entered. Due date needs to be ahead of time") #making sure due date is ahead not behind current date
            else:
                print(f"Date approved {date.strftime('%d %B %Y')}") #changing month to the month name not value
                new_date = date.strftime('%d %B %Y')
                return new_date 

        except ValueError: 
            print("Invalid date entered please try again") #if numbers that are not correct date or incorrect format is entered except will deal with it 


def va():

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



def vm():
    
    input_username = input("Please enter username: ")
    vm_task_contents = open("PART_17\\tasks.txt", "r")

    vm_task_contents = vm_task_contents.read()
    
    vm_task_contents = vm_task_contents.strip() #removing spaces
    vm_task_contents = vm_task_contents.replace("\n",",") #removing \n and replacing it with ,
    vm_task_contents = vm_task_contents.split(",") #splitting it up based on , ]


    my_tasks =[]
    for i in range(0,len(vm_task_contents)):
        if vm_task_contents[i] == input_username:
            my_tasks.append(vm_task_contents[i:i+6])
        
 

    vm_headers  = PrettyTable(["User","Title", "Description", "Upload Date", "Due Date","Completion Status"], align= "c", max_width = 60)

    print(my_tasks)

    for i in my_tasks:

        vm_headers.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])

    print(vm_headers)



def admin_stats():

    with open("PART_17\\tasks.txt", "r") as task_stat: 
        lines = len(task_stat.readlines())


    with open("PART_17\\user.txt", "r") as user_stat: 
        lines2 = len(user_stat.readlines())


    headers = PrettyTable(["Total tasks", "Total users"])

    headers.add_row([lines,lines2])

    print(headers)

admin_stats()