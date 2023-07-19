#The area of a rectangle is the rectangle’s length times its width. Write a program that asks
#for the length and width of two rectangles. The program should tell the user which
#rectangle has the greater area, or if the areas are the same.

a=int(input("Please input the length of rectangle 1"))
b=int(input("Please input the width of rectangle 1"))
c=int(input("Please input the length of rectangle 2"))
d=int(input("Please input the width of rectangle 2"))

if a*b > c*d:
    print("Rectangle one has a greater area")
elif a*b<c*d:
    print("Rectangle two has a greater area")
elif a*b==c*d:
    print("Both rectangles have the same area")
else:
    print("Invalid input")
