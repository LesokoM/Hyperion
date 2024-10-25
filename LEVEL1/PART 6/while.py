
user_input_history = []

not_neg1 = True
while not_neg1:
    user_input = int(input("Enter a number: "))
    if user_input== -1:
        print("User input is: ", user_input_history)
        print("The average is:", sum(user_input_history)/len(user_input_history))
        not_neg1 = False
    user_input_history.append(user_input)
    