#A “sleep debt” represents the difference between a person’s desirable and actual
#amount of sleep. Write a program that prompts the user to enter how many hours they slept each
#day over a period of seven days. Using 8 hours per day as the desirable amount of sleep, determine
#their sleep debt by calculating the total hours of sleep they got over the seven-day period and
#subtracting that from the total hours of sleep they should have got. If the user does not have a sleep
#debt, display a message expressing your jealousy.

def main():
    desirable_sleep = 8  # hours

    # Get the hours of sleep for each day of the week
    weekly_sleep = []
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        hours_slept = float(input(f"How many hours did you sleep on {day}? "))
        weekly_sleep.append(hours_slept)

    # Calculate the total hours of sleep over the seven-day period
    total_sleep = sum(weekly_sleep)

    # Calculate the sleep debt
    sleep_debt = (7 * desirable_sleep) - total_sleep

    # Display the results
    print("Total hours of sleep over the week:", total_sleep, "hours")
    print("Sleep debt:", sleep_debt, "hours")

    if sleep_debt <= 0:
        print("No sleep debt! I'm jealous.")
    else:
        print("You have a sleep debt. Get some rest!")

if __name__ == "__main__":
    main()
