
#Write a Python script that asks the user to enter two numbers. The program should use
#the conditional expression to determine which number is the smaller and which is the
#larger.

a=input("Please add ur first number")
b=input("Please add ur second number")

if a>b and b<a:
    print(a,"is the largest",b,"is smallest")
elif b>a and a<b:
     print(b,"is largest",a,"is smallest")
else:
     print("They are the same")
