#Prompt the user to input the shape type (rectangle, circle, or cylinder) and the appropriate
#dimension of the shape. The Python script then outputs the following information about
#the shape:
#For a rectangle, it outputs the area and perimeter; for a circle, it outputs the area and
#circumference; and for a cylinder, it outputs the volume and surface area.

user=input("Hello welcome,please if your shape type is rectangle input r,if it is circle ci or cylinder cy")
if user=="r":
    a=int(input("Please add your first value"))
    b=int(input("Please add your second value"))
    area = a*b
    perimeter = 2*a + 2*b
    print("Area is:",area,"\nPerimeter is:",perimeter)
elif user=="ci":
    r=int(input("Please add radius:"))
    area=3.14*r*r
    circ=2*3.14*r
    print("Area is:",area,"\nCircumfence is:",circ)
elif user=="cy":
    r=int(input("Please add your given radius:"))
    h=int(input("Please add your given height:"))
    volume=3.14*r*r*h
    sarea=2*3.14*r*r+2*3.14*r*h
    print("Volume is:",volume,"\nSurface area is:",sarea)
else:
    print("Wrong input please add either cy,ci or r")
