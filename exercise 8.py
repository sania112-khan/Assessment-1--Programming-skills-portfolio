

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask user to enter a name to search
search_name = input("Enter a name to search: ")

# Check if the name exists in the list
# Using .title() to handle cases like 'sam' or 'SAM'
if search_name.title() in names:
    print(f"{search_name} was found in the list!")
else:
    print(f"{search_name} was NOT found in the list.")

