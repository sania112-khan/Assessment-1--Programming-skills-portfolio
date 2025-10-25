Correct_Password= "12345" #defines the correct password
Max_Attempts= 5 #sets the maximum number of allowed attempts

attempts= 0   #initialize the attempts counter

#starts a loop that continues until the user uses 5 attempts

while attempts< Max_Attempts:
    entered = input("Enter password: ")    # Ask the user to enter the password
    attempts += 1                          # Increase the number of attempts by 1
    

    # Check if entered password matches the correct one
    if entered == Correct_Password:
        print("Access granted. Welcome!")  # Success message
        break                              # Exit the loop when correct
    else:
        remaining = Max_Attempts - attempts    # Calculate how many attempts are left
        if remaining > 0:
            # Inform user of wrong password and remaining tries
            print(f"Wrong password. You have {remaining} attempt(s) remaining.")
        else:
            # If all attempts used up
            print("Wrong password.")
            print("Maximum attempts reached. Authorities have been alerted.")


