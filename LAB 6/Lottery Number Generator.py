# Design a program that generates a seven-digit lottery number.
# The program should generate seven random numbers, each in the range of 0 through 9,
# and assign each number to a list element.

import random

# Generate a list of seven random digits between 0 and 9
lottery_number = [random.randint(0, 9) for _ in range(7)]

# Display the contents of the list
print(f"Lottery Number: {lottery_number}")
print("Lottery Number:", *lottery_number)
