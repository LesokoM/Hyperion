user_input = input("Enter a string: ")
new_string = ""
for i in range(0,len(user_input)):
    if i %2 ==0: 
        new_string += user_input[i].upper()
    if i %2 != 0:
        new_string += user_input[i].lower()

print(new_string)

new_string2 = user_input.split()
my_string = ""

for j in range(0,len(new_string2)):
    if j %2 ==0: 
        my_string+=new_string2[j].lower() + " "
       
    if j %2 != 0:
        my_string+=new_string2[j].upper() + " "
        


print(my_string)