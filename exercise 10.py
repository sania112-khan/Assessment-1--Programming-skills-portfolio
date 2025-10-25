# Function to check if a number is even or odd
def check_even_odd(number):
    # The modulus operator (%) gives the remainder after division
    # If the remainder when divided by 2 is 0, the number is even
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        # Otherwise, the number is odd
        return f"The number {number} is odd."

# The main function controls the flow of the program
def main():
    # Ask the user to enter a number
    # input() takes user input as a string, so we convert it to an integer using int()
    num = int(input("Enter a number: "))

    # Call the check_even_odd() function and pass the user's number to it
    result = check_even_odd(num)

    # Print the message returned by the function
    print(result)

# This line ensures the main() function runs only when the file is executed directly
if __name__ == "__main__":
    main()
