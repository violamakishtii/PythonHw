#Write a Python script that asks the user to enter a number within the range of 1 through
#10. Use IF construct to display the Roman numeral version of that number.
#Input Validation: Do not accept a number less than 1 or greater than 10.
def convert_to_roman(num):
    roman_numerals = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X'
    }
    return roman_numerals[num]

# Ask the user to enter a number within the range of 1 through 10
number = int(input("Enter a number between 1 and 10: "))

# Validate the input
if number < 1 or number > 10:
    print("Invalid input. Number should be within the range of 1 through 10.")
else:
    # Convert the number to its Roman numeral version
    roman_numeral = convert_to_roman(number)
    print("The Roman numeral for", number, "is", roman_numeral, ".")

