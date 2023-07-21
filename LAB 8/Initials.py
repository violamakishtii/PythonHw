#Write a program that gets a string containing a person’s first, middle, and last names, and then
#display their first, middle, and last initials. For example, if the user enters John William Smith
#the program should display J. W. S.

def get_initials(full_name):
    return ' '.join(name[0].upper() + '.' for name in full_name.split())

# Get the full name from the user
full_name = input("Enter your first, middle, and last names: ")

# Get and display the initials
initials = get_initials(full_name)
print("Initials:", initials)
