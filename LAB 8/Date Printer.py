#Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It
#should print the date in the form March 12, 2012.
    

def format_date(date_str):
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    parts = date_str.split('/')
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    formatted_date = months[month - 1] + " " + str(day) + ", " + str(year)
    return formatted_date

date_str = input("Enter a date in the format mm/dd/yyyy: ")
formatted_date = format_date(date_str)
print("Formatted date:", formatted_date)
