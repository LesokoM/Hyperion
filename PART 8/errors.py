# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #syntax error missing brackerts
print ("\n") #syntax error incorrect indentation and no brackets 


    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #syntax wrong indentation and should be 
#1 equal sign to assign not compare and runtime error 
# where converting string to int when it should only be 24

age = int(age_Str) #syntax wrong indentation 
print("I'm" , age , "years old.") #syntax wrong indentation and should use , not + 



    # Variables declaring additional years and printing the total years of age
years_from_now = "3" #syntax wrong indentation 
total_years = age + int(years_from_now)
#syntax wrong indentation 
#runtime error years_from_now still seen as string needs to be converted to int

print("The total number of years:" ,  total_years ) 
#syntax missing the brackets for print
#also logical errors answer_years should be total_years 
#syntax total_years should not be in quotation marks as its a variable
#should use comma not + to print out the years 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 
#logical error total should be total_years 
print("In 3 years and 6 months, I'll be " , total_months+6 , " months old")
#syntax missing brackets for print and + shoud be commas 
#logical looking for 3 years and 6 months but only set years_from_now to 3 years so we need to add the 6 months

#HINT, 330 months is the correct answer
