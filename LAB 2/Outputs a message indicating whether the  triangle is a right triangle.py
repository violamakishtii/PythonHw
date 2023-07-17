#In a right triangle, the square of the length of one side is equal to the sum of the squares
#of the lengths of the other two sides. Write a Python script that prompts the user to enter
#the lengths of three sides of a triangle and then outputs a message indicating whether the
#triangle is a right triangle.

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
