name = []
birthdate = []
new_list  = []
f = open("DOB.txt", "r")

for line in f:
    line  = line.strip("\n") #remove the charcter \n before adding it to the list
    new_list.append(line.split(" "))

#sort list into appropriate list name or DOB (date of birth )

for i in range(0,len(new_list)):
    for j in range(0,5):
        if j <= 1 : 
            name.append(new_list[i][j])
        if j >=2:
            birthdate.append(new_list[i][j])




#NOW LETS PRINT IN CORRECT FORMAT

#PRINTING NAMES
'''
now names we know we only have 2 
names and surname so 0,1 and 2,3 and 4,5 and 6,7 

above tells me that after uneven number we do new line 
'''

print("     NAMES          ")
for i in range(0,len(name)-1):
     
        print(name[i] ,name[i+1], "\n")
    

print("     BIRTHDATE          ")
for i in range(0,len(birthdate)-2,3): #we have to skip 3 because of the way we are printing the list we have to jump to the date 
     
        print(birthdate[i] ,birthdate[i+1],birthdate[i+2], "\n")
    