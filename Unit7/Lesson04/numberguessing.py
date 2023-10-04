from random import randint

secret = randint(0, 20)

user_guess = input("Enter a number between 0 and 20:")
user_guess = int(user_guess)
number_of_guess = 1


while True:
    if user_guess == secret:
        print("Good job! You've picked the right number!")
        print("It took you", number_of_guess, "guesses")
        choice = input("Do you want to play again? (Enter YES to play again)")
        if choice == "YES":
            secret = randint(0, 20)
            user_guess = input("Enter a number between 0 and 20:")
            user_guess = int(user_guess)
            number_of_guess = 1
        else:
            print("Exiting, All Done")
            break
    elif user_guess == -1:
        print("Exiting, All Done")
        break
    else:
        if user_guess > secret:
            print("You guessed tp high.")
        elif user_guess < secret:
            print("You guessed to low.")
        user_guess = input("Enter a number between 0 and 20: Enter -1 to exit ")
        user_guess = int(user_guess)
        number_of_guess += 1