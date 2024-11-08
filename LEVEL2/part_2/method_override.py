
class Adult():
    
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
       
         print(f"{self.name} can drive") 
       
class Child(Adult):

    def can_drive(self):
        print(f"{self.name} can't drive")

name,age,hair_colour,eye_colour = input('''Please enter the below information separated by commas:
        name
        age
        hair colour
        eye colour  
        >>> ''').replace(" ", "").split(",")#removing any spaces and seperating input with commas

if age >=18:
    me = Adult(name, age, hair_colour,eye_colour)
else: 
    me = Child(name, age, hair_colour,eye_colour)

me.can_drive()

