#Magic Dates. The date June 10, 1960, is special because when we write it in the
#following format, the month times the day equals the year.
#6/10/60
#Write a program that asks the user to enter a month (in numeric form), a day, and a two-
#digit year. The program should then determine whether the month times the day is equal
#to the year. If so, it should display a message saying the date is magic. Otherwise, it
#should display a message saying the date is not magic.

month = input("Add mm")
date = input("Add dd")
year = input("Add yy")

equation = int(month)*int(date)

if equation == int(year):
    print("mAGICC")
else:
    print("Not magic")
