# --------------------------------------------
# Dylan Ravel
# October 6th, 2023
# Homework 03 - Celsius Assignment
# References
# 1. https://www.uptodate.com/contents/calculator-temperature-unit-conversions
# 2. https://stackoverflow.com/questions/28279732/how-to-type-negative-number-with-isdigit
#
# README
# This code converts a temperature in fahrenheit to celsius,
# while displaying the status of the program to the user. The
# updated version now has the ability to handle invalid inputs.
# -----------------------------------------------

# Declares the range of temperatures
highestTemperature = 134.06 # highest recorded temperature (Death Valley, USA)
lowestTemperature = -128.74 # lowest recorded temperature (Antarctica)

# greets the user and takes in the user input
print("Welcome to the Fahrenheit to Celsius converter!")
enteredTemperature = input("Please enter the temperature you want to convert in Fahrenheit: ")

# declares True as a general thing so it can be broken later
while True:
    # Checks if enteredTemperature (without + or -) is a digit then checks if the number is within the bounds of the max and min
    if enteredTemperature.lstrip('+-').isdigit() and float(enteredTemperature) < highestTemperature and float(enteredTemperature) > lowestTemperature:
        # if it passes the number check, it converts the string to a float and then tells the user it is calculating eventually breaking the while loop
        enteredTemperature = float(enteredTemperature)
        print(f"Converting {enteredTemperature}F° to celsius...")
        break
    else:
        # gets to here if it doesn't pass the number checks allowing the user ot have another chance to input a valid temperature
        print("That's not a valid temperature!")
        enteredTemperature = input("Please enter a valid temperature you want to convert in Fahrenheit: ")

# Does the calculations to convert from fahrenheit to celsius
tempInCelsius = round(((enteredTemperature - 32) * 5/9), 2)

# Tells the user what their converted temperature is
print(f"{enteredTemperature}°F is equal to {tempInCelsius}°C.")