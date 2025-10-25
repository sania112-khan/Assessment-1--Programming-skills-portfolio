

# Dictionary mapping month numbers to number of days
# February initially set to 28 
months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for the month number
month_number = int(input("Enter month number (1-12): "))

# Check if the input is valid
if month_number in months:
    # Special case for February
    if month_number == 2:
        # Ask user if it's a leap year
        leap_year = input("Is it a leap year? (yes/no): ").lower()

        # If leap year, February has 29 days
        if leap_year == "yes":
            print("Number of days: 29")
        else:
            # Default 28 days otherwise
            print("Number of days: 28")
    else:
        # For other months, simply print value from dictionary
        print(f"Number of days: {months[month_number]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
