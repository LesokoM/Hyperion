import sqlite3
from tabulate import tabulate
import os
from tqdm import tqdm
import time
from datetime import datetime


class menuSelection():
    def __init__(self):
        """ Constuructor method. 
        Creates a instance of the menuSelection class and creates
        the databases where the data will be stored
        """
        self.loading_screen()

        # links us to the database
        self.db = sqlite3.connect('budgettracker.db')
        self.cursor = self.db.cursor()

        # creating the database
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
            )''')
 
        self.db.commit()

        # Above creates the file to avoid duplicates
        if os.path.exists("initialised.txt"):
            pass
        else:
            with open("initialised.txt", "w") as file:
                pass
         
            # creating our category list with the budget
            self.def_category_list=[
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
                ("Side Hustle", 0),
                ("Debts", 0)]

            self.cursor.executemany('''
                INSERT OR IGNORE INTO category(Category_Name, Budget)
                VALUES (?, ?)
                ''', self.def_category_list)
            
            self.db.commit()

            # Setting budget for each category

            print("LETS SET OUR FINANCIAL GOALS...")
          
            time.sleep(1)

            self.cursor.execute('''SELECT Category_Name,Budget
                                FROM category''')

            categories_and_budget=self.cursor.fetchall()

            for i in range(len(categories_and_budget)):
                print(f"Category: {categories_and_budget[i][0]} Current Budget: R{categories_and_budget[i][1]}")

                table=tabulate([categories_and_budget[i]],
                    headers=["Category", "Current Budget"],
                    tablefmt="fancy_grid")
                
                print(table)
                while True:
                    try:
                        new_budget_amount=int(input(">>Please enter a new budget amount: R"))
                        if new_budget_amount < 0:
                            new_budget_amount  =new_budget_amount * -1
                        break
                    except ValueError:
                        print("Please try again.")

                self.cursor.execute('''
                        UPDATE category
                        SET Budget=?
                        WHERE Category_Name=?
                            ''', (new_budget_amount, categories_and_budget[i][0]))
            self.db.commit()
          
        self.menu_selection()
    
    def date_validation(self, input_date):
        """Validates if the input_date is in 'YYYY-MM-DD' format."""

        try:
            entry_date=datetime.strptime(input_date, "%Y-%m-%d")
        
            return True
        except ValueError:
            print("Incorrect date entry. Please try again")
            
            return False
        
    def loading_screen(self):
        """Creates a loading screen effect"""

        for i in tqdm(range(5)):
            time.sleep(0.2)

    def clear_screen(self):
        """Clears the screen for better visibility"""

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
    def print_category_list(self):
        """Prints the category list for ease of access"""

        self.cursor.execute('''
        SELECT Category_Name from category
        ORDER BY Category_Name ASC
        ''')

        db_category_list=self.cursor.fetchall()

        return db_category_list
    
    def menu_selection(self):
        """function that calls the menu"""

        time.sleep(2)

        # dictionary holding all the functions from the menu
        menu_dictionary={
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
            11: self.view_progress_towards_financial_goals,
            12: self.quit_app,
            13: self.delete_account
            }

        # ensuring user choses an option thats possible
        while True:

            try:
                menu_num_selection=int(input('''
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
                    11.View progress towards financial goals
                    12.Quit
                    13.Delete Account
                    >> '''))
                
                if menu_num_selection > len(menu_dictionary) or menu_num_selection < 1:
                    print("Incorrect option selection")
                else:
                    break
            except ValueError:
                print("You have not entered a correct value")

        menu_dictionary[menu_num_selection]()

    def create_table(self, rows):
        """Creates table output for improved readability """

        self.loading_screen()
        self.clear_screen()
   
        headers=["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]

        table=tabulate(zip(headers, rows), headers=["Information", "Your Input"], tablefmt="fancy_grid")
        print(table)

    def create_table_with_own_headers(self, headers, rows):

        """Creates table output with own headers for improved readability"""
      
        self.loading_screen()
        self.clear_screen()
        table=tabulate(rows, headers=headers, tablefmt="fancy_grid")
        print(table)

    def add_expense(self):

        """Allows user to add an expense to the database"""
        while True:
            while True:
                temp_date=input('''Please enter the date of the transaction ie yyyy-mm-dd: >>''')
                is_date_correct=self.date_validation(temp_date)
                if is_date_correct:
                    break
            
            temp_description=input('''Please give the transaction a name: >>''')

            temp_type='Expense'

            db_category_list=self.print_category_list()
         
            while True:
                for index, value in enumerate(db_category_list, start=1):
                    print(f"{index}. {value[0]}")

                try:
                    category_selection=int(input("Please select a category ie 3: "))

                    if (category_selection > len(db_category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break

                except ValueError:
                    print("You have chosen the incorrect option")

            selected_category=db_category_list[category_selection-1]

            temp_amount=float(input('''How much was spent ie R120.05? >> -R'''))*-1
            
            temp_comments=input('''Please enter any comments you have about this transaction: >>''')

            # creating table for better visibility
            
            rows=[temp_date, temp_description,temp_type,selected_category[0],temp_amount,temp_comments]
            self.create_table(rows)

            while True:
                correct_info=input("Please confirm if the following is correct[Y/n]:").lower()
                if correct_info != 'y' and correct_info != 'n':
                    self.create_table(rows)
                elif correct_info == 'y':
                    self.cursor.execute('''
                        INSERT INTO budgettracker (Date, Description,Type, Category, Amount,Comments)
                            VALUES(?,?,?,?,?,?)''', rows)
                    self.db.commit()
                    
                    break
                elif correct_info == 'n':
                    self.menu_selection()
                else:
                    print("Incorrect input! Please re-enter... ")
            break

        self.menu_selection()

    def view_expenses(self):
        """Allows user to view all expenses"""
       
        self.cursor.execute('''
            SELECT *
            FROM budgettracker
            WHERE Type='Expense'
            ORDER BY Date
            ''')
        
        list_expenses=self.cursor.fetchall()

        headers=["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
        
        self.create_table_with_own_headers(headers, list_expenses)

        time.sleep(2)

        self.menu_selection()

    def view_expenses_by_category(self):
        """Allows user to view expenses based on desired category"""

        db_category_list=self.print_category_list()
      
        while True:
            for index, value in enumerate(db_category_list, start=1):
                print(f"{index}. {value[0]}")

            try:
                category_selection=int(input("Please select a category to view ie 3: "))

                if (category_selection > len(db_category_list)) or category_selection < 1:
                    print("Incorrect category selection please try again")
                else:
                    break

            except ValueError:
                print("You have chosen the incorrect option")

        self.cursor.execute('''
            SELECT *
            FROM budgettracker
            WHERE Category=? AND Type='Expense'
            ORDER BY Date ASC
            ''', db_category_list[category_selection-1] )
      
        list_incomes=self.cursor.fetchall()

        headers=["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers, list_incomes)
        time.sleep(2)
        self.menu_selection()

    def add_income(self):
        """Allows user to add income"""

        while True:
            while True:
                temp_date=input('''Please enter the date of the transaction ie yyyy-mm-dd: >>''')
                is_date_correct=self.date_validation(temp_date)

                if is_date_correct:
                    break
            
            temp_description=input('Please give the transaction a name: >>')

            temp_type='Income'

            db_category_list=self.print_category_list()
         
            while True:
                for index, value in enumerate(db_category_list, start=1):
                    print(f"{index}. {value[0]}")

                try:
                    category_selection=int(input("Please select a category ie 3: "))

                    if (category_selection > len(db_category_list)) or category_selection < 1:
                        print("Incorrect category selection please try again")
                    else:
                        break

                except ValueError:
                    print("You have chosen the incorrect option")

            selected_category=db_category_list[category_selection-1]

            temp_amount=float(input('How much was recieved ie R120.05? >> R'))
                 
            temp_comments=input('Please enter any comments you have about this transaction: >>')

            # creating table for better visibility
        
            rows=[temp_date, temp_description, temp_type, selected_category[0], temp_amount, temp_comments]
            self.create_table(rows)

            # validating if the details entered are correct

            while True:
                correct_info=input("Please confirm if the following is correct[Y/n]:").lower()
                if correct_info != 'y' and correct_info != 'n':
                    self.create_table(rows)
                elif correct_info == 'y':
                    self.cursor.execute('''
                                        INSERT INTO budgettracker (Date, Description, Type, Category, Amount, Comments)
                                        VALUES(?,?,?,?,?,?)''', rows)
                    self.db.commit() 
                    break
                elif correct_info == 'n':
                    self.menu_selection()
                else:
                    print("Incorrect input! Please re-enter... ")
            break
        self.menu_selection()

    def view_income(self):
        """Allows user to view all income"""

        self.cursor.execute('''
                            SELECT *
                            FROM budgettracker
                            WHERE Type='Income'
                            ORDER BY Date
                            ''')
        
        list_income=self.cursor.fetchall()

        headers=["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]

        self.create_table_with_own_headers(headers, list_income)

        time.sleep(2)

        self.menu_selection()
    
    def view_income_by_category(self):
        """Allows user to view income based on desired catergory"""

        db_category_list=self.print_category_list()
      
        while True:
            for index, value in enumerate(db_category_list, start=1):
                print(f"{index}. {value[0]}")

            try:
                category_selection=int(input("Please select a category to view ie 3: "))

                if (category_selection > len(db_category_list)) or category_selection < 1:
                    print("Incorrect category selection please try again")
                else:
                    break

            except ValueError:
                print("You have chosen the incorrect option")
 
        self.cursor.execute('''
            SELECT *
            FROM budgettracker
            WHERE Category=? AND Type='Income'
            ORDER BY Date
            ''', db_category_list[category_selection-1])
        
        list_incomes=self.cursor.fetchall()

        headers=["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers, list_incomes)

        time.sleep(2)

        self.menu_selection()
        
    def add_a_category(self):
        """Allows user to add category"""

        while True:
            db_category_list=self.print_category_list()

            print("==Current Categories==")

            for index, value in enumerate(db_category_list, start =1):
                print(f"{index}. {value[0]}")
   
            new_category=input("Please enter a new category: >> ")
        
            for i in db_category_list:
                if new_category.lower() == i[0].lower():
                    print("That category already exisits. ")
                    self.menu_selection()
            else:
                budget=int(input(f"What is the monthly budget for {new_category.capitalize()}:>> R"))
                self.cursor.execute('''
                    INSERT OR IGNORE INTO category(Category_Name, Budget)
                    VALUES (?,?)
                  
                    ''', (new_category.capitalize(), budget))
                self.db.commit()
        
            time.sleep(1)

            self.menu_selection()

    def delete_a_category(self):
        """Allows user to delete a category"""

        db_category_list=self.print_category_list()

        for i, value in enumerate(db_category_list, start=1):
            print(f"{i}. {value[0]}")

        while True:
            try:
                del_category_selection=int(input("Which category do you want to delete ie. 2: >> "))

                if del_category_selection > len(db_category_list) or del_category_selection < 1:
                    print("Incorrect selection")
                else:
                    break
            except ValueError:
                print("Incorrect input. Please try again")
        
        print(db_category_list[del_category_selection-1][0])

        self.cursor.execute('''DELETE FROM category
            WHERE Category_Name=?
                            ''', (db_category_list[del_category_selection-1][0],))
        self.db.commit()

    def set_budget_for_a_category(self):
        """Allows user to set a budget for a category"""

        while True:
            try:
                budget_option_1=int(input(
                    '''Would you like to:
                    1. Set budget for all your categories
                    2. Set budget for a specifc category
                        >>'''))
                
                if budget_option_1 == 1:
                    self.cursor.execute('''SELECT Category_Name, Budget FROM category''')
                    categories_and_budget=self.cursor.fetchall()
                  
                    for i in range(len(categories_and_budget)):
                        print(f"Category: {categories_and_budget[i][0]} Current Budget: R{categories_and_budget[i][1]}")

                        table=tabulate(
                            [categories_and_budget[i]],
                            headers=["Category", "Current Budget"],
                            tablefmt="fancy_grid"
                        )
                        
                        print(table)

                        while True:
                            try:
                                new_budget_amount=int(input(">>Please enter a new budget amount: R"))
                                if new_budget_amount < 0:
                                    new_budget_amount=new_budget_amount * -1
                                break
                            except ValueError:
                                print("Please try again.")

                        self.cursor.execute('''
                                UPDATE category
                                SET Budget=?
                                WHERE Category_Name=?
                                            
                                    ''', (new_budget_amount, categories_and_budget[i][0]))
                        self.db.commit()

                    self.menu_selection()
          
                else:
                    if budget_option_1 == 2:
                        print(("======== Your current categories ========="))

                        self.cursor.execute('''SELECT Category_Name, Budget FROM category''')
                        categories_and_budget=self.cursor.fetchall()
                
                        table=tabulate(categories_and_budget, 
                            headers=["Category Name", "Budget"], 
                            tablefmt="fancy_grid",
                            showindex=range(1, len(categories_and_budget)+1))

                        print(table)
                    
                        while True:
                            try:
                                set_selection=int(input("Which budget would you like to set? ie 4: >>"))

                                if set_selection > len(categories_and_budget) or set_selection < 1:
                                    print("Incorrect value chosen")
                                else:
                                    try:
                                        new_budget_amount=float(input("Please enter a new budget amount: >>R "))
                                        break
                                    except ValueError:
                                        print("Unknown value added")
                            except ValueError:
                                print("Incorrect option selected")
                        
                        print(f"{categories_and_budget[set_selection-1][0]} new budget is R{new_budget_amount}")

                        self.cursor.execute('''
                            UPDATE category
                            SET Budget=?
                            WHERE Category_Name=?''', (new_budget_amount, categories_and_budget[set_selection-1][0]))
                        self.db.commit()
                        
                        self.menu_selection()
            except ValueError:
                print("Incorrect option selected. Please try again")
        
    def view_budget_for_category(self):

        """Allows user to view budget for a category"""

        self.cursor.execute('''
                            SELECT Category_Name, Budget
                            FROM category
                            ''')
        
        categories_and_budget=self.cursor.fetchall()
       
        for i, value in enumerate(categories_and_budget, start=0):
            print(f"{i+1}. {categories_and_budget[i][0]}")
        
        while True:
            try:
                view_category_selection=int(input("Which category would you like to view ie 3: "))

                if view_category_selection > len(categories_and_budget) or view_category_selection < 1:
                    print("Incorrect selection. Please try again")
                else:
                    break
            except ValueError:
                print("Incorrect option selected")

        table=tabulate([[categories_and_budget[view_category_selection-1][0],categories_and_budget[view_category_selection-1][1]]],
                        headers=["Category", "Budget"], tablefmt="fancy_grid" )
        
        print(table)

        self.menu_selection()

    def view_progress_towards_financial_goals(self):
        """Allows user to view progress towards financial goals
        by comparing actual money spent/made to budgeted amount"""

        self.cursor.execute('''SELECT abs(sum(Amount))
                            FROM budgettracker
                            GROUP BY Category
                            ORDER BY Category ASC''')

        actuals=self.cursor.fetchall()
     
        # category headers
        self.cursor.execute('''SELECT Category
                            FROM budgettracker
                            GROUP BY Category
                            ORDER BY Category ASC''')

        headers=self.cursor.fetchall()

        # budgeted anounts
        self.cursor.execute('''SELECT Budget
                            FROM category
                            GROUP BY Category_Name
                            ORDER BY Category_Name ASC''')
        
        budget_amount=self.cursor.fetchall()
       
        # Creating a table that shows budgeted amount and actual
    
        edited_actuals=[]
        for i in range(0, len(actuals)):
            edited_actuals.append(actuals[i][0])

        edited_headers=[]
        for i in range(0, len(headers)):
            edited_headers.append(headers[i][0])

        edited_budget_amount=[]
        for i in range(0, len(budget_amount)):
            edited_budget_amount.append(budget_amount[i][0])

        goal_data=zip(edited_headers, edited_budget_amount, edited_actuals)

        progress_table=tabulate(goal_data, headers=["Category", "Budget", "Actual"], tablefmt="fancy_grid")

        print(progress_table)

        self.menu_selection()

    def quit_app(self):
        """Allows user to quit the app"""
        print("Goodbye...")
        exit()
     
    def delete_account(self):
        """Allows user to delete their account and remove all data"""

        confirm_delete=input("You are about to permenatley delete your account! Are you sure [Y/n]: ").lower()

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


new_year_resolution=menuSelection()

new_year_resolution.menu_selection()
