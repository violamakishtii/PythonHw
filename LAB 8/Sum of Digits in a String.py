#Write a program that asks the user to enter a series of single-digit numbers with nothing
#separating them. The program should display the sum of all the single digit numbers in the string.
#For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1,
#and 4.

def calculate_sum_of_digits(number_str):
    return sum(int(digit) for digit in number_str if digit.isdigit())

def main():
    number_str = input("Enter a series of single-digit numbers: ")
    result = calculate_sum_of_digits(number_str)
    print("The sum of single-digit numbers in the string is:", result)

main()

