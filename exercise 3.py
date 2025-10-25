#biography 




# Ask the user to enter their full name
# input() allows multiple words like "John Michael Doe"
name = input("Enter your full name: ")

# Ask the user to enter their hometown
hometown = input("Enter your hometown: ")

# Loop to keep asking for age until a valid number is entered
while True:
    age_input = input("Enter your age: ")

    # isdigit() checks if the input contains only digits (0-9)
    if age_input.isdigit():
        age = int(age_input)  # Convert from string to integer
        break  # Exit the loop once a valid age is entered
    else:
        print("Invalid age! Please enter a number only.")

# Store the information inside a dictionary
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print each piece of information on a new line
# sep="\n" prints each value on a separate line
print("\nYour Biography:")
print(biography["name"], biography["hometown"], biography["age"], sep="\n")
