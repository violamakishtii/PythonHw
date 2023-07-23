
# Ask the user to input a series of numbers separated by spaces
numbers_input = input("Enter a series of numbers separated by spaces: ")

# Split the input string into a list of individual numbers
numbers = [int(num) for num in numbers_input.split()]

res = []  # Initialize an empty list to store the squared results

for i in numbers:
    # Calculate square and add to the 'res' list
    res.append(i * i)

print("The squares of the numbers are:", res)
