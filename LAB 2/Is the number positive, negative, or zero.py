#Write a Python script that prompts the user to input a number. The program should then
#output the number and a message saying whether the number is positive, negative, or
#zero.

x=int(input("Add your value: "))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")
