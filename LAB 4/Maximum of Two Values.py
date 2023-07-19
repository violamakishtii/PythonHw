#Write a function named maximum that accepts two integer values as arguments and returns the
#value that is the greater of the two. For example, if 7 and 12 are passed as arguments to the
#function, the function should return 12. Use the function in a program that prompts the user to
#enter two integer values. The program should display the value that is the greater of the two.

def function(a,b):
    if a>b:
        print(a)
    else:
        print(b)
    

a=int(input("First no"))
b=int(input("Second no"))


function(a,b)
