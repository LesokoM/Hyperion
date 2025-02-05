import sqlite3
from tabulate import tabulate




#starting_balance = int(input("What is your current balance? ie R12 000.50: R"))



class menuSelection():


    def __init__(self):
                
                
                print("CREATING DATABASE...")
                
                self.category_list = ["Savings", "Groceries","Utilites","Health","Insurance","Transportation","Clothing","Cellphone and Internet" , "Petrol/Diesel","Housing", "Main Job", "Side Hustle"]
                self.category_list.sort()
                
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
                
                
                #add dummy entires here


                self.menu_selection()

        


    def menu_selection(self):

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
        print("creating table.....")
        headers = ["Date", "Desciption", "Type", "Category", "Amount(R)", "Comments"]

        table = tabulate(zip(headers,rows), headers= ["Information", "Your Input"], tablefmt = "fancy_grid")
        print(table)


    def create_table_with_own_headers(self,headers, rows):
    #neater output 
        print("creating table with your headers.....")
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
        print("ENTERING view_expenses")

        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Type = 'Expense'
                            ORDER BY Date
                            ''')
        list_expenses = self.cursor.fetchall()
        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
        self.create_table_with_own_headers(headers,list_expenses)
        self.menu_selection()
        







    def view_expenses_by_category(self):
        print("ENTERING view_expenses_by_category")

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
        print("ENTERING view_income")
         
        
        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Type = 'Income'
                            ORDER BY Date
                            ''')
        list_income = self.cursor.fetchall()
        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]


        self.create_table_with_own_headers(headers,list_income)
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

    
        print(self.category_list[category_selection-1])
        self.cursor.execute('''
                            SELECT * 
                            FROM budgettracker
                            WHERE Category = ? AND Type = 'Income'
                            ORDER BY Date
                            ''', (self.category_list[category_selection-1],) )
        
        list_incomes = self.cursor.fetchall()

        headers = ["Date", "Desciption", "Type","Category", "Amount(R)", "Comments"]
       
        self.create_table_with_own_headers(headers,list_incomes)
        self.menu_selection()
        
    def add_a_category(self):
        print("adding a category")
        pass
    
    def set_budget_for_a_category(self):
        print("ENTERING set_budget_for_a_category")
        pass
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
        print("ENTERING delete_sccount")
        pass


    


    


#####################################
menuSelection()
       







