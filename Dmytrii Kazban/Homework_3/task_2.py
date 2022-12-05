number_to_guess = 8
number_to_enter = int(input("Enter the number"))


while number_to_enter != number_to_guess:
    if number_to_enter != number_to_guess:
        print("Try another number")
        number_to_enter = int(input("Enter the number"))
else:
        print("Congrats! You've guessed the number")
