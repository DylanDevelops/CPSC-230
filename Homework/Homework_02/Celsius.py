# --------------------------------------------
# Dylan Ravel
# September 11, 2023
# Homework 02 - Celsius Assignment
# References
# 1. https://www.uptodate.com/contents/calculator-temperature-unit-conversions
#
# README
# This code converts a temperature in fahrenheit to celsius,
# while displaying the status of the program to the user.
# -----------------------------------------------

# Welcomes the user, asks for the user to type in a temperature
# in fahrenheit, converts it to a float and stores it in a variable
# called "tempInFahrenheit".
print("Welcome to the Fahrenheit to Celsius converter!")
tempInFahrenheit =  float(input("Please enter the temperature you want to convert in Fahrenheit: "))

# Tells the user it is calculating and does the calculation needed
# to convert. After that, it rounds it to the nearest 2 decimals,
# storing it in 
print("Converting " + str(tempInFahrenheit) + "F° to celsius...")
tempInCelsius = round(((tempInFahrenheit - 32) * 5/9), 2)

# Displays the output of the calculations to the console.
print(str(tempInFahrenheit) + "°F is equal to " + str(tempInCelsius) + "°C.")