from datetime import datetime

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


  
validate_date()