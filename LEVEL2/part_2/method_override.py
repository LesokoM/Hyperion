
class Adult():
    while True: 
        try:
            name,age,hair_colour,eye_colour = input('''Please enter the below information separated by commas:
            name
            age
            hair colour
            eye colour  
            >>> ''').replace(" ", "").split(",")

            age = int(age)
            break

        except:
            print("Please enter information in correct format ")

    def can_drive(self):
        print(f"Driver Name: {self.name}")
        if self.age >= 18:
            print(f"{self.name} can drive")
        else:
            print(f"{self.name} can't drive")

class Child(Adult):

    def category(self):
        if self.age >=18:
            person = Adult()
            person.can_drive()
        else:
            person = Child()
            person.can_drive()

me = Child()
me.category()

