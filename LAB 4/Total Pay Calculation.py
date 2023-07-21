#Write a Python function to compute the total pay given to an employee, which is a product of the
##hourly rate times the hours worked. Do note that the employee will be paid 1.5 times the hourly
#rate for hours worked above 40 hours (overtime). Create a function called computepay which
#takes two parameters (hours and rate).

def computepay(h,r):
    total_pay=int(h)*int(r)
    if h>40:
        overtime=total_pay*1.5
        print("Total pay is",overtime)
    else:
        print("Total pay is",total_pay)

h=int(input("Write hours worked"))
r=int(input("Input hourly rates"))

computepay(h,r)
