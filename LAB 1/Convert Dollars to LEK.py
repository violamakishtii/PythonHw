#Write a Python script that will convert Dollars amounts to Leke. You can use the
#following conversion rate:
#1 USD= 105.40 Leke
def function(u):
    result=u * 105.4
    print("The result is:",result)


u = float(input("Input USD: "))

function(u)
