'''
Ask for user name store in name variable
Ask for user age store in age variable
Ask for user House number store in house_num variable
Ask for user street name store in street_name variable
then -print out user info 

'''

# Asking for user input and printing out input

name= input("What is your name? ")
age = input("What is your age? ")
house_num = input("What is your house number? ")
street_name = input("What is your street name? ")

# Printing out user input
print(f'''
      This is {name}. 
      She is {age} years old 
      {name} lives at house number {house_num} on {street_name}
    ''')