#A cookie recipe calls for the following ingredients:
#• 1.5 cups of sugar
#• 1 cup of butter
#• 2.75 cups of flour
#The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the
#user how many cookies he or she wants to make, then displays the number of cups of each
#ingredient needed for the specified number of cookies
def calculate_ingredient_amounts(cookies_wanted):
    cookies_produced = 48
    sugar_per_cookie = 1.5 / cookies_produced
    butter_per_cookie = 1 / cookies_produced
    flour_per_cookie = 2.75 / cookies_produced

    sugar_needed = sugar_per_cookie * cookies_wanted
    butter_needed = butter_per_cookie * cookies_wanted
    flour_needed = flour_per_cookie * cookies_wanted

    return sugar_needed, butter_needed, flour_needed

def main():
    try:
        cookies_wanted = int(input("Enter the number of cookies you want to make: "))
        if cookies_wanted <= 0:
            raise ValueError("Number of cookies should be a positive integer.")
    except ValueError as e:
        print("Invalid input. Please enter a positive integer for the number of cookies.")
        return

    sugar_needed, butter_needed, flour_needed = calculate_ingredient_amounts(cookies_wanted)

    print("For", cookies_wanted, "cookies, you'll need:")
    print(sugar_needed, "cups of sugar")
    print(butter_needed, "cups of butter")
    print(flour_needed, "cups of flour")

if __name__ == "__main__":
    main()
