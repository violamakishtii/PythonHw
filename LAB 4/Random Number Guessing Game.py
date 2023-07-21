#Write a program that generates a random number in the range of 1 through 100 and asks the user
#to guess what the number is. If the user’s guess is higher than the random number, the program
#should display “Too high, try again.” If the user’s guess is lower than the random number, the
#program should display “Too low, try again.” If the user guesses the number, the application
#should congratulate the user and then generate a new random number so the game can start over.

#Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
#user makes. When the user correctly guesses the random number, the program should display the
#number of guesses.
import random

def random_guess_game():
    random_number = random.randint(1, 100)
    num_guesses = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        num_guesses += 1

        if user_guess < random_number:
            print("Too low, try again.")
        elif user_guess > random_number:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {num_guesses} guesses.")
            break


random_guess_game()
