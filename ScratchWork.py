# Define a function that checks if a number is even and returns a boolean value
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Call the function and store the returned value in a variable
result = is_even(6)

# Print the result
if result:
    print("The number is even.")
else:
    print("The number is odd.")
