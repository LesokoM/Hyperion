# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax forgot quotation marks 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth } teeth"
#syntax forgot to use f in front of the quotation so that we can make use of f-strings 
#logical fmixed up number_of_teeth and animal_type placement in string 
print(full_spec)
#syntax forgot brackets for print function 
