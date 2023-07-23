#Design a program that asks the user to enter a series of 20 numbers. The program should store
#the numbers in a list and then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list
def main():
    numbers_list = []
    for i in range(20):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        numbers_list.append(num)

    lowest_number = min(numbers_list)
    highest_number = max(numbers_list)
    total = sum(numbers_list)
    average = total / len(numbers_list)

    print("The lowest number is:", lowest_number)
    print("The highest number is:", highest_number)
    print("The total of the numbers is:", total)
    print("The average of the numbers is:", average)

if __name__ == "__main__":
    main()
