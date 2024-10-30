
class Adult():
    while True: 
        try: #taking in input and making sure its correct
            name,age,hair_colour,eye_colour = input('''Please enter the below information separated by commas:
            name
            age
            hair colour
            eye colour  
            >>> ''').replace(" ", "").split(",")#removing any spaces and seperating input with commas

            age = int(age) #making sure age is an int
            break#breaking loop if all info is correct

        except:#if user does not enter using correct fomat
            print("Please enter information in correct format ")

    def can_drive(self):
        print(f"Name: {self.name}")
        if self.age >= 18:#determining age of user
            print(f"{self.name} can drive") #older than 18 can drive
        else:
            print(f"{self.name} can't drive") #younger than 18 cant drive

class Child(Adult):

    def category(self):#creating function to check driving age
        if self.age >=18:
            person = Adult()
            person.can_drive()
        else:
            person = Child()
            person.can_drive()

me = Child()
me.category()

