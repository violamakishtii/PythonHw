# Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week
# and display the result.

def main():
    total_sales = 0

    # Get sales input for each day of the week
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        sales = float(input(f"Enter sales for {day}: "))
        total_sales += sales
        #total_sales=total_sales+sales

    # Display the result
    
    print(f"Total sales for the week: {total_sales}")

main()
