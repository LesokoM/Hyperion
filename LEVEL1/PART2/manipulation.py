str_manip = input("Enter a sentence: ")
len_manip = len(str_manip)
print(len_manip)

last_letter = str_manip[-1]

print(str_manip.replace(last_letter,"@"))

print(str_manip[-1:-4:-1])


my_5_letter_word = str_manip[0:3] + str_manip[-2] +str_manip[-1]


print(my_5_letter_word)