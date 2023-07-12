#Write a Python script to find the area and perimeter of a rectangle. The user provides the
#input for the length and width of the rectangle.

def function(x, y,):
    area = x * y
    perimeter = 2 * x + 2 * y
    print("The area is:", area)
    print("The perimeter is:", perimeter)

x = int(input("Input length: "))
y = int(input("Input width: "))

function(x, y)
