import sqlite3
from tabulate import tabulate
import os
from tqdm import tqdm
import time


#starting_balance = int(input("What is your current balance? ie R12 000.50: R"))



class menuSelection():
  
    def __init__(self):
                           
        self.category_list  = ["Savings", "Groceries","Utilites","Health","Insurance","Transportation","Clothing","Cellphone and Internet" , "Petrol/Diesel","Housing", "Main Job", "Side Hustle"]


        self.db =sqlite3.connect('budgettracker.db') #links us to the database
        self.cursor = self.db.cursor() #creates a cursor linked to the database 

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS budgettracker(
                    id INTEGER PRIMARY KEY,
                    Date DATE,
                    Description TEXT,
                    Type TEXT,
                    Category TEXT,
                    Amount INT,
                    Comments TEXT)
                    ''') #creating database 

        self.db.commit()
        
        if os.path.exists("initialised.txt"):
            print("EXISTS")
        else:    

            with open("initialised.txt","w") as file:
                pass
            dummy_entries = [
            ("2024-01-05", "Salary", "Income", "Main Job", 15000, "January salary from main job"),
            ("2024-02-14", "Groceries", "Expense", "Groceries", -1200, "Weekly grocery shopping"),
            ("2024-03-10", "Electricity Bill", "Expense", "Utilities", -900, "Monthly electricity bill"),
            ("2024-04-05", "Health Insurance", "Expense", "Health", -2000, "Monthly health insurance payment"),
            ("2024-05-20", "Petrol", "Expense", "Petrol/Diesel", -800, "Fuel for the car"),
            ("2024-06-15", "Freelance Work", "Income", "Side Hustle", 3000, "Completed a graphic design project"),
            ("2024-07-01", "Rent", "Expense", "Housing", -7500, "Monthly apartment rent"),
            ("2024-08-10", "Clothing", "Expense", "Clothing", -1800, "Bought new work outfits"),
            ("2024-09-25", "Savings Deposit", "Expense", "Savings", -5000, "Transferred to savings account"),
            ("2024-10-12", "Internet Bill", "Expense", "Cellphone and Internet", -700, "Monthly internet subscription"),
            ("2024-11-15", "Car Insurance", "Expense", "Insurance", -1200, "Quarterly car insurance payment"),
            ("2024-12-24", "Groceries", "Expense", "Groceries", -1400, "Christmas grocery shopping"),
            ("2024-01-20", "Phone Plan", "Expense", "Cellphone and Internet", -500, "Monthly cellphone plan"),
            ("2024-03-30", "Public Transport", "Expense", "Transportation", -150, "Bus tickets for the month"),
            ("2024-04-15", "Medical Checkup", "Expense", "Health", -600, "Annual health checkup"),
            ("2024-06-25", "Petrol", "Expense", "Petrol/Diesel", -900, "Filled up the tank"),
            ("2024-09-05", "Salary", "Income", "Main Job", 15000, "September salary from main job"),
            ("2024-10-30", "Utilities", "Expense", "Utilities", -1000, "Monthly water and electricity bill"),
            ("2024-11-18", "Groceries", "Expense", "Groceries", -1100, "Weekly grocery shopping"),
            ("2024-12-10", "Side Gig", "Income", "Side Hustle", 4000, "Income from tutoring students"),
                    ]
        
            self.cursor.executemany('''
                                INSERT OR IGNORE INTO budgettracker(Date,Description,Type,Category,Amount,Comments)
                                VALUES(?,?,?,?,?,?)
                                ''', dummy_entries)
            
            self.db.commit()
            file.close()
                        #we have to make it run once because it re-assigns them and removes the changes we need flag for dummy lis and pre-exisiting category list
            self.category_list.sort()
        


        self.menu_selection()
    

    def loading_screen(self):
        for i in tqdm(range(5)):
                    time.sleep(0.2)

    def clear_screen(self):
        if os.name== "nt":
            os.system("cls")
        else:
            os.system("clear")
         
    def menu_selection(self):
        time.sleep(5)
   
        menu_dictionary = {
        1: self.add_expense,
        2: self.view_expenses,
        3: self.view_expenses_by_category,
        4: self.add_income,
        5: self.view_income,
        6: self.view_income_by_category,
        7: self.add_a_category,
        8: self.set_budget_for_a_category,
        9: self.view_budget_for_category,
        10: self.set_financial_goals,
        11:self.view_progress_towards_financial_goals,
        12:self.quit_app,
        13:self.delete_account

        } #dictionary holding all the functions from the menu

        while True:  #ensuring user choses an option thats possible 

            try:
                menu_num_selection = int(input('''
                                1.Add expense
                                2.View expenses 
                                3.View expenses by category 
                                4.Add income
                                5.View income
                                6.View income by category 
                                7.Add a category
                                8.Set budget for a category 
                                9.View budget for category 
                                10.Set financial goals
                                11.View progress towards financial goals
                                12.Quit 
                                13.Delete Account
                                >> '''
                                            ))
                if menu_num_selection > len(menu_dictionary) or menu_num_selection < 1:
                    print("Incorrect option selection")
                else: 
                    break 

            except ValueError: 
                print("You have not entered a correct value")

        menu_dictionary[menu_num_selection]()


    def create_table(self, rows):
        #creating neater output. Need to create it so that it works everytime when displaying the db too 
        self.loading_screen()
        self.clear_screen()
   
        headers = ["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]

        table = tabulate(zip(headers,rows), headers= ["Information", "Your Input"], tablefmt = "fancy_grid")
        print(table)


    def create_table_with_own_headers(self,headers, rows):
    #neater output 
        self.loading_screen()
        self.clear_screen()
        
        table = tabulate(rows, headers= headers, tablefmt = "fancy_grid")
        print(table)

    def add_expense(self):

        while True:

            temp_date = input('''Please enter the date of the transaction ie yyyy-mm-dd: >>''')
            
            temp_description = input('''Please give the transaction a name: >>''')

            temp_type = 'Expense'
         
            while True:
                for index, value in enumerate(self.category_list, start=1):
                    print(f"{index}. {value}")

                try: 
                    category_selection = int(input("Please select a category ie 3: "))

                    if(category_selection > len(self.category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")



            temp_amount = float(input('''How much was spent ie R120.05? >> -R'''))*-1
            
            temp_comments = input('''Please enter any comments you have about this transaction: >>''')

        
            #creating table for better visibility 
            rows = [temp_date, temp_description,temp_type,self.category_list[category_selection-1],temp_amount,temp_comments]
            self.create_table(rows)

            #validating input
            correct_info = input("Please confirm if the following is correct[Y/n]:").lower()
            print(f'Your response: {correct_info}')

            #validating if the details entered are correct
            if correct_info != 'y' and correct_info != 'n':
                self.create_table(rows)
                correct_info = input("Incorrect option chosen.Please confirm if the following is correct[Y/n]:").lower().strip()
                print(f'Your response: {correct_info}')    
            elif correct_info == 'y':
                print("Input Valid!")
            
                #adding entry into database
                self.cursor.execute('''
                                    INSERT INTO budgettracker (Date, Description,Type, Category,Amount,Comments)
                                    VALUES(?,?,?,?,?,?)''', rows)
                self.db.commit()
                
                break
            else: 
                print("Incorrect input! Please re-enter... ")
        


        self.menu_selection()


    def view_expenses(self):
       
        
        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Type = 'Expense'
                            ORDER BY Date
                            ''')
        list_expenses = self.cursor.fetchall()
        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
        self.create_table_with_own_headers(headers,list_expenses)
        time.sleep(2)
        self.menu_selection()
        







    def view_expenses_by_category(self):

      

        while True:
                for index, value in enumerate(self.category_list, start=1):
                    print(f"{index}. {value}")

                try: 
                    category_selection = int(input("Please select a category to view ie 3: "))

                    if(category_selection > len(self.category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")

    
        print(self.category_list[category_selection-1])
        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Category = ? AND Type = 'Expense'
                            ORDER BY Date
                            ''', (self.category_list[category_selection-1],) )
        
        list_expenses = self.cursor.fetchall()

        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers,list_expenses)

        time.sleep(2)
        self.menu_selection()
        
        
        


    def add_income(self):
        
        while True:

            temp_date = input('Please enter the date of the transaction ie yyyy-mm-dd: >>')
            
            temp_description = input('Please give the transaction a name: >>')

            temp_type = 'Income'

            while True:
                for index, value in enumerate(self.category_list, start=1):
                    print(f"{index}. {value}")

                try: 
                    category_selection = int(input("Please select a category ie 3: "))

                    if(category_selection > len(self.category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")


            temp_amount = float(input('How much was recieved ie R120.05? >> R'))
                 
            temp_comments = input('Please enter any comments you have about this transaction: >>')

    
            #creating table for better visibility 
            rows = [temp_date, temp_description,temp_type, self.category_list[category_selection-1],temp_amount,temp_comments]
            self.create_table(rows)

            #validating input
            correct_info = input("Please confirm if the following is correct[Y/n]:").lower()
            print(f'Your response: {correct_info}')

            #validating if the details entered are correct
            if correct_info != 'y' and correct_info != 'n':
                self.create_table(headers,rows)
                correct_info = input("Incorrect option chosen.Please confirm if the following is correct[Y/n]:").lower().strip()
                print(f'Your response: {correct_info}')    
            elif correct_info == 'y':
                print("Input Valid!")
            
                #adding entry into database
                self.cursor.execute('''
                                    INSERT INTO budgettracker (Date, Description,Type, Category,Amount,Comments)
                                    VALUES(?,?,?,?,?,?)''', rows)
                self.db.commit()
                
                break
            else: 
                print("Incorrect input! Please re-enter... ")
        


        self.menu_selection()


    def view_income(self):

        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Type = 'Income'
                            ORDER BY Date
                            ''')
        list_income = self.cursor.fetchall()
        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]


        self.create_table_with_own_headers(headers,list_income)
        time.sleep(2)
        self.menu_selection()
        
   
    def view_income_by_category(self):
      
        
        while True:
                for index, value in enumerate(self.category_list, start=1):
                    print(f"{index}. {value}")

                try: 
                    category_selection = int(input("Please select a category to view ie 3: "))

                    if(category_selection > len(self.category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")

    
 
        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Category = ? AND Type = 'Income'
                            ORDER BY Date
                            ''', (self.category_list[category_selection-1],) )
        
        list_incomes = self.cursor.fetchall()

        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers,list_incomes)
        time.sleep(2)
        self.menu_selection()
        

    def add_a_category(self):
 
 
        new_category = input("Please enter a new category: ")

        edited_category_list = []

        for i in self.category_list:
            i = i.strip()
            i = i.lower()

            edited_category_list.append(i)


        if new_category.strip().lower() in edited_category_list:
            print("This category already exists")
        else:
            self.category_list.append(new_category)
            self.category_list.sort()

        self.loading_screen()
        print("=== Saved Categories ===")
        for i, value in enumerate(self.category_list, start=1):
            print(f"{i}. {value}")

        time.sleep(1)
        self.menu_selection()



    def set_budget_for_a_category(self):
        print("ENTERING set_budget_for_a_category")
        self.category_list.sort()
        print(self.category_list)
        




        
    def view_budget_for_category(self):
        print("ENTERING view_budget_for_category")
        pass
    def set_financial_goals(self):
        print("ENTERING set_financial_goals")
        pass
    def view_progress_towards_financial_goals(self):
        print("ENTERING view_progress_towards_financial_goals")
        pass
    def quit_app(self):
        print("Goodbye...")
        exit()
        pass
    def delete_account(self):
        confirm_delete = input("You are about to permenatley delete your account! Are you sure [Y/n]: ").lower()

        if confirm_delete == 'n':
            pass

          


        self.cursor.execute('''
                        DROP TABLE budgettracker

                            ''')


        pass


#####################################
mySavings = menuSelection()
mySavings.menu_selection()
       






