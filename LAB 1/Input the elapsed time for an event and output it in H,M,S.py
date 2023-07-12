#Write a Python script that prompts the user to input the elapsed time for an event in
#seconds. The program then outputs the elapsed time in hours, minutes, and seconds. (For
#example, if the elapsed time is 9630 seconds, then the output is 2:40:30.)

# Prompt the user to input the elapsed time in seconds

seconds = int(input("Enter the elapsed time in seconds: "))

# Calculate the hours, minutes, and remaining seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

# Format the output as HH:MM:SS
formatted_time = f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

# Output the elapsed time
print("Elapsed time:", formatted_time)
