import sqlite3

class Menu():

    def __init__(self): 
         
            self.db = sqlite3.connect('ebookstore.db')
            self.cursor = self.db.cursor()
            self.columnTitles = ["id", "title", "author", "qty"]

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
            print("Goodbye")
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
        while True:
            try:
                update_book = int(input("Please enter the ID of the book you'd like to update: "))
                
                # have to make sure the id exists 
                self.cursor.execute('''SELECT id FROM book''')
                id_list = self.cursor.fetchall()

                for i in range(len(id_list)):
                    if update_book == id_list[i][0]:
                        #book found
                        break
                else:
                    raise ValueError

                break
            except ValueError:
                print("You have not entered a valid ID")

        while True:
            update_column = int(input(
                        ''' 
                        What would you like to update?
                        1. ID
                        2. Title
                        3. Author
                        4. Quantity 

                        >>'''))
            if update_column > 4 or update_column < 1:
                print("Incorrect option chosen please try again")
                #valdating user option
            else: 
                break
        while True:
            try:

                    if update_column == 1:
                        new_id = int(input("Please enter unique ID: "))
                        updated_info = new_id
                        break
                    elif update_column == 2:
                        new_title = input("Please enter the the title of the book: ")
                        updated_info = new_title
                        break
                    elif update_column == 3:
                        new_author = input(f"Please enter the author of {new_title}: ")
                        updated_info = new_author
                        break
                    elif update_column == 4:
                        new_qty = int(input("Please enter quantity of books: "))      
                        updated_info = new_qty
                        break
            except ValueError:
                print("Incorrect entry please try again")     

        self.cursor.execute(f'''
                        UPDATE book 
                        SET {self.columnTitles[update_column-1]} = ?
                        WHERE id = ?

                        ''', ( updated_info ,update_book,))

        self.db.commit()
        self.displayMenu()


    def deletebook(self):
        print("== You're about to delete a book ==")

        while True:
            try:
                delete_book = int(input("Please enter the ID of the book you'd like to delete: "))
                
                # have to make sure the id exists 
                self.cursor.execute('''SELECT id FROM book''')
                id_list = self.cursor.fetchall()

                for i in range(len(id_list)):
                    if delete_book == id_list[i][0]:
                        #book found
                        break
                else:
                    raise ValueError

                break
            except ValueError:
                print("You have not entered a valid ID")

        self.cursor.execute('''
                        DELETE FROM book 
                        WHERE id = ?
                               ''', (delete_book,))

        print(f"You have successfully deleted book with ID: {delete_book}")
        self.db.commit()

        self.displayMenu()


    def searchbook(self):
        print("== You're about to search for a book ==")
        while True:
            try: 
                search_option  = int(input('''
                                Please enter your search option:
                                1. Search by ID
                                2. Search by Title
                                3. Search by Author
                                >> '''))
                if search_option > 3 or search_option < 1:
                    print("Incorrect option selected")
                else:
                    break
            except ValueError:
                print("Incorrect option selected")


        search_info = input(f"Please enter the {self.columnTitles[search_option-1]}: ")

        if search_option == 1:
            search_info = int(search_info)

        self.cursor.execute(f''' 
                        SELECT * FROM book 
                        WHERE {self.columnTitles[search_option-1]} = ?
                        ''',(search_info,))
        book_found = self.cursor.fetchall()

        print(f'''

                ID:     {book_found[0][0]}
                Title:  {book_found[0][1]}
                Author: {book_found[0][2]}
                Qty:    {book_found[0][3]}
        
        ''')

        self.displayMenu()

myMenu = Menu()
myMenu.displayMenu()












