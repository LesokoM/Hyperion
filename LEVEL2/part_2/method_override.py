
class Adult():
    
    def __init__(self, name, age, eye_colour, hair_colour): #creating object
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
       
         print(f"{self.name} can drive")  #setting can drive to print 
       
class Child(Adult):

    def can_drive(self):
        print(f"{self.name} can't drive") #if is a child then cant drive

name,age,hair_colour,eye_colour = input('''Please enter the below information separated by commas:
        name
        age
        hair colour
        eye colour  
        >>> ''').split(",")#removing any spaces and seperating input with commas

age = int(age)

if age >=18: 
    me = Adult(name, age,eye_colour,hair_colour)#creating adult if they can drive
else: 
    me = Child(name, age,eye_colour,hair_colour) #creating child if cant drive 

me.can_drive() #prining driving status

