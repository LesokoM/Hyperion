import sqlite3

class Menu():

    def __init__(self): 
         
            self.db = sqlite3.connect('ebookstore.db')
            self.cursor = self.db.cursor()

            # Creating the table 

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            qty INTEGER)
            ''')

            self.db.commit()

            # Now we popoulate the table 
            initial_books = [
            (3001,'A Tale of Two Citites','Charles Dickens', 30),
            (3002,'Harry Potter and the Philosopher\'s Stone','J.K. Rowling ',40),
            (3003,'The Lion, the Witch and the Wardrobe', 'C. S. Lewis',25),
            (3004,'The Lord of the Rings', 'J.R.R Tolkien ', 37),
            (3005, 'Alice in Wonderland','Lewis Carroll ',12)
            ]

            self.cursor.executemany('''
            INSERT OR IGNORE INTO book(id,title,author,qty)
            VALUES(?,?,?,?)
            ''', (initial_books))

            self.db.commit()


    def displayMenu(self):

        print('======Menu=======')
        print('|1. Enter book  |')
        print('|2. Update book |')
        print('|3. Delete book |')
        print('|4. Search books|')
        print('|0. Exit        |')
        print('-----------------')
        self.userChoice()
   
    def userChoice(self):
        while True:
            try:
                userChoice = int(input('Please select a menu option: '))
                if userChoice>4 or userChoice<0:
                    print("Incorrect option chosen please try again!")
                else:
                    break
            except ValueError:
                print("Incorrect option chosen please try again!")
        
        self.chosenOption(userChoice)

    
    def chosenOption(self, userChoice):

        if userChoice == 1:
            self.enterbook()
        elif userChoice == 2:
            self.updatebook()
        elif userChoice == 3:
            self.deletebook()
        elif userChoice == 4:
            self.searchbook()
        else:
            exit()

    def enterbook(self):
        print("== You're about to add a new book ==")

     

        while True:

            try:

                new_id = int(input("Please enter unique ID: "))
                new_title = input("Please enter the the title of the book: ")
                new_author = input(f"Please enter the author of {new_title}: ")
                new_qty = int(input("Please enter quantity of books: "))

                while True:
                    print(f'''
                    Please confirm if the following is correct:
                    ID: {new_id}
                    Title: {new_title}
                    Author: {new_author}
                    Quantity: {new_qty}     
                    ''')
                    correct_info = input("Y/N: ").upper()
              

                    if correct_info == "Y" or correct_info =="N":
                        if correct_info == "Y":
                            new_entry = (new_id,new_title,new_author,new_qty)
                            break
                        elif correct_info == "N":
                            raise ValueError
                    else:
                        print("Please re-confirm")
                break
            except ValueError:
                print("Incorrect entry please try again")


        new_entry_list = [new_entry]
        self.cursor.executemany('''
                            INSERT OR IGNORE INTO book(id,title,author,qty)
                            VALUES(?,?,?,?)
                            ''', new_entry_list
                            )
        self.db.commit()

        self.displayMenu()



    def updatebook(self):
        print("== You're about to update an exisiting book ==")
        pass
        #self.displayMenu()
    def deletebook(self):
        print("== You're about to delete a book ==")
        pass
        #self.displayMenu()
    def searchbook(self):
        print("== You're about to search for a book ==")
        pass
        #self.displayMenu()
    





    


myMenu = Menu()

myMenu.displayMenu()












