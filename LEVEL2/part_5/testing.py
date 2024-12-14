import sqlite3

db = sqlite3.connect('student_db.db')

cursor = db.cursor()

cursor.execute ('''
                CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY, 
                name TXT, 
                grade INTEGER)''')

db.commit()

name1 = "John"
grade1 = 50

name2 = "Melvin"
grade2 = 24

name3 = "Thando"
grade3 = 88

cursor.execute(''' 
               INSERT INTO student(name,grade)
               values(?,?)''', (name1, grade1))

print(f"{name1} has been added")

cursor.execute('''
               INSERT INTO student(name,grade)
               values(?,?)''', (name2,grade2))

print(f"{name2} has been added")

cursor.execute('''
               INSERT INTO student(name,grade)
               values(?,?)''', (name3,grade3))

print(f"{name3} has been added")

db.commit()

cursor.execute('''SELECT DISTINCT name FROM student WHERE grade<=?''', (60,))
student = cursor.fetchall()
student_names = []

for i in student:
    student_names.append(i[0])

print(student_names)

db.close()