import sqlite3
from prettytable import PrettyTable\

def PrintTable(cursorvariable):
    '''
    Function to print table in a neater fashion
    '''
    print("----PYTHON PROGRAMMING-----")
    myTable = PrettyTable(["ID", "NAME", "GRADE"])

    for i in range(len(cursorvariable)):
        for j in range(1):
            myTable.add_row([cursorvariable[i][j],cursorvariable[i][j+1],cursorvariable[i][j+2]])

    print(myTable)





db = sqlite3.connect('python_programing_db.db')

cursor = db.cursor()


cursor.execute('''
               CREATE TABLE IF NOT EXISTS python_programming(
               id INTEGER PRIMARY KEY, -- ID must be unique so we dont have duplicates
               name TEXT,
               grade INTEGER
               
               )  
               ''')

db.commit()

start_up_info = [
    (55,'Carl Davis', 61),
    (66,'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
    ] # List of  tuples 

cursor.executemany('''
                   INSERT OR IGNORE INTO python_programming(id,name,grade) -- Ensuring there are no duplicates
                   -- Using OR IGNORE ensures we can avoid errors if there is a dup id
                   VALUES(?,?,?)
                  ''', start_up_info)

db.commit()

cursor.execute('''
               SELECT * FROM python_programming
               ''')

PrintTable(cursor.fetchall())




print("Who got between 60 and 80")
cursor.execute('''
    SELECT id,name,grade FROM python_programming 
    WHERE grade>=? AND grade<=?
    ''', (60,80,))

grades_between_60_and_80 = cursor.fetchall()

for i in grades_between_60_and_80:
    print(f'ID: {i[0]} Name and Surname: {i[1]}')

cursor.execute('''
    UPDATE python_programming
    SET grade = 65
    WHERE name =? OR id =?
            ''', ('Carl Davis', 55,))

db.commit()


cursor.execute('''
            SELECT * FROM python_programming
            WHERE id =? 
               ''', (55,))
PrintTable(cursor.fetchall())
print("GRADE UPDATED SUCCESSFULLY")


cursor.execute('''
            DELETE  FROM python_programming 
            WHERE name =? or id =?
               ''',('Dennis Fredrickson',66))

db.commit

cursor.execute('''
                SELECT * FROM python_programming
               ''')
PrintTable(cursor.fetchall())
print("USER REMOVED SUCCESSFULLY")

cursor.execute('''
               UPDATE python_programming
               SET grade = 80
               WHERE id>?
               ''',(55,))

db.commit()

cursor.execute('''
                SELECT * FROM python_programming
               ''')
PrintTable(cursor.fetchall())
print("GRADES UPDATED SUCCESSFULLY")

db.close()