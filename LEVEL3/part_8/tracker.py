import sqlite3
from tabulate import tabulate
import os
from tqdm import tqdm
import time

class menuSelection():
    def __init__(self):
        self.loading_screen()

        self.db =sqlite3.connect('budgettracker.db') # links us to the database
        self.cursor = self.db.cursor() # creates a cursor linked to the database 

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY,
            Category_Name TEXT,
            Budget INTEGER      
            )''')

        self.db.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgettracker(
            id INTEGER PRIMARY KEY,
            Date DATE,
            Description TEXT,
            Type TEXT,
            Category TEXT,
            Amount INT,
            Comments TEXT,
            FOREIGN KEY(Category) REFERENCES category(Category_Name)
            )''')  # creating database 
        
        self.db.commit()
        # FOREIGN KEY GO HERE
        if os.path.exists("initialised.txt"):
            pass

        else:   
            with open("initialised.txt", "w") as file:

                pass 
            # Above creates the file to avoid duplicates
            self.def_category_list = [
                ("Savings", 0),
                ("Groceries", 0),
                ("Utilities", 0),
                ("Health", 0),
                ("Insurance", 0),
                ("Transportation", 0),
                ("Clothing", 0),
                ("Cellphone and Internet", 0),
                ("Petrol/Diesel", 0),
                ("Housing", 0),
                ("Main Job", 0),
                ("Side Hustle", 0)
                ]

            self.cursor.executemany('''
                INSERT OR IGNORE INTO category(Category_Name, Budget)
                VALUES (?, ?)
                ''', self.def_category_list)

            
            self.db.commit()
            
            dummy_entries = [
                ("2024-01-05", "Salary", "Income", "Main Job", 15000, 
                 "January salary from main job"),
                ("2024-02-14", "Groceries", "Expense", "Groceries", -1200, 
                 "Weekly grocery shopping"),
                ("2024-03-10", "Electricity Bill", "Expense", "Utilities", -900,
                  "Monthly electricity bill"),
                ("2024-04-05", "Health Insurance", "Expense", "Health", -2000, 
                 "Monthly health insurance payment"),
                ("2024-05-20", "Petrol", "Expense", "Petrol/Diesel", -800, 
                 "Fuel for the car"),
                ("2024-06-15", "Freelance Work", "Income", "Side Hustle", 3000, 
                 "Completed a graphic design project"),
                ("2024-07-01", "Rent", "Expense", "Housing", -7500, 
                 "Monthly apartment rent"),
                ("2024-08-10", "Clothing", "Expense", "Clothing", -1800, 
                 "Bought new work outfits"),
                ("2024-09-25", "Savings Deposit", "Expense", "Savings", -5000,
                  "Transferred to savings account"),
                ("2024-10-12", "Internet Bill", "Expense", 
                 "Cellphone and Internet", -700, 
                 "Monthly internet subscription"),
                ("2024-11-15", "Car Insurance", "Expense", "Insurance", -1200, 
                 "Quarterly car insurance payment"),
                ("2024-12-24", "Groceries", "Expense", "Groceries", -1400, 
                 "Christmas grocery shopping"),
                ("2024-01-20", "Phone Plan", "Expense", 
                 "Cellphone and Internet",  -500, "Monthly cellphone plan"),
                ("2024-03-30", "Public Transport", "Expense", "Transportation", 
                 -150, "Bus tickets for the month"),
                ("2024-04-15", "Medical Checkup", "Expense", "Health",
                  -600, "Annual health checkup"),
                ("2024-06-25", "Petrol", "Expense", "Petrol/Diesel",
                  -900, "Filled up the tank"),
                ("2024-09-05", "Salary", "Income", "Main Job", 
                 15000, "September salary from main job"),
                ("2024-10-30", "Utilities", "Expense", "Utilities", 
                 -1000, "Monthly water and electricity bill"),
                ("2024-11-18", "Groceries", "Expense", "Groceries",
                  -1100, "Weekly grocery shopping"),
                ("2024-12-10", "Side Gig", "Income", "Side Hustle", 
                 4000, "Income from tutoring students"),
                    ]
                  
            self.cursor.executemany('''
                INSERT OR IGNORE INTO budgettracker(Date,Description,Type,Category,Amount,Comments)
                VALUES(?,?,?,?,?,?)
                ''', dummy_entries)
            
            self.db.commit()

            self.def_category_list.sort()

        self.menu_selection()
    
    def loading_screen(self):
        for i in tqdm(range(5)):
            time.sleep(0.2)

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
    def print_category_list(self):
        self.cursor.execute('''
        SELECT Category_Name from category
        ORDER BY Category_Name ASC
        ''')

        db_category_list = self.cursor.fetchall()

        return db_category_list


    def menu_selection(self):
        time.sleep(2)

        menu_dictionary = {
			1: self.add_expense,
			2: self.view_expenses,
			3: self.view_expenses_by_category,
			4: self.add_income,
			5: self.view_income,
			6: self.view_income_by_category,
			7: self.add_a_category,
            8: self.delete_a_category,
			9: self.set_budget_for_a_category,
			10: self.view_budget_for_category,
			11: self.set_financial_goals,
			12:self.view_progress_towards_financial_goals,
			13:self.quit_app,
			14:self.delete_account

			} # dictionary holding all the functions from the menu

        while True:  # ensuring user choses an option thats possible 

            try:
                menu_num_selection = int(input('''
                    1.Add expense
                    2.View expenses 
                    3.View expenses by category 
                    4.Add income
                    5.View income
                    6.View income by category 
                    7.Add a category
                    8.Delete a category
                    9.Set budget for a category 
                    10.View budget for category 
                    11.Set financial goals
                    12.View progress towards financial goals
                    13.Quit 
                    14.Delete Account
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
        # creating neater output. Need to create it so that it works everytime when displaying the db too 
        self.loading_screen()
        self.clear_screen()
   
        headers = ["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]

        table = tabulate(zip(headers,rows), headers= ["Information", "Your Input"], tablefmt = "fancy_grid")
        print(table)


    def create_table_with_own_headers(self,headers, rows):
        # neater output 
        self.loading_screen()
        self.clear_screen()
        table = tabulate(rows, headers= headers, tablefmt = "fancy_grid")
        print(table)


    def add_expense(self):
        while True:

            temp_date = input('''Please enter the date of the transaction ie yyyy-mm-dd: >>''')
            
            temp_description = input('''Please give the transaction a name: >>''')

            temp_type = 'Expense'

            db_category_list = self.print_category_list()
         
            while True:
                for index, value in enumerate(db_category_list,start=1):
                    print(f"{index}. {value[0]}")

                try: 
                    category_selection = int(input("Please select a category ie 3: "))

                    if(category_selection > len(db_category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")

            selected_category  = db_category_list[category_selection-1]

            temp_amount = float(input('''How much was spent ie R120.05? >> -R'''))*-1
            
            temp_comments = input('''Please enter any comments you have about this transaction: >>''')

            # creating table for better visibility 
            
            rows = [temp_date, temp_description,temp_type,selected_category[0],temp_amount,temp_comments]
            self.create_table(rows)

            # validating input
            correct_info = input("Please confirm if the following is correct[Y/n]:").lower()
            print(f'Your response: {correct_info}')

            # alidating if the details entered are correct
            if correct_info != 'y' and correct_info != 'n':
                self.create_table(rows)
                correct_info = input("Incorrect option chosen.Please confirm if the following is correct[Y/n]:").lower().strip()
                print(f'Your response: {correct_info}')    
            elif correct_info == 'y':
                print("Input Valid!")
            
                # adding entry into database
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

        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", 
            "Comments"]
        
        self.create_table_with_own_headers(headers ,list_expenses)
        time.sleep(2)
        self.menu_selection()
        

    def view_expenses_by_category(self):
        db_category_list = self.print_category_list()
      
        while True:
                for index, value in enumerate(db_category_list, start=1):
                    print(f"{index}. {value[0]}")

                try: 
                    category_selection = int(input("Please select a category to view ie 3: "))

                    if(category_selection > len(db_category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")

 
        self.cursor.execute('''
            SELECT * 
            FROM budgettracker
            WHERE Category = ? AND Type = 'Expense'
            ORDER BY Date
            ''', db_category_list[category_selection-1] )
        
        list_incomes = self.cursor.fetchall()
       
        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers,list_incomes)
        time.sleep(2)
        self.menu_selection()
        

    def add_income(self):
        while True:

            temp_date = input('Please enter the date of the transaction ie yyyy-mm-dd: >>')
            
            temp_description = input('Please give the transaction a name: >>')

            temp_type = 'Income'

            db_category_list = self.print_category_list()
         
            while True:
                for index, value in enumerate(db_category_list,start=1):
                    print(f"{index}. {value[0]}")

                try: 
                    category_selection = int(input("Please select a category ie 3: "))

                    if(category_selection > len(db_category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break 

                except ValueError:
                    print("You have chosen the incorrect option")

            selected_category  = db_category_list[category_selection-1]


            temp_amount = float(input('How much was recieved ie R120.05? >> R'))
                 
            temp_comments = input('Please enter any comments you have about this transaction: >>')

            # creating table for better visibility 
            rows = [temp_date, temp_description,temp_type, selected_category[0],temp_amount,temp_comments]
            self.create_table(rows)

            # validating input
            correct_info = input("Please confirm if the following is correct[Y/n]:").lower()
            print(f'Your response: {correct_info}')

            # validating if the details entered are correct
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

        db_category_list = self.print_category_list()
      
        while True:
                for index, value in enumerate(db_category_list, start=1):
                    print(f"{index}. {value[0]}")

                try: 
                    category_selection = int(input("Please select a category to view ie 3: "))

                    if(category_selection > len(db_category_list)) or category_selection < 1:
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
            ''', db_category_list[category_selection-1] )
        
        list_incomes = self.cursor.fetchall()

        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers,list_incomes)
        time.sleep(2)
        self.menu_selection()
        

    def add_a_category(self):

        while True:
            db_category_list = self.print_category_list()

            print("==Current Categories==")

            for index, value in enumerate(db_category_list, start =1):
                print(f"{index}. {value[0]}")
   
            new_category = input("Please enter a new category: >> ")
        
            for  i in db_category_list:
                if new_category.lower() == i[0].lower():
                    print("That category already exisits. ")
                    self.menu_selection()
            else:       
                budget = int(input(f"What is the monthly budget for {new_category.capitalize()}:>> R"))     
                self.cursor.execute('''
                    INSERT OR IGNORE INTO category(Category_Name, Budget)
                    VALUES (?,?)
                    ''', (new_category.capitalize(), budget))
                self.db.commit()
        
            time.sleep(1)
            self.menu_selection()

    def delete_a_category(self):
        db_category_list = self.print_category_list()

        for i, value in enumerate(db_category_list, start=1):
            print(f"{i}. {value[0]}")

        while True:
            try: 
                del_category_selection = int(input("Which category do you want to delete ie. 2: >> "))

                if del_category_selection > len(db_category_list) or del_category_selection < 1:
                    print("Incorrect selection")
                else:
                    break
            except ValueError:
                print("Incorrect input. Please try again")
        
        print(db_category_list[del_category_selection-1][0])

        self.cursor.execute(''' 
            DELETE FROM category
            WHERE Category_Name = ?
                            ''', (db_category_list[del_category_selection-1][0],))
        self.db.commit()


       


    def set_budget_for_a_category(self):
        print("ENTERING set_budget_for_a_category")
       
        while True:
            try: 
                budget_option_1 = int(input(
                    '''Would you like to:
                    1. Set budget for all your categories
                    2. Set budget for a specifc category
                        >>'''))
                
                if budget_option_1 == 1:
                    self.cursor.execute('''SELECT Category_Name, Budget FROM category''')
                    categories_and_budget = self.cursor.fetchall()
                    print(categories_and_budget)
                    for i in range(len(categories_and_budget)):
                        print(f"Category: {categories_and_budget[i][0]} Current Budget: R{categories_and_budget[i][1]}")

                        table = tabulate([categories_and_budget[i]],
                                        headers = ["Category",
                                        "Current Budget"],
                                        tablefmt="fancy_grid")
                        print(table)
                        while True:
                            try:
                                new_budget_amount = int(input(">>Please enter a new budget amount: R"))
                                if new_budget_amount < 0: 
                                    new_budget_amount   = new_budget_amount * -1
                                break
                            except ValueError:
                                print("Please try again.")

                        self.cursor.execute('''
                                UPDATE category 
                                SET Budget = ?
                                WHERE Category_Name = ?
                                    ''', (new_budget_amount, categories_and_budget[i][0]))
                        self.db.commit()
                    self.menu_selection()
          
                else:
                    if budget_option_1 == 2:
                        print(("======== Your current categories ========="))

                        self.cursor.execute('''SELECT Category_Name, Budget FROM category''')
                        categories_and_budget = self.cursor.fetchall()
                
                        table = tabulate(categories_and_budget, 
                        headers = ["Category Name", "Budget"], tablefmt= 
                        "fancy_grid", showindex=range(1, len(categories_and_budget)+1))
                        print(table)
                        

                        while True:
                            try:
                                set_selection = int(input("Which budget would you like to set? ie 4: >>"))

                                if set_selection > len(categories_and_budget) or set_selection < 1:
                                    print("Incorrect value chosen")
                                else: 
                                    try:
                                        new_budget_amount = float(input("Please enter a new budget amount: >>R "))
                                        break
                                    except ValueError:
                                        print("Unknown value added")
                            except ValueError:
                                print("Incorrect option selected")
                        
                        print(f"{categories_and_budget[set_selection-1][0]} new budget is R{new_budget_amount}")

                        self.cursor.execute(''' 
                            UPDATE category 
                            SET Budget = ? 
                            WHERE Category_Name = ?''', (new_budget_amount,categories_and_budget[set_selection-1][0]))
                        self.db.commit()
                        self.menu_selection()


            except ValueError:
                print("Incorrect option selected. Please try again")
        
        


    def view_budget_for_category(self):
        print("ENTERING view_budget_for_category")

        self.cursor.execute('''
                            SELECT Category_Name, Budget
                            FROM category
                            ''')
        
        categories_and_budget = self.cursor.fetchall()
        print(categories_and_budget)

        for i, value in enumerate(categories_and_budget, start=0):
            print(f"{i+1}. {categories_and_budget[i][0]}")
        
        while True:
            try:
                view_category_selection = int(input("Which category would you like to view ie 3: "))

                if view_category_selection > len(categories_and_budget) or view_category_selection < 1:
                    print("Incorrect selection. Please try again")
                else:
                    break
            except ValueError:
                print("Incorrect option selected")

        table = tabulate([[categories_and_budget[view_category_selection-1][0],categories_and_budget[view_category_selection-1][1]]],
                        headers = ["Category", "Budget"], tablefmt="fancy_grid" )
        print(table)

        self.menu_selection()
        




        
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
     


    def delete_account(self):
        confirm_delete = input("You are about to permenatley delete your account! Are you sure [Y/n]: ").lower()

        if confirm_delete == 'n':
            print("ABORTING DELETION")
            self.menu_selection()

        elif confirm_delete == 'y':

            print("Deleting in progress...")

            self.loading_screen()

            self.cursor.execute('''
                DROP TABLE budgettracker
                    ''')
            
            self.db.commit()

            self.db.close()

            if os.path.exists("initialised.txt"):
                os.remove("initialised.txt")
                os.remove("budgettracker.db")
                print("Deleting Complete")
                exit()
            else: 
                pass
        else: 
            print("Incorrect option selected. Returning to main menu...")
            self.menu_selection()
           
# Code starts here
new_year_resolution = menuSelection()
new_year_resolution.menu_selection()