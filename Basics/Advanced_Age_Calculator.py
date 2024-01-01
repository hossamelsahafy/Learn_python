#!/usr/bin/python3
# Advanced_Age_Calculator
# Write_Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name Of Time Unit ".center(80, "#"))
print("#" * 80)
age = input("what 's your age? ").strip()
# collect unite time data
unit = (
    input("Please Choose Time Unite: Months, Weeks, Days, Hours, Mins, Secs ")
    .strip()
    .lower()
)
# Get time units
months = int(age) * 12
weeks = int(months) * 4
days = int(age) * 365
hours = int(days) * 24
mins = int(hours) * 60
secs = mins * 60
try:
    if unit == "months" or unit == "m":
        print("you lived for {} months.".format(months))
    elif unit == "weeks" or unit == "w":
        print("you lived for {:,} weeks.".format(weeks))
    elif unit == "days" or unit == "d":
        print("you have lived for {:,} days.".format(days))
    elif unit == "hours" or unit == "h":
        print("You've been alive for about {:,} hours.".format(hours))
    elif unit == "mins" or unit == "m":
        print("You've been alive for {:,} minutes.".format(mins))
    elif unit == "secs" or unit == "s":
        print("You've been alive for {:,} seconds.".format(secs))
    else:
        raise ValueError("Please enter a valid unit.")
except ValueError as e:
    print(e)
