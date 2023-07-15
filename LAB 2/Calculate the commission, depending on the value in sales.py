#Using the following chart, write a Python script to calculate the commission, depending
#on the value in sales.

def calculate_commission(sales):
    if sales >= 0 and sales <= 9999:
        commission = sales * 0.1
        print("Commission:", commission)
    elif sales > 9999 and sales <= 15000:
        commission = sales * 0.15
        print("Commission:", commission)
    elif sales > 15000: 
        commission = sales * 0.2
        print("Commission:", commission)
    else:
        print("INVALID INPUT")

sales = int(input("Enter the sales value: "))
calculate_commission(sales)
