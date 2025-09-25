# A simple program to get input from the user and display it.

# Step 1: Get input from the user.
# The `input()` function prompts the user with the message inside the parentheses
# and then waits for the user to type something and press Enter.
# The entered text is stored as a string in the 'user_input' variable.
user_input = input("Please enter your name or a short message: ")

# Step 2: Display the input back to the user.
# The `print()` function displays text on the console.
# We use an f-string to easily combine our own text with the value stored in 'user_input'.
print(f"You entered: {user_input}")

