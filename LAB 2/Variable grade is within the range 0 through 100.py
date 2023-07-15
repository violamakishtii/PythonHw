#Write a Python script that prints the message “The number is valid.” if the variable grade
#is within the range 0 through 100.
grade = int(input("Input your number: "))

if grade >= 0 and grade <= 100:
    print("The number is valid.")
else:
    print("Invalid input.")
