#Write a Python script to display the decimal value of a fraction. The user provides the
#input for the numerator and the denominator.

def function(n,d):
    result= n/d
    print("The result is:",float(result))



n = float(input("Input numerator: "))
d = float(input("Input denumerator: "))

function(n,d)
